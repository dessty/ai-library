# Templates

Shapes used by the `sdlc-plan` steps. The rules for filling them are in `SKILL.md`.

## Project summary (step 1)

```md
## Project summary
- Goal: <what the project must achieve, one sentence>
- Context: <who it is for, the problem today, why it matters>
- What gets built: <the product or service, one or two sentences>
- Constraints: <deadline, time box, required stack, how the work is judged>
- Unclear: <what the input does not say; these become questions later>
```

## Glossary entry (step 1)

```md
# Glossary

**SSE** (Server-Sent Events): A way for a server to push a stream of messages to a browser over one HTTP connection. In this project: the agent streams its answer token by token.
```

## Requirement (step 2)

```md
#### R1: <who> can <do what>
- Source: explicit / implied (why)
- Should: <user or app> should be able to <...>
- Should not: <user or app> should not be able to <...>
- Status: proposed / accepted / dropped
```

## WBS (step 4)

```md
1 Credentialing service
├── 1.1 Register providers and credentials      scope: providers     R1, R2
│   ├── 1.1.1 Set up the project and database (S)
│   ├── 1.1.2 Add a provider (S)
│   └── 1.1.3 Add a credential to a provider (M)
└── 1.2 Check if a provider can see patients    scope: eligibility   R3
    └── 1.2.1 Answer yes or no for a state and date (S)

Levels: 1 = project · 1.1 = feature · 1.1.1 = task (one ticket)

| WBS | Label | After | Files |
|---|---|---|---|
| 1.1.1 | chore | none | package.json, src/db/* |
| 1.1.2 | feat | 1.1.1 | src/providers/* |
| 1.1.3 | feat | 1.1.2 | src/credentials/* |
| 1.2.1 | feat | 1.1.1 | src/eligibility/* |

Build order: Batch 1: 1.1.1 · Batch 2: 1.1.2, 1.2.1 (parallel) · Batch 3: 1.1.3
```

## Tracking ticket (step 5)

```md
### Plan: <project>
- Plan: .work/PLAN.md
- Goals: <from PLAN.md>
- Batch 1: [ ] 1.1.1 <title>
- Batch 2: [ ] 1.1.2 <title> · [ ] 1.2.1 <title>
```

## Ticket (step 5)

```md
### <title>
- WBS: 1.1.1
- Label: feat / chore / test
- Scope: <the level 2 scope word>
- Covers: R1, R2
- Goal: <one sentence a non-technical person understands: who gets what, and why>
- Scenarios:
  - Should: <from the requirement>
  - Should not: <from the requirement>
- Acceptance criteria:
  - [ ] <checkable result>
- Tests: <one per scenario, plus edge cases>
- Model: <links to the MODEL.md diagrams this ticket builds or changes>
- Size: XS / S / M
- After: <WBS ids, or none>
- Files: <folders or files it touches>
- Agent does: <what the agent implements>
- I check: <what I review by hand, and why>
- AI evals: <expected AI behaviors for sdlc-evals, or none>
```
