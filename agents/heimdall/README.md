<div align="center">

<img src="heimdall-logo.png" width="180" alt="Heimdall">

# Heimdall

**The gatekeeper for this library.**

</div>

Heimdall is the agent you talk to. You describe a skill, rule, or agent;
Heimdall writes it into this repo, checks it against what is already here,
and tells [Bifrost](https://github.com/dessty/bifrost-cli) to deploy it.

Bifrost is the bridge. It does not decide what a skill *means*. It moves
files into Claude Code, Cursor, and Codex and records what it moved.

Heimdall never writes into `.claude/`, `.cursor/`, or `.codex/` itself.
Those folders are generated. Edit the library, then re-link.

---

## How it works

```
you  →  Heimdall  →  this library  →  Bifrost  →  each tool
              │              │
         decides,        skills/
         writes,         rules/
         checks          agents/
```

1. You ask: `add a skill for writing conventional commits`
2. Heimdall picks a scope — global (this repo) by default, project only if you say so
3. It searches the library for the same name, the same job under another name, or a contradictory rule
4. On a conflict it stops: *Hold. Which one stands?*
5. Otherwise it writes the files here
6. It runs `bifrost validate`, then `bifrost link --apply`
7. If `[git] auto_push` is on, it commits and pushes

The definition Cursor (and later other tools) should load is [`Heimdall.md`](Heimdall.md). The greeting banner is [`banner.txt`](banner.txt).

---

## In this folder

| File | Role |
|---|---|
| `Heimdall.md` | The agent prompt — source of truth |
| `heimdall-logo.png` | Mark used in this README |
| `banner.txt` | ASCII mark printed on first greeting |
| `README.md` | This file |

---

## Using it in Cursor

Cursor reads a single file at `~/.cursor/agents/heimdall.md`. Point that at this folder:

```bash
ln -sf "$(pwd)/agents/heimdall/Heimdall.md" ~/.cursor/agents/heimdall.md
```

Run that from the library root (or use an absolute path). Then: *Use the heimdall subagent to add a skill…*

Bifrost does not yet deploy markdown agent folders into Cursor. Until it does, the symlink is the deploy step.

---

## What it will not do

- Write directly into a tool's config folder
- Approve a script it just wrote
- Overwrite or delete without asking
- Resolve a conflict silently — between skills, between scopes, or in git
- Edit Bifrost's `state.json`

If a skill ships a script and `require_script_approval` is on, the script stays inert until you approve it through `bifrost validate`. An agent that can write scripts and also green-light them is not a gate.

---

## Voice

Plain, except at the two moments the job is literally “gatekeeper”:

- Greeting: the banner, then *Heimdall here. What do you need watched over?*
- Stopping you: *Hold. `db-migrations` already exists… Which one stands?*

Status, lists, and errors read like a tool.
