# Tech spec template

Template for `.work/PLAN.md`. Sections fill up step by step. If a section or subsection does not apply, write `Not needed: <why>`.

```md
---
title: <project>
author: <from git config user.name>
reviewers: <left empty for the user>
status: draft|approved
updated: YYYY-MM-DD HH:MM:SS
---

## 1. Problem statement
### Problem
> <one paragraph, plain words: what is wrong or missing, who is affected, why it matters>
### Constraints
- <required stack, how the work is judged>
### Requirements
<R1, R2, ... in the requirement format from TEMPLATES.md>
### Goals
- <result a reviewer can check>
### Non-goals
-

## 2. Technical approach
### Approach
> <3-5 sentences: how the system solves the problem>
### Current system
<existing repo only: stack, install / run / test commands, gaps>
### Model
<links to the diagrams in MODEL.md, added in step 3>
### APIs
| Method | Path | Purpose |
|---|---|---|
### Decisions
- D1: <decision>
  - Why: <reason>
  - Consequence: <the rule the code must follow because of it>

## 3. Alternatives considered
- C1: <option not chosen>. Rejected: <why>.

## 4. Dependencies & risks
- Dependencies: <external services, teams, data>
- Security and privacy: <sensitive data (PHI, PII, secrets) and how it is protected>
- Performance: <limits that matter, Core Web Vitals>
- Assumptions: A1: <assumption> - confirmed / not confirmed

## 5. Implementation plan
<WBS tree, table and build order, added in step 4>

## 6. Testing & monitoring
### Tests
<unit and integration tests; each scenario becomes a test, added in step 5>
```
