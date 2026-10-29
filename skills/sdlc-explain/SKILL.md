---
name: sdlc-explain
description: Explain a prompt, git repo, problem or assignment in simple terms, as if to a junior engineer, one short interactive chunk at a time. Then offer to grill the user on the problem and the approach with grill-me skill. Use before planning, when the user says "explain", "help me understand", or hands over an assignment, repo or idea they do not know yet. Standalone.
---

Version: 1.2.0

# Explain

The goal is that I understand the problem and how to solve it, in plain words, before any technical analysis or planning. No code, no tickets, no design. Use answer-style rule for the tone and style of your response.

Input: a prompt, a git repo, a problem, or an assignment.

## 1. Read

- Prompt, assignment or problem: read the text.
- Repo: read the README, manifests, folder tree, entry points, tests and stack.
- Do not run anything unless a fact needs it.
- Finding facts is your job. Never ask me for something you can look up.

## 2. Explain in chunks

Explain one chunk at a time, in this order:

1. **What is the problem to solve?** What is wrong or missing, who is affected, why it matters.
2. **What exists today?** What is already there (repo or system). Skip it for a blank start, and say so.
3. **How will we solve it?** The approach in 3-5 steps. No files, libraries or code.
4. **How will we know it works?** The result a reviewer can check.

Rules for each chunk:

- Under 120 words. Short sentences. Literal words. No idioms, no analogies.
- Define each technical term on first use, in one sentence. Definitions stay in the chat; the glossary file belongs to `sdlc-plan`.
- Show only what the input says or what you read. Mark guesses as guesses.

After each chunk, ask one check question with the interactive question tool (`AskQuestion` in Cursor, `AskUserQuestion` in Claude Code). Without one, ask in text.

- Options: `Clear (Recommended)`, `Say it simpler`, `Go deeper`.
- On `Say it simpler` or `Go deeper`, rewrite the chunk and ask again.
- Do not start the next chunk until I say it is clear.

## 3. Offer the grill

After the last chunk, ask: "Do you want me to grill you on this, to check you understood the problem and the approach?" Options: `Yes (Recommended)`, `No`.

If yes, load the `grill-me` skill with this scope:

- Grill on the problem and the approach: what is the problem, who has the problem, what done means, constraints, why this approach, what could go wrong.
- Do not grill on the implementation: no files, libraries, code structure or tests.
- At most 3 questions per round, with the interactive question tool. This overrides the `grill-me` rule of asking the whole frontier at once.
- Facts from the repo are yours to find. Only decisions and understanding are asked.

## 4. Save and hand off

When I confirm I understand, write `.work/EXPLAIN.md`, under 250 words:

```md
# Explain
- What is the problem to solve:
- What exists today:
- How we will solve it:
- How we will know it works:
- Open questions:
```

Say: "Next: `sdlc-plan`." `sdlc-plan` reads this file when it exists.

## Stop

Do not plan, design or write code in this skill.
