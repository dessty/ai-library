# To-do

- Iterate on `scripts/check-docs.py`. It checks the README contents table against the skill folders, the rules, and the agent yaml files.
- Done: the hook source is `scripts/pre-commit`. Run `sh scripts/install-hooks.sh` once per clone. That copies it to `.git/hooks/pre-commit` and makes it executable. The hook runs `scripts/check-docs.py` and blocks the commit when the check fails.
