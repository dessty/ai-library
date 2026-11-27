---
name: sdlc-build
description: Implement approved tickets (GitHub issues or .work/tickets.md entries). Test first, implement, run the tests, review the diff, commit, close the ticket, and log any mistake the user catches. Runs one ticket at a time, or as an orchestrator that builds independent tickets in parallel with subagents in git worktrees. Use when the user says "next ticket", "build #N", "build the plan", or approves the tickets.
---

Version: 5.4.0

# Build step

Two modes:

- Single: one ticket per call, in this chat. Use it by default, and in tools without subagents.
- Orchestrator: several tickets from the plan, built by subagents in parallel. Use it when the user asks to build the plan or several tickets.

Read tickets from GitHub (`gh issue view <n>`) or `.work/tickets.md`. The build order is in `Implementation plan` of `.work/PLAN.md`.

## Progress

Start every message of this skill with the progress header:

```
**sdlc-build** · Tickets ███░░░░░ 3/8
Now: 1.2.1 Check eligibility (Grok 4.7) · Loop step 4/9: run the tests
```

- The bar has 8 cells, filled in proportion to tickets done. The tracking ticket does not count.
- In orchestrator mode, `Now` lists every running ticket with its model.

When a ticket is done, show a banner: `✔ 1.2.1 done: committed a1b2c3d. ▶ Next: 1.3.1 Expiring-soon list.`

Also track the tickets with the to-do list tool when one exists (`TodoWrite` in Cursor and Claude Code, `update_plan` in Codex).

## Loop (single mode)

1. State the ticket, its acceptance criteria and the requirements it covers.
2. Write the tests first, at least one per scenario in the ticket. A "should" scenario is a test that the behavior works. A "should not" scenario is a test that it is rejected. Run them. Confirm they fail for the right reason.
3. Implement the smallest change that makes them pass.
4. Run the full test suite. Show the output.
5. Show the diff summary. Point out what the user should check by hand: queries, date logic, auth, sensitive data.
6. Wait for the user's review. Apply their corrections.
7. Commit with the `commit-work` skill. Subject: `<label>(<scope>): <ticket title in lower case>`, from the ticket's `Label`, `Scope` and title. Body: reference the ticket, for example `Refs #12, WBS 1.2.1`.
8. Check every acceptance criterion. Close the ticket (`gh issue close <n>`) or tick it in `.work/tickets.md`. Tick it in the tracking ticket too.
9. Say what the next ticket is. If the work changed the plan, stop and propose the change to `.work/PLAN.md` and the affected tickets.

If the code differs from `.work/MODEL.md` (a new field, table or call), update the diagram in the same commit and say so. Add any new term to `CONTEXT.md`, or to `.work/GLOSSARY.md` at its alphabetical place when that file exists.

## Orchestrator mode

You plan, dispatch, review and merge. Subagents write the code.

1. Check that the `.work/` files and the base code are committed (`git status`). If not, stop and ask to commit. A worktree starts from the last commit.
2. Pick the ready tickets: every `After` is done, and their `Files` do not overlap. At most 3 at a time.
3. Start one `best-of-n-runner` subagent per ticket, in parallel. Model by size: XS or S `grok-4.7-medium`, M `claude-sonnet-5-5-high`.
4. Show each result to the user: ticket, test output, diff summary, and the `I check` items. Wait for their review. For corrections, resume the same subagent.
5. After approval, `git cherry-pick` each commit onto the current branch, in WBS order. Rebuild, then run the full test suite in the main checkout and show the output. Do not start the next ticket until it passes. On a conflict, stop and show it.
6. Tick the todo or close the ticket. Log mistakes in `.work/build-log.md`. Remove the worktree with `git worktree remove <path>`.
7. Say which tickets are ready next. If the work changed the plan, stop and propose the change to `.work/PLAN.md` and the affected tickets.

The subagent does not see this chat. Its prompt must contain:

- The repo root path, and this instruction word for word: "Create a new git worktree of `<repo root>` from HEAD with the `/worktree` flow. Work and commit only inside it. Do not edit `<repo root>`." Without it, a subagent may start outside any worktree.
- The full ticket text, and the paths of `.work/PLAN.md`, `.work/MODEL.md`, `CONTEXT.md` and `.work/GLOSSARY.md`.
- The single-mode loop steps 1-5 above, then: commit in the worktree. Subject: `<label>(<scope>): <ticket title in lower case>`. Body: `Refs <ticket>, WBS <id>`.
- What to return: worktree path, commit hash, full test output, diff summary, the `I check` items, and anything it did not do.

## Mistake log

When the user corrects you, or a test catches a wrong implementation, append to `.work/build-log.md`:

```md
## Ticket <n> - <short title>
- Wrong: <what the agent did>
- Caught by: <user review / test name>
- Fix: <what changed>
- Prevent with: <skill or rule> - <the check that would have stopped it>
```

## Rules

- Never weaken or delete a test to make it pass. If a test is wrong, say why and ask.
- Never change a ticket silently. If it is wrong, stop and propose the change.
- If a ticket grows past size M, stop and split it.
- Commit at a safe checkpoint: tests pass and the diff is reviewed. Finished work must never sit only in the working tree.
- After each merge, rebuild and run the tests before the next ticket. In single mode, the loop's commit and test steps do this.

## After the last ticket

Copy each `build-log.md` entry into `~/.ai-library/skills/<skill>/LESSONS.md` for the skill that should have prevented it.
