---
name: sdlc-plan
description: Turn a prompt, an existing repo, or an idea into an executable plan, like a tech spec plus tasks (WBS). Validates simple requirements with should / should not scenarios, models the system in Mermaid or Excalidraw, and writes small tickets for sdlc-build, grouped so independent tickets can be built in parallel by subagents. Use at the start of any feature, project, assignment or assessment, or when the user asks for a plan or tickets.
---

Version: 6.0.0

# Plan work

The output is an executable plan: a tech spec (`.work/PLAN.md`), diagrams (`.work/MODEL.md`) and tasks. Each task is one ticket. Tickets are grouped so independent ones can be built in parallel, in an order that gives a working result early. Do not write production code.

Files next to this one: `TECH-SPEC.md` (the `PLAN.md` template) and `TEMPLATES.md` (the other shapes).

## How to ask

- Use the interactive question tool (`AskQuestion` in Cursor, `AskUserQuestion` in Claude Code). Without one, number the questions and list the options as `a)`, `b)`.
- At most 3 questions per round. Recommended option first, marked `(Recommended)`.
- Group only questions that do not depend on each other. The others wait for a later round.
- Before a round, say in one sentence what it decides. After it, update the files and say in one line what changed.
- Find facts yourself: read the repo or docs, or run a command. Never make up an assumption. Ask when unsure.
- Expand every acronym on first use, unless it is defined in `CONTEXT.md` or `.work/GLOSSARY.md`.
- Never move to the next step while a question is open.

## Step changes

Steps: 📥 1. Intake · 🎯 2. Scope · 📊 3. Model · 🗂️ 4. WBS · 🎫 5. Tickets. Use the emoji every time you name a step.

When the step changes, show this banner as rendered markdown, never inside a code block:

````md
---
## ✅ 🎯 Step 2 of 5: Scope (Complete!)
8 requirements accepted, 1 dropped.

## ▶️▶️▶️ 📊 Step 3 of 5: Model (in progress...)
First, the class diagram.
````

Never skip a step on your own. Ask: "Skip 📊 Step 3: Model? Why: <reason>." Options: `Skip`, `Do it anyway`, recommended first. On `Skip`, show `## ❌ 📊 Step 3 of 5: Model (Skipped)` and the reason.

Track the 5 steps with the to-do list tool when one exists (`TodoWrite`, or `update_plan` in Codex).

## 1. 📥 Intake

If `.work/EXPLAIN.md` exists, read it first. Do not explain again what the user confirmed there.

| Input | First move |
|---|---|
| Prompt, assignment or assessment | Read the text. |
| Existing repo | Read the tree, README, manifests, config and tests. Find the install, run and test commands, and run the tests once. Read `CONTEXT.md`, `.work/GLOSSARY.md` and `docs/adr/` if they exist. |
| Idea or product doc (PRD) | Read it. Note the user, the problem and the value. No design yet. |

**Project summary.** Before any question, show the project summary (`TEMPLATES.md`), written from the input only.

- Under 120 words. No design, no tech choices the input does not state.
- Put the `Open questions` of `.work/EXPLAIN.md` in `Unclear`.
- Then ask in one round: "Is this summary right?" (`Yes`, `Change it`), and, if `.work/GLOSSARY.md` does not exist, "Create `.work/GLOSSARY.md` with this project's terms?" (`Yes (Recommended)`, `No`). On `Change it`, rewrite and ask again.
- In `PLAN.md`, Goal and Context become `Problem`, Constraints become `Constraints`. Unclear items become step 2 questions.

**Glossary.** If `.work/GLOSSARY.md` exists, update it as new terms appear.

- One entry per term (`TEMPLATES.md`): what it is in 1-2 sentences, then one example from this project.
- Keep entries sorted alphabetically.
- Business terms specific to this project go in `CONTEXT.md`, in the `domain-modeling` format.

## 2. 🎯 Scope

Turn the input into simple requirements (`TEMPLATES.md`), and validate each one.

- One requirement is one behavior. Split anything with "and".
- 1-2 "should" and at least 1 "should not" scenario, with concrete values from the project.
- Sensitive data (PHI, PII, secrets) is a requirement when present.

Rounds:

1. Requirements: up to 3 per round, options Accept / Edit / Drop. On Edit, ask what to change, then show the new version.
2. Decisions that change the design, highest impact first. The chosen option goes in `Decisions`, the others in `Alternatives considered`.
3. Assumptions and non-goals, in one round: the assumptions you would otherwise make silently, and one question listing what you propose to leave out.

Write `.work/PLAN.md` from `TECH-SPEC.md`.

- If a section does not apply, write `Not needed: <why>`. Never invent content to fill it.
- Draft `Dependencies & risks` yourself. Ask only about points that change the design.

The step is done when every requirement is accepted or dropped.

## 3. 📊 Model

Write `.work/MODEL.md`. Draw only the diagrams that apply, and say which ones you skipped and why.

| Diagram | Mermaid type | When |
|---|---|---|
| Class diagram: domain entities, fields, relations | `classDiagram` | Always |
| Data model (ER diagram, MCD): tables, keys, relations | `erDiagram` | The project stores data |
| Component diagram: system parts, external services, databases, and their links | `flowchart` | More than one component, or an external API |
| Sequence diagram: who calls whom, in order, for one flow | `sequenceDiagram` | For the 1-3 most important flows |

- One `##` heading per diagram, named after its type: `## Class diagram`, `## Data model (Entity/Relation diagram)`, `## Component diagram`, `## Sequence diagram: <flow name>`.
- Link each diagram from `### Model` in `PLAN.md`: `[Sequence diagram: Check eligibility](MODEL.md#sequence-diagram-check-eligibility)`.
- Use the names from `CONTEXT.md`. Keep each diagram under about 10 boxes.
- Show all diagrams in one message. Under each, 3-5 plain non-technical sentences on what the boxes and arrows mean. Then ask one question: Accept all / Change one (which).
- Mermaid is the source of truth. If an Excalidraw MCP is available, add the offer of an Excalidraw version to the same question.
- Fill `### APIs` in `PLAN.md` when the system exposes endpoints.
- A design choice made while modeling goes in `### Decisions`, and the options not chosen in `Alternatives considered`.

## 4. 🗂️ WBS

A WBS (work breakdown structure) splits the project into features (level 2), then into tasks (level 3). Write it in `Implementation plan` of `PLAN.md`, in the `TEMPLATES.md` format: tree, levels legend, `After` / `Files` table, build order.

- `After`: tasks that must be done first. `Files`: code files or folders the task changes. Tasks in the same batch run in parallel, so neither is after the other and their `Files` do not overlap.
- Put shared groundwork (scaffold, schema, shared types) in one early `chore` task under the first feature. Keep `After` links few and `Files` apart.
- A feature is something the user or the app gets, never a layer ("Database", "API"). Its `scope` is one short lower-case word, used as the commit scope.
- A task is one ticket of size XS, S or M. It works end to end and can be tested. Only the groundwork task may skip end to end.
- Every requirement maps to at least one task. Every task maps to a requirement, or is a `chore`.

Naming. Labels become ticket titles and commit messages, so a junior developer or a non-technical person must understand them:

- Feature: what a user or the app can do. "Check if a provider can see patients", not "Eligibility engine".
- Task: a verb and the visible result, at most 50 characters. "Show credentials that expire in 60 days", not "Expiry query + cron".
- No jargon, no undefined acronyms, no file, library or function names. Read each line aloud: if an outsider would not understand it, rename it.

Show the tree and the build order, and ask: Accept / Change.

## 5. 🎫 Tickets

Write the tickets to `.work/tickets.md` (`TEMPLATES.md`):

- One tracking ticket: the goals, a link to `PLAN.md`, and a checklist of all tickets, grouped by batch.
- One ticket per task. The title is the task label only; the WBS id stays in the `WBS` field.
- Labels: `feat` (user-visible behavior), `chore` (groundwork, config), `test` (tests only).
- `sdlc-build` turns each ticket into its commit message: `<label>(<scope>): <title in lower case>`.
- Derive values that can go stale (status, eligibility). Do not store them.
- Fill `Testing & monitoring` in `PLAN.md`: the tests from the ticket scenarios, or `Not needed: <why>`.
- For an LLM or agent feature, fill `AI evals` for `sdlc-evals`. Each "should not" scenario is a candidate refusal case.

## Stop

Show the tickets. Do not start building until the user says "approved". Then:

1. Set `status: approved` and `updated` in the `PLAN.md` header.
2. If the repo has a GitHub remote and `gh auth status` succeeds, create the GitHub issues from `.work/tickets.md`. Create missing labels first with `gh label create`.
3. Say: "Commit `.work/`, then run `sdlc-build`."
