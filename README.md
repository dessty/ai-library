# ai-library

My skills, rules, and agents for AI tools, kept in one place.

Each item lives here once. Install [Bifrost](https://github.com/dessty/bifrost-cli), then use Bifrost to deploy the library into Claude Code, Cursor, and Codex, so no tool keeps its own copy.

## Layout

```
.
├── config.toml                 # Bifrost settings (tools, git, scripts, logging)
├── skills/<name>/SKILL.md      # one folder per skill, optional scripts
├── rules/                      # markdown rules, compiled into each tool's rules file
└── agents/
    ├── <name>.yaml             # agent source, compiled for Claude Code and Cursor
    └── <name>/                 # notes for that agent, not deployed
```

A skill's folder name must match the `name` field in its `SKILL.md`.
Bifrost only deploys agent files that sit directly in `agents/`.

## Contents

| Kind | Name | Use |
|---|---|---|
| SDLC-* workflow | | |
| Skill | `sdlc-explain` | Explain a prompt, repo or problem in plain words, one chunk at a time, then an optional grill |
| Skill | `sdlc-plan` | Prompt, repo or idea -> tech-spec plan: scenarios, diagrams, WBS, tickets; guided rounds |
| Skill | `sdlc-build` | One ticket: test first, implement, review, commit, close, log mistakes |
| Skill | `sdlc-evals` | Evaluate an LLM or agent feature and save a receipt |
| Skill | `sdlc-retro` | After a project, review the work and record lessons for the other SDLC skills |
| --- | --- | --- |
| Skill | `commit-work` | Review, split and write clean commits |
| Skill | `deploy-to-vercel` | Deploy an app to Vercel |
| Skill | `domain-modeling` | Build a project's glossary (`CONTEXT.md`) and ADRs |
| Skill | `grill-me` | Stress-test a plan with rounds of questions |
| Skill | `grill-with-docs` | `grill-me` plus `domain-modeling`, writing docs as it goes |
| Skill | `vercel-react-best-practices` | React and Next.js performance rules |
| Rule | `sdlc-workflow` | Plan first, small steps, tests, explicit assumptions |
| Rule | `answer-style` | How to write answers to me |
| Rule | `commit-convention` | Commit message format |
| Rule | `steve-voice` | My written voice |
| Agent | `heimdall` | Writes and audits skills, then deploys them through Bifrost |

## Development workflow

`sdlc-explain` (optional: problem and approach in plain words) -> `sdlc-plan` (scope, model, WBS, tickets; calls `domain-modeling`) -> `sdlc-build` (one ticket at a time, or parallel subagents in Cursor) -> `sdlc-evals` (only for AI features).
Tickets are GitHub issues, or `.work/tickets.md` when there is no GitHub access. Working files go in `.work/` in the project repo.

## Improving skills

`sdlc-explain`, `sdlc-plan`, `sdlc-build` and `sdlc-evals` keep a `LESSONS.md` with lessons and
a changelog. `sdlc-build` logs agent mistakes in `.work/build-log.md`, and
`sdlc-evals` logs scores in `.work/receipts.jsonl`. After a project, move lessons
into the skill that should have prevented them. When a lesson repeats, edit the
skill and bump its `Version:` line.

## Bifrost

Bifrost is a command line tool. It deploys AI skills from the AI library into Claude Code, Cursor, and Codex.

Install Bifrost. Then use Bifrost to deploy the library:

```bash
bifrost init --repo https://github.com/dessty/ai-library.git
bifrost link --apply
```

`init` clones this repo into `~/.ai-library`. Set `BIFROST_HOME` to use a different folder. `link --apply` creates the links in Claude Code, Cursor, and Codex.

## Making a change

1. Edit the files in `~/.ai-library`, or in a separate clone.
2. Run `bifrost validate`.
3. Run `bifrost link --apply`.

If you edit a separate clone, push it first. Then run `bifrost sync --apply`
to pull the change into `~/.ai-library`, and link again.

After renaming or deleting a skill, run `bifrost doctor --fix`. `link` only
adds links, so the link for the old name stays until `doctor` removes it.
