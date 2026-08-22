# my-skills-library

The library Bifrost deploys and Heimdall watches. Skills, rules, and agents
live here once; each AI tool gets its own copy through Bifrost.

```
.
├── config.toml
├── skills/     # folders with SKILL.md
├── rules/      # markdown
└── agents/     # Heimdall, and later other agents
```

Heimdall is first in. Cursor reads `agents/heimdall.md` (point
`~/.cursor/agents/heimdall.md` at it). Bifrost currently deploys YAML agents
to Claude only — this markdown file is the source of truth until that adapter
exists.

```bash
bifrost init --repo https://github.com/dessty/my-skills-library.git
```
