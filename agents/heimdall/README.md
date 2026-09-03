# Heimdall

Gatekeeper for the Bifrost skill store. You talk to this agent; Bifrost deploys
what it writes.

## Store files

| Path | What it is |
|---|---|
| `agents/heimdall.yaml` | The payload Bifrost links (Claude Code agents directory) |
| `agents/heimdall/README.md` | This file |

Bifrost only loads `*.yaml` / `*.yml` files sitting directly in `agents/`. This
folder is documentation. Do not move the yaml file in here — it would stop
deploying.

## What it does

Writes skills, rules, and agents into `BIFROST_HOME` (default `~/.bifrost`),
checks for name and content overlap, then runs:

1. `bifrost validate --json`
2. `bifrost link --apply --json`

It never writes into `.claude/`, `.cursor/`, or `.codex/` itself.

## Scope

Global by default. Project overlay (`<repo>/.bifrost/`) only when you ask for it.

## Boundaries

- Does not delete payloads without confirmation
- Does not approve its own scripts
- Does not resolve conflicts silently
- Does not edit `state.json`

## Related

- CLI: `bifrost`
- Existing Cursor copy (hand-managed, not from this store): `~/.cursor/agents/heimdall.md`
