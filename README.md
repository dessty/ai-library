# ai-library

My skills, rules, and agents for AI tools, kept in one place.

Each item lives here once. [Bifrost](https://github.com/dessty/bifrost-cli)
deploys it into Claude Code, Cursor, and Codex, so no tool keeps its own copy.

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
| Skill | `deploy-to-vercel` | Deploy an app to Vercel |
| Skill | `domain-modeling` | Build a project's glossary (`CONTEXT.md`) and ADRs |
| Skill | `grill-me` | Stress-test a plan with rounds of questions |
| Skill | `grill-with-docs` | `grill-me` plus `domain-modeling`, writing docs as it goes |
| Skill | `vercel-react-best-practices` | React and Next.js performance rules |
| Agent | `heimdall` | Writes and audits skills, then deploys them through Bifrost |

`rules/` is empty for now.

## Setup

```bash
bifrost init --repo https://github.com/dessty/ai-library.git
bifrost link --apply
```

`init` clones this repo into `~/.ai-library`. Set `BIFROST_HOME` to use a
different folder. `link --apply` creates the links in each tool.

## Making a change

1. Edit the files in `~/.ai-library`, or in a separate clone.
2. Run `bifrost validate`.
3. Run `bifrost link --apply`.

If you edit a separate clone, push it first. Then run `bifrost sync --apply`
to pull the change into `~/.ai-library`, and link again.

After renaming or deleting a skill, run `bifrost doctor --fix`. `link` only
adds links, so the link for the old name stays until `doctor` removes it.
