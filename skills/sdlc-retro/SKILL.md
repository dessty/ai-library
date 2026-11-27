---
name: sdlc-retro
description: After a project is complete, review the chats, agents, commits and test results, find gaps in the SDLC steps, and record which model, token count and cost each phase used. Propose edits to the other SDLC skills. Use when the user says "retro", or when a finished project should improve the skills. Does not edit the other skills. Standalone.
---

Version: 1.2.0

# Retro

The goal is a report of what the SDLC steps missed on a finished project, plus suggested edits to the skills. Do not edit those skills in this run.

The suite is `sdlc-explain`, `sdlc-plan`, `sdlc-build` and `sdlc-evals`. There is no single `skills.md`. A suggested edit names the skill file to change (`SKILL.md` or `LESSONS.md`).

SDLC means the steps in this suite: explain, plan, build, then evals when the work has an LLM or agent feature. A gap is a step a skill requires that did not happen, or a repeated mistake the skill did not prevent.

Use the answer-style rule for the chat. The report file can be longer.

## When

Run this after the project is complete. The tickets are done, or the user says the work is finished. Do not run it in the middle of a build.

## 1. Read the project

Finding facts is your job. Read what is on disk. Do not ask for a path you can find.

- `.work/EXPLAIN.md`, `.work/PLAN.md`, `.work/MODEL.md`, `.work/tickets.md`, `.work/build-log.md`, `.work/evals.md`, `.work/receipts.jsonl` and `CONTEXT.md`, when they exist.
- `git log` and `git status` for the project. Note commits, and work left uncommitted.
- Test results the user already ran, or the latest test output in the logs. Do not re-run the suite unless a result is missing and a run is safe. Say which results you ran and which you only read.

## 2. Read the chats and agents

- This chat, and any agent transcript the user names or that is clearly about this project.
- Subagent results: what they changed, and whether a person reviewed the diff before it was committed.
- If a transcript is missing, say so. Do not invent what an agent did.

## 2b. Models, tokens and cost

A model is the named system that wrote or reviewed a phase, such as Grok 4.7. A token is one piece of text the model reads or writes. Cost is money, only when a price per token is in the logs or the user gives one.

For each phase or ticket, collect what the logs actually contain:

- Which model ran it. Use the name written in the chat, the subagent prompt, or `.work/receipts.jsonl`. One row per phase. A phase is explain, plan, build of one ticket, or evals.
- Token counts, if a log or receipt stores them. Keep input and output separate when both are present. If only a total is present, label it total.
- A cost estimate, if a price is present. Multiply tokens by that price and show the arithmetic. If no price is present, write "no price" and do not guess a dollar amount.

Then write a short correlation. A correlation is a link you can point at, not a guess. Compare model choice and token spend with outcomes already in the record: a failed test, a `.work/build-log.md` entry, an extra commit that fixed the same ticket, or a clean first pass. Say when a more capable model lines up with less rework, and when it does not. If the logs have no model or no token count, say "not in the logs" for that phase. Do not invent a model, a token count, or a price.

## 3. Read the four skills

Read each `SKILL.md` and `LESSONS.md` for `sdlc-explain`, `sdlc-plan`, `sdlc-build` and `sdlc-evals`, from `~/.ai-library/skills/`.

Check at least:

- Explain: the problem was stated in plain words and saved, or planning started from a guess.
- Plan: requirements, scenarios and tickets exist, and the build followed them.
- Build: tests first, tests shown, review before commit, mistakes logged in `.work/build-log.md`.
- Evals: if the project has an LLM or agent feature, evals were run and a receipt was saved. If it has no such feature, say evals were not required.
- Lessons: a mistake in `.work/build-log.md` that is not yet in the skill that should have prevented it.
- Plan: tickets run one after another even though their files do not overlap. That is a plan smell. A plan smell is a shape that hides work which could run at the same time. The plan should show the dependency graph at plan time, name which tickets can run together, and keep two clocks separate. Agent execution time is time the model is working. Wall-clock time is time on the calendar, including waits.
- Plan: a missing module or a missing API field found only after implementation.
- Build: work left uncommitted with no safe checkpoint, and no test run or rebuild after a merge.
- Evals: a headed browser run left until the end, instead of a gate on each ticket that changes the UI. A gate is a check that must pass before the next ticket starts.
- Explain: an agent that stops and is not restarted. Record the time it stalled.

## Example: async-pdf-processing, 2026-11-26 to 2026-11-27

Coding ran from 9:16 PM to 1:01 AM, about 3 hours 45 minutes, with long stretches of one ticket after another. The brief's build cap is 2 hours. Treat that cap as agent execution time. Do not mix it with wall-clock time.

On the next retro, look for the same shapes:

- Batches stayed sequential where files did not overlap. This retro estimated that 10 workers with disjoint files could have done that coding in about 30 to 40 minutes. That estimate was not re-run.
- The dependency graph was not drawn at plan time, so the parallel split was not visible from the start.
- Idle time came from sandbox approval, slow worker start, and a manual gate between commits.
- Safe checkpoint commits were not automatic. A merge was not followed by a rebuild and a test run.
- Headed browser tests waited until the end.
- `httpx` was missing from the production image, and list offset was missing from the API, both found after implementation.
- A docs agent stopped at 12:03 AM and was not restarted.

Record model, tokens and cost for each phase, as in section 2b. Do not drop that when you add these checks.

## 4. Write the report

Write `.work/RETRO.md` in the project. Do not change application code.

```md
# Retro
- Project:
- Window:
- Sources read:

## Gaps
| Skill | What it requires | What happened | Suggested change |
|---|---|---|---|

## Spend
| Phase or ticket | Model | Tokens | Cost | Outcome |
|---|---|---|---|---|

## Spend notes
- What lined up with less rework:
- What did not:
- Missing from the logs:

## Suggested edits
### <skill>/SKILL.md
- Add or change:
- Why:
- Lesson it would have caught:

## Not changed
The skill files were not edited.
```

In chat, lead with how many gaps, then the table. Stay under 250 words unless the user asks for the full report.

## Stop

Do not edit `SKILL.md`, `LESSONS.md`, or any other skill file. Do not bump a version. Ask before applying a suggested edit.
