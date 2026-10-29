---
name: sdlc-workflow
description: My SDLC workflow with AI agents. The rules the agent always follows, and a how-to for the sdlc- skills.
---

# SDLC workflow

My way to take work from a prompt, a repo or an idea to tested, committed code with an AI agent.
I decide and review. The agent implements. The plan is a short tech spec that breaks the work into small tickets.

## Rules (always)

Apply to any task bigger than a one-line fix.

1. Plan first. Never write code before I approve the plan or ticket.
2. Work in small steps. Write the test first, then the implementation.
3. Run the tests after every step and show the output.
4. State assumptions explicitly. Ask before inventing requirements.
5. No PHI, PII or secrets in code, logs, fixtures or prompts. Use parameterized queries only.
6. Use the stack named in the plan or ticket. Do not add a dependency without saying why.
7. When you are unsure, say so. Do not guess and present it as fact.

## The flow

```
sdlc-explain ··> sdlc-plan ──> sdlc-build ──> sdlc-build ──> ... ──> sdlc-evals
 optional         scope         ticket 1       ticket 2              AI features only
 problem          model
 approach         WBS
 grill            tickets
```

## The pieces

| Piece | When | Output |
|---|---|---|
| `sdlc-explain` | Optional, before planning, when I don't know the problem yet | `.work/EXPLAIN.md` |
| `sdlc-plan` | Start of any work | `.work/PLAN.md`, `.work/MODEL.md`, `.work/GLOSSARY.md` (optional), tickets |
| `domain-modeling` | Called by `sdlc-plan` | `CONTEXT.md` (domain glossary) |
| `sdlc-build` | One ticket at a time | tests, code, one commit per ticket, `.work/build-log.md` |
| `commit-work` | Called by `sdlc-build` | clean commits |
| `sdlc-evals` | Only when the work has an LLM or agent feature | scorecard, `.work/receipts.jsonl` |

## How to use it

1. Start: "sdlc-explain" if I don't know the problem yet, then "sdlc-plan" plus a prompt, a repo, or an idea.
2. Answer the rounds of questions (at most 3 at a time): requirements, decisions, assumptions.
3. Review the diagrams, the WBS and the tickets. Say "approved".
4. "sdlc-build #N" for each ticket. Review every diff before it is committed. If a ticket changes the plan, the build stops and proposes the change.
5. AI feature? "sdlc-evals" after each change to the prompt, model or tools.

A banner marks each step change in `sdlc-plan`. Every `sdlc-build` message starts with the ticket bar.

## Parallel build

1. Run `sdlc-plan`. Section 5 of `.work/PLAN.md` groups the tickets in batches that can run in parallel.
2. Commit the `.work/` files.
3. Run `sdlc-build` in orchestrator mode. Independent tickets go to parallel subagents in git worktrees: Grok 4.7 for XS and S, Sonnet 5.5 for M. I review each diff before it is merged.

## Terms

- Ticket: a GitHub issue, or an entry in `.work/tickets.md` when there is no GitHub access. Each ticket works end to end and can be tested.
- Scenario: one concrete "should" or "should not" example of a requirement. Each scenario becomes a test.
- WBS (work breakdown structure): a tree that splits the project into features, then into tasks. Each task is one ticket.
- Eval: a fixed input with an expected AI behavior (answer, tool call, refusal). Unit tests check code. Evals check model behavior.
- Receipt: one JSON line per eval run: commit, model, prompt version, score, failed cases.

## Files in a project

```
.work/
├── EXPLAIN.md       problem, today, approach, done when (from sdlc-explain)
├── PLAN.md          tech spec: problem, approach, alternatives, risks, implementation plan (WBS), testing
├── MODEL.md         class, data model, component and sequence diagrams (Mermaid), one ## per diagram
├── GLOSSARY.md      project terms and acronyms (optional, asked first)
├── tickets.md       only when not using GitHub issues
├── build-log.md     mistakes the agent made and how I caught them
├── evals.md         AI eval cases
└── receipts.jsonl   eval score history
CONTEXT.md           domain glossary
```

## Improving the system

1. After a project, read `.work/build-log.md`.
2. Copy each lesson into `skills/<skill>/LESSONS.md` of the skill that should have prevented it.
3. When a lesson appears twice, edit the skill, bump its `Version:` line, and add a changelog line.
4. Compare later eval receipts to see if the change helped.

## Changing the workflow

All files live in `~/.ai-library`. Bifrost deploys them to Claude Code, Cursor and Codex.

```bash
cd ~/.ai-library
bifrost validate
bifrost link --apply
bifrost doctor --fix   # after renaming or deleting a skill
```
