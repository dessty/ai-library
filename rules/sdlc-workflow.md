---
name: sdlc-workflow
description: My SDLC workflow with AI agents. The rules the agent always follows, and a how-to for the sdlc- skills.
---

# SDLC workflow

My way to take work from a prompt, a repo or an idea to tested, committed code with an AI agent.
I decide and review. The agent implements. Plans stay small and are proven with spikes before I build on them.

## Rules (always)

Apply to any task bigger than a one-line fix.

1. Plan first. Never write code before I approve the plan or ticket.
2. Work in small steps. Write the test first, then the implementation.
3. Run the tests after every step and show the output.
4. State assumptions explicitly. Ask before inventing requirements.
5. No PHI, PII or secrets in code, logs, fixtures or prompts. Use parameterized queries only.
6. Use the stack named in the brief or ticket. Do not add a dependency without saying why.
7. When you are unsure, say so. Do not guess and present it as fact.

## The flow

```
sdlc-plan ──> sdlc-build ──> sdlc-plan (step 7) ──> sdlc-build ──> ... ──> sdlc-evals
 terms         spike          validate              next ticket            AI features only
 scope         first          update tickets
 model, WBS
 tickets
```

## The pieces

| Piece | When | Output |
|---|---|---|
| `sdlc-plan` | Start of any work, and after each spike or slice | `.work/BRIEF.md`, `.work/GLOSSARY.md`, `.work/MODEL.md`, tickets |
| `domain-modeling` | Called by `sdlc-plan` | `CONTEXT.md` (domain glossary), `docs/adr/` (decisions) |
| `sdlc-build` | One ticket at a time | tests, code, one commit per ticket, `.work/build-log.md` |
| `commit-work` | Called by `sdlc-build` | clean commits |
| `sdlc-evals` | Only when the work has an LLM or agent feature | scorecard, `.work/receipts.jsonl` |

## How to use it

1. Start: "sdlc-plan" plus a prompt, a repo, or an idea.
2. Answer the rounds of questions (at most 3 at a time): terms I don't know, requirements, decisions.
3. Review the diagrams, the WBS, the spike ticket and the first tickets. Say "approved".
4. "sdlc-build" the spike. Read the answer.
5. "sdlc-plan" again. It records the decision (keep / change / drop) and updates the next tickets.
6. "sdlc-build #N" for each ticket. Review every diff before it is committed.
7. AI feature? "sdlc-evals" after each change to the prompt, model or tools.

Every `sdlc-plan` and `sdlc-build` message starts with a progress header: the current step, or the ticket bar. A banner marks each step change.

## In Cursor: plan mode and parallel build

1. Plan mode (Opus): run `sdlc-plan`. The Cursor plan's todos are the spike and the WBS work packages. The todo id is the WBS id.
2. Commit the `.work/` files.
3. Build (Opus in the Build picker): `sdlc-build` in orchestrator mode. Independent tickets go to parallel subagents in git worktrees: Grok 4.7 for XS and S, Sonnet 5.5 for M. I review each diff before it is merged.

## Terms

- Spike: a small, time-limited task that answers one question. The output is an answer, not a feature.
- Vertical slice: a small change that works end to end and can be tested.
- Ticket: a GitHub issue, or an entry in `.work/tickets.md` when there is no GitHub access.
- Scenario: one concrete "should" or "should not" example of a requirement. Each scenario becomes a test.
- WBS (work breakdown structure): a tree that splits the project into capabilities, then into work packages. Each work package is one ticket.
- Eval: a fixed input with an expected AI behavior (answer, tool call, refusal). Unit tests check code. Evals check model behavior.
- Receipt: one JSON line per eval run: commit, model, prompt version, score, failed cases.

## Files in a project

```
.work/
├── BRIEF.md         problem, constraints, requirements, WBS, risks, validation decisions
├── GLOSSARY.md      technical and industry terms, acronyms
├── MODEL.md         class, data, service and flow diagrams (Mermaid)
├── tickets.md       only when not using GitHub issues
├── build-log.md     mistakes the agent made and how I caught them
├── evals.md         AI eval cases
└── receipts.jsonl   eval score history
CONTEXT.md           domain glossary
docs/adr/            hard-to-reverse decisions
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
