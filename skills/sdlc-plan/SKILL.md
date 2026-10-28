---
name: sdlc-plan
description: Guide the user from a prompt, an existing repo, or an idea to a shared understanding of the work, then to tickets. Defines unknown terms, validates simple requirements with should / should not scenarios, models the system (class, data, services, flows) in Mermaid or Excalidraw, breaks the work down with a WBS, tests the riskiest assumption with a spike, and writes small tickets (GitHub issues or .work/tickets.md). Use at the start of any feature, project, assignment or assessment, after a spike or slice finishes, or when the user asks for a plan or tickets.
---

Version: 5.3.0

# Plan work

The goal is that the user understands the project and how it will be built before any code exists. Guide them one small step at a time. Plan in short cycles: detail only the next 1-2 tickets, and prove the riskiest assumption with a spike before building on it.

Do not write production code in this skill. Working files go in `.work/` at the repo root.

```
1 Intake + summary -> 2 Terms -> 3 Scope -> 4 Model -> 5 WBS -> 6 Risks + spike -> 7 Validate -> 8 Tickets
                                                                                        ^_____________|
```

## How to ask

These rules apply to every step.

- Ask with the interactive question tool when one exists: `AskQuestion` in Cursor, `AskUserQuestion` in Claude Code. Without one, use the text format below.
- At most 3 questions per round. Put the recommended option first and mark it `(Recommended)`.
- Only group questions that do not depend on each other. A question is ready when every answer it depends on is known. The others wait for a later round.
- Before each round, say in one sentence what the round decides and why it matters.
- After each round, write the answers to the files, then show a one-line summary of what changed.
- Finding facts is your job. Read the repo, the docs, or run a command. Ask the user only for decisions.
- Expand every acronym on first use in a message, or use only terms already defined in `CONTEXT.md` or `.work/GLOSSARY.md`.
- Never move to the next step while a question in the current step is open.

Text format, when there is no question tool:

```
Q1 - <title>: <question, plain words>
  a) <option> (Recommended)
  b) <option>
```

## 1. Intake

Name the input type and act on it:

| Input | First move |
|---|---|
| Prompt, assignment or assessment | Read the text. |
| Existing repo | Read the tree, README, manifests, config and tests. Find the install, run and test commands, and run the tests once. Read `CONTEXT.md`, `.work/GLOSSARY.md` and `docs/adr/` if they exist. |
| Idea or product doc (PRD) | Read it. Note the user, the problem and the value. No design yet. |

### Project summary

Before you ask any question, show a project summary. It proves you understood what the project is about. Write it from the input only, in plain words:

```md
## Project summary
- Goal: <what the project must achieve, one sentence>
- Context: <who it is for, the problem today, why it matters>
- What gets built: <the product or service, one or two sentences>
- Constraints: <deadline, time box, required stack, how the work is judged>
- Unclear: <what the input does not say; these become questions later>
```

- Keep it under 120 words. No design, no tech choices the input does not state.
- End with one line: "Tell me if this is wrong. Otherwise I'll start with the terms."
- If the user corrects it, rewrite it and show it again before step 2.
- The summary becomes the `Problem` and `Constraints` sections of `.work/BRIEF.md` in step 3.

Only after the summary, start step 2.

## 2. Terms

Make sure the user knows every word the plan will use.

1. List the jargon, business terms and acronyms in the input. Add the technical terms the plan will need.
2. Ask one multi-select question: "Which of these terms do you already know?" At most 8 terms per round.
3. For each unknown term, write a definition: what it is in 1-2 sentences, then one example from this project. Record known terms too, in one line.
4. Business terms specific to this project go in `CONTEXT.md`, in the `domain-modeling` format. Other terms (technical, industry, acronyms) go in `.work/GLOSSARY.md`.
5. Show the definitions of the unknown terms in the chat.

`.work/GLOSSARY.md` format:

```md
# Glossary

**ADK** (Agent Development Kit): Google's framework for building AI agents. In this project: runs the drill agent.

**SSE** (Server-Sent Events): A way for a server to push a stream of messages to a browser over one HTTP connection. In this project: the agent streams its answer token by token.

Known terms: Vitest (test runner). Zod (runtime schema validation).
```

- Sort entries alphabetically by term, ignoring case (`LCSW`, `Log redaction`, `LPC`).
- Keep the `Known terms:` line last, also sorted.

New terms that appear in later steps are inserted at their alphabetical place, never appended at the end.

## 3. Scope

Turn the input into simple requirements, and validate each one with the user.

Requirement format:

```md
### R1: <who> can <do what>
- Source: explicit / implied (why)
- Should: <user or app> should be able to <...>
- Should not: <user or app> should not be able to <...>
- Status: proposed / accepted
```

- One requirement is one behavior. Split anything with "and".
- Give 1-2 "should" and at least 1 "should not" scenario. Scenarios use concrete values from the project ("a psychiatrist with a DEA registration that expired yesterday").
- Mark sensitive data (PHI, PII, secrets) as a requirement when present.

Rounds:

1. Requirements: up to 3 per round, one question each, with options Accept / Edit / Drop. On Edit, ask what to change, then show the new version.
2. Decisions: open questions that change the design. Highest impact first, up to 3 per round, each with a recommended option.
3. Assumptions: anything you would otherwise assume silently. Ask them now, before the brief is final.
4. Out of scope: one question listing what you propose to leave out.

Write `.work/BRIEF.md`:

```md
# Brief

## Input
<prompt / repo / idea / PRD>

## Problem
<one paragraph, plain words>

## Constraints
- <deadline, time box, required stack, how the work is judged>

## Repo (if any)
- Stack:
- Commands: install / run / test
- Gaps:

## Requirements
<R1, R2, ... in the format above>

## Decisions
- D1: <decision> (why)

## Assumptions
- A1: <assumption> - confirmed / not confirmed

## Success criteria
- <result a reviewer can check>

## Out of scope
-
```

The step is done when every requirement is accepted or dropped, and the user confirms a 3-5 sentence summary of the scope.

## 4. Model

Show the user how the system is shaped. Write `.work/MODEL.md`. Draw only the diagrams that apply, and say which ones you skipped and why.

| Diagram | Mermaid type | When |
|---|---|---|
| Class diagram: domain entities, fields, relations | `classDiagram` | Always |
| Data model: tables, keys, relations | `erDiagram` | The project stores data |
| Services: components, external systems, databases | `flowchart` | More than one component, or an external API |
| Main flow: who calls whom, in order | `sequenceDiagram` | For the riskiest or most important flow |

- Use the names from `CONTEXT.md`.
- Keep each diagram under about 10 boxes. Split a larger one.
- Show one diagram at a time. Under it, explain in 3-5 plain sentences what the boxes and arrows mean. Then ask: Accept / Change.
- Mermaid in `.work/MODEL.md` is the source of truth, because it lives in the repo and diffs.
- If an Excalidraw MCP is available, offer an Excalidraw version of the accepted diagrams. Add the scene link under the Mermaid block. Never replace the Mermaid.
- A decision that is hard to reverse (a database choice, an append-only history) becomes an ADR through the `domain-modeling` skill.

## 5. WBS

A WBS (work breakdown structure) is a tree that splits the project into deliverables, then into work packages. Each work package becomes one ticket.

Add to `.work/BRIEF.md`:

```md
## WBS

1 <project>
├── 1.1 <capability>                      R1, R2
│   ├── 1.1.1 <work package> (S)
│   └── 1.1.2 <work package> (M)
└── 1.2 <capability>                      R3
    └── 1.2.1 <work package> (S)

| WBS | After | Files |
|---|---|---|
| 1.1.1 | S0 | src/db/*, src/providers/* |
| 1.1.2 | 1.1.1 | src/providers/* |
| 1.2.1 | S0 | src/eligibility/* |
```

- `After` lists the packages that must be done first. `Files` lists the folders or files the package will touch. Two packages can be built in parallel only when neither is after the other and their `Files` do not overlap.
- Level 2 is a capability the user or the app gets ("Check eligibility"), never a layer ("Database", "API"). Layers produce horizontal tickets that cannot be tested end to end.
- Level 3 is a vertical slice of size XS, S or M. Split anything larger.
- The children of a node cover all of its scope, and nothing outside it.
- Every requirement maps to at least one work package. Every work package maps to a requirement, or is a `chore`.
- Show the tree and ask: Accept / Change.

## 6. Risks and spike

Add to `BRIEF.md`:

```md
## Riskiest assumptions
1. <assumption> - if wrong: <consequence>
```

Keep 1-3. Rank by "most likely wrong" times "most expensive if wrong".

A spike is a small, time-limited task that answers one question. The output is an answer, not a feature. Create one spike ticket for the top risk:

```md
### [spike] <question as a yes/no question>
- Time limit: <fit the constraints>
- Test: <the smallest experiment that answers it>
- Done when: <the answer is written down>
- Code: throwaway / keep
```

Run it with `sdlc-build`. If the top risk is low, say so and skip to step 8.

## 7. Validate

After a spike or a slice, append to `.work/BRIEF.md`:

```md
## Validation <n> - <spike or ticket title>
- Answer:
- Learned:
- Decision: keep / change / drop
- Plan change:
```

If the answer changes a requirement, a diagram or the WBS, update the file and tell the user what changed.

## 8. Tickets

Create:

- One tracking ticket: the goal, the success criteria, and the WBS tree as a checklist that links to each ticket.
- Detailed tickets for the next 1-2 work packages only.
- Title-only tickets for the rest, named `<WBS id> <title>`.

Detailed ticket format:

```md
### [feat] <WBS id> <title>
- WBS: 1.1.1
- Covers: R1, R2
- Goal: <one sentence>
- Scenarios:
  - Should: <from the requirement>
  - Should not: <from the requirement>
- Acceptance criteria:
  - [ ] <checkable result>
- Tests: <one per scenario, plus edge cases>
- Model: <the part of .work/MODEL.md this ticket builds or changes>
- Size: XS / S / M
- After: <WBS ids, or none>
- Files: <folders or files it touches>
- Agent does: <what the agent implements>
- I check: <what I review by hand, and why>
```

Labels: `spike`, `feat`, `test`, `chore`.

Where tickets go:

- GitHub issues with `gh issue create` when the repo has a GitHub remote and `gh auth status` succeeds.
- Otherwise, or when the user asks: `.work/tickets.md`, same format.

Rules:

- Derive values that can go stale (status, eligibility) instead of storing them, unless a ticket says why.
- If a slice has an LLM or agent feature, list its behaviors under `AI evals` in the ticket for `sdlc-evals`. Each "should not" scenario is a candidate refusal case.

## Cursor plan mode

When this skill runs in Cursor plan mode, also write the Cursor plan. The `.work/` files stay the source of truth, because other tools cannot read a Cursor plan.

- Start the plan body with: "Build with the `sdlc-build` skill, orchestrator mode."
- Body: the project summary, the requirements (id and one line each), the WBS tree and table, the detailed tickets, and links to the `.work/` files.
- Todos: one per spike and per level 3 work package, in WBS order. The todo id is the WBS id (`s0`, `1.1.1`). Content: `[feat] 1.1.1 <title> - R1, R2 - S - after s0`.
- If plan mode cannot write the `.work/` files, put their full content in the plan body, and make the first todo `0 Write the .work/ files from this plan and commit them`.
- The `.work/` files and the base code must be committed before the build starts. Build agents work in git worktrees, and a worktree starts from the last commit.
- The user picks the models: the plan model in the chat picker, the build model in the picker next to Build.

## Stop

Show the WBS tree and the detailed tickets. Do not start building until the user says "approved".

After each spike or slice, run this skill again from step 7.
