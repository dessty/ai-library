---
name: commit-work
description: Create clean git commits. Review and stage only the intended changes, split them into logical commits, and write each message. Use when the user asks to commit, write a commit message, stage changes, or split work into several commits.
---

Each commit holds only the intended changes, covers one logical change, and has a message that says what changed and why.

## Workflow

1. **Inspect the working tree.**
   - `git status`
   - `git diff` for unstaged changes, `git diff --stat` when there are many.
   - Note any change you did not make. Leave it unstaged and tell the user, unless they asked you to commit it.

2. **Decide the commit boundaries.** Split by:
   - feature vs refactor
   - backend vs frontend
   - formatting vs logic
   - tests vs production code
   - dependency bumps vs behavior changes

3. **Stage only what belongs in the next commit.**
   - Stage by path: `git add <path>`.
   - Unstage by path: `git restore --staged <path>`.
   - `git add -p` and `git restore --staged -p` wait for keyboard input, so they do not work from an agent. If one file mixes two changes, ask the user to split it, or write a patch for one part and stage it with `git apply --cached <patch>`.

4. **Review what will be committed.** Run `git diff --cached` and check for:
   - secrets or tokens
   - leftover debug logging
   - unrelated formatting changes

5. **Describe the staged change in one or two sentences:** what changed, and why. If you cannot, the commit is too big or mixed. Go back to step 2.

6. **Run the smallest useful check** before committing: the repo's fastest unit test, lint, or build for the files touched. Report a failure. Do not commit around it.

7. **Write the message** following the `commit-convention` rule. Commit without an editor:

   ```bash
   git commit -F - <<'EOF'
   type(scope): subject

   Optional body.
   EOF
   ```

8. **Repeat** until every intended change is committed.

## Do not

- Push, unless the user asks.
- Amend, rebase, or force-push a commit that is already pushed.
- Commit with `--no-verify` to skip a failing hook.

## Report

For each commit, give:

- the hash and the message
- one line on what changed and why
- the checks you ran, and their result

End with any changes you left unstaged.
