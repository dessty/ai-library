---
name: sdlc-plan
description: Turn a prompt, an existing repo, or an idea into a brief, a spike that tests the riskiest assumption, and small tickets (GitHub issues or .work/tickets.md). Plans in short cycles instead of one dense plan. Use at the start of any feature, assignment, take-home or live exercise, after a spike finishes, or when the user asks for a plan or tickets.
---

Version: 4.0.0

# Plan work

Plan in short cycles. Detail only the next 1-2 slices. Prove the riskiest assumption with a spike before building on it.

Do not write production code in this skill. Working files go in `.work/` at the repo root.

```
1 Intake -> 2 Brief + grill -> 3 Risks -> 4 Spike -> 5 Validate -> 6 Tickets
                                             ^__________________________|
```

## 1. Intake

Name the input type and act on it:

| Input | First move |
|---|---|
| Prompt or assignment | Brief from the text |
| Existing repo | Read the tree, README, manifests, config and tests. Find the install, run and test commands, and run the tests once. Read `CONTEXT.md` and `docs/adr/` if they exist. Then brief. |
| Idea | Brief on the user, the problem and the value. No design yet. |

## 2. Brief and grill

Write `.work/BRIEF.md`:

```md
# Brief

## Input
<prompt / repo / idea>

## Problem
<one paragraph, plain words>

## Repo (if any)
- Stack:
- Commands: install / run / test
- Gaps:

## Requirements
- R1: <explicit>
- R2: <implied> (why)

## Open questions
- Q1: <question> - options: <a / b> - impact: <low / high>

## Success criteria
- <result a reviewer can check>

## Out of scope
-
```

- Number every requirement.
- Mark sensitive data (PHI, PII, secrets) as a requirement when present.
- Call the `grill-with-docs` skill on the open questions, highest impact first. Stop when the user confirms shared understanding. Update `BRIEF.md`.

## 3. Risks

Add to `BRIEF.md`:

```md
## Riskiest assumptions
1. <assumption> - if wrong: <consequence>
```

Keep 1-3. Rank by "most likely wrong" times "most expensive if wrong".

## 4. Spike

A spike is a small, time-limited task that answers one question. The output is an answer, not a feature.

Create one spike ticket for the top risk:

```md
### [spike] <question as a yes/no question>
- Time limit: <15 min in a timed round, 1-2 days at work>
- Test: <the smallest experiment that answers it>
- Done when: <the answer is written down>
- Code: throwaway / keep
```

Run it with `sdlc-build`. If the top risk is low, say so and skip to step 6.

## 5. Validate

After the spike, append to `.work/BRIEF.md`:

```md
## Validation <n> - <spike title>
- Answer:
- Learned:
- Decision: keep / change / drop
- Plan change:
```

## 6. Tickets

Create:

- One tracking ticket: the goal, success criteria, and a checklist that links to each child ticket.
- Detailed tickets for the next 1-2 vertical slices only. A vertical slice is a small change that works end to end and can be tested.
- Title-only tickets for the rest of the backlog.

Detailed ticket format:

```md
### [feat] <slice title>
- Covers: R1, R2
- Goal: <one sentence>
- Acceptance criteria:
  - [ ] <checkable result>
- Tests: <key cases, including edge cases>
- Size: XS / S / M
- Agent does: <what the agent implements>
- I check: <what I review by hand, and why>
```

Labels: `spike`, `feat`, `test`, `chore`. Split anything larger than M.

Where tickets go:

- Default: GitHub issues with `gh issue create`. Check `gh auth status` first.
- Timed round, no GitHub access, or the user asks: `.work/tickets.md`, same format.

Design notes (schema, API) go in the ticket that needs them, not in a separate dense plan. A decision that is hard to reverse becomes an ADR through `domain-modeling`.

Rules:

- Derive values that can go stale (status, eligibility) instead of storing them, unless a ticket says why.
- If a slice has an LLM or agent feature, list its behaviors under `AI evals` in the ticket for `sdlc-evals`.

## Stop

Show the tickets. Do not start building until the user says "approved".

After each slice or spike, run this skill again from step 5 to update the next tickets.

In a timed round: intake and brief 5 min, grill 10 min, risks and spike ticket 5 min, tickets 5 min. Run the spike first in the live session.
