# Lessons

Mistakes this skill should have prevented, and the changes made because of them.
Add a lesson from an assignment's `.work/build-log.md`.
When the same lesson appears twice, change the skill, bump its `Version:` line, and record it under Changelog.

## Lessons

- async-pdf-processing, 2026-11-27: finished work was left only in the working tree. Prevent with: a commit at a safe checkpoint.
- async-pdf-processing, 2026-11-27: the next ticket started before the merged code was rebuilt and tested. Prevent with: rebuild and run the tests after each merge, before the next ticket.

## Changelog

- 1.0.0 - first version
- 2.0.0 - simplified to a 3-skill workflow
- 3.0.0 - short planning cycles: intake by input type, spike first, tickets (GitHub issues or .work/tickets.md)
- 4.0.0 - renamed with the sdlc- prefix
- 4.1.0 - one test per ticket scenario, keep `.work/MODEL.md` and the glossary in sync, re-plan from `sdlc-plan` step 7
- 4.2.0 - new glossary terms inserted alphabetically
- 5.0.0 - orchestrator mode: parallel subagents in git worktrees, model by ticket size, cherry-pick after review
- 5.1.0 - progress header with ticket bar on every message, ticket-done banners
- 5.1.1 - glossary terms only when `.work/GLOSSARY.md` exists
- 5.2.0 - no spikes; reads `.work/PLAN.md`; plan changes are proposed by the build, not by re-running `sdlc-plan`
- 5.3.0 - commit subject built from the ticket: `<label>(<scope>): <title>`. No Cursor plan todos; build order read from `.work/PLAN.md`
- 5.4.0 - commit at a safe checkpoint so finished work is not left only in the working tree; rebuild and run the tests after each merge, before the next ticket
