# Scripts

## check-docs.py

Checks the README contents table against the files on disk. A skill is `skills/<name>/SKILL.md`. A rule is a file in `rules/`. An agent is a `.yaml` file directly in `agents/`.

The check fails if a table link points at a missing file, or if a skill, rule, or agent on disk is missing from the table. It prints one line per problem and exits with an error. It does not edit files.

Run it from the repo root:

```bash
python3 scripts/check-docs.py
```

## pre-commit

This is the git hook source. Git runs it before each commit. It runs `scripts/check-docs.py`. If the check fails, the commit is blocked.

## install-hooks.sh

Copies `scripts/pre-commit` to `.git/hooks/pre-commit` and makes that file executable. Run it once per clone:

```bash
sh scripts/install-hooks.sh
```
