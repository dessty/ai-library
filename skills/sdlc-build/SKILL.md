---
name: sdlc-build
description: Implement one approved ticket (GitHub issue or .work/tickets.md entry). Test first, implement, run the tests, review the diff, commit, close the ticket, and log any mistake the user catches. Also runs spikes. Use when the user says "next ticket", "build #N", or approves the tickets.
---

Version: 4.1.0

# Build step

Do one ticket per call. Read it from GitHub (`gh issue view <n>`) or `.work/tickets.md`.

For a `spike` ticket: run the smallest experiment, respect the time limit, write the answer, then hand back to `sdlc-plan` step 7. Skip steps 2 and 7 unless the spike code is kept.

## Loop

1. State the ticket, its acceptance criteria and the requirements it covers.
2. Write the tests first, at least one per scenario in the ticket. A "should" scenario is a test that the behavior works. A "should not" scenario is a test that it is rejected. Run them. Confirm they fail for the right reason.
3. Implement the smallest change that makes them pass.
4. Run the full test suite. Show the output.
5. Show the diff summary. Point out what the user should check by hand: queries, date logic, auth, sensitive data.
6. Wait for the user's review. Apply their corrections.
7. Commit with the `commit-work` skill. Reference the ticket, for example `Refs #12`.
8. Check every acceptance criterion. Close the ticket (`gh issue close <n>`) or tick it in `.work/tickets.md`.
9. Say what the next ticket is. If the work changed what comes next, run `sdlc-plan` from step 7.

If the code differs from `.work/MODEL.md` (a new field, table or call), update the diagram in the same commit and say so. Add any new term to `CONTEXT.md` or `.work/GLOSSARY.md`.

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

## After the last ticket

Copy each `build-log.md` entry into `~/.ai-library/skills/<skill>/LESSONS.md` for the skill that should have prevented it.
