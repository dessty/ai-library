# my-skills-library

The library Bifrost deploys and Heimdall watches. Skills, rules, and agents
live here once; each AI tool gets its own copy through Bifrost.

```
.
├── config.toml
├── skills/<name>/SKILL.md
├── rules/                 # markdown
└── agents/<name>/Heimdall.md   # one folder per agent
```

Heimdall is first in. See [`agents/heimdall/README.md`](agents/heimdall/README.md).
The prompt is `agents/heimdall/Heimdall.md`. Point Cursor at it:

```bash
ln -sf /path/to/my-skills-library/agents/heimdall/Heimdall.md ~/.cursor/agents/heimdall.md
```

Bifrost currently deploys top-level YAML agents to Claude only. These
markdown folders are the source of truth until that adapter exists.

```bash
bifrost init --repo https://github.com/dessty/my-skills-library.git
```
