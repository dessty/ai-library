# Lessons

Mistakes this skill should have prevented, and the changes made because of them.
Add a lesson from a project's `.work/RETRO.md`.
When the same lesson appears twice, change the skill, bump its `Version:` line, and record it under Changelog.

## Lessons

From the async-pdf-processing retro, 2026-11-27. These name the skill that should change. They are not applied yet.

- 2026-11-27, `sdlc-plan`: sequential-only batches are a plan smell when files do not overlap. Default to parallel workers with disjoint file sets. On this project the coding was about 3 hours 45 minutes. The retro estimated a 10-worker split at about 30 to 40 minutes. That estimate was not re-run.
- 2026-11-27, `sdlc-plan`: the 2-hour build target is agent execution time, not wall-clock calendar time. Write both clocks in the plan.
- 2026-11-27, `sdlc-plan`: pre-approved sandbox access, a worker that starts immediately, and no manual gate between safe commits. Those waits were idle time.
- 2026-11-27, `sdlc-plan`: draw the dependency graph at plan time so a parallel split is visible from the start.
- 2026-11-27, `sdlc-build`: commit at a safe checkpoint so finished work is not left only in the working tree.
- 2026-11-27, `sdlc-build`: after each merge, rebuild and run the tests before the next ticket.
- 2026-11-27, `sdlc-evals`: a headed browser run is a gate on UI tickets, not a check deferred to the end.
- 2026-11-27, `sdlc-plan`: check dependencies early. On this project `httpx` was missing from the production image, and the list API had no offset, both found after implementation.
- 2026-11-27, `sdlc-explain`: a stalled agent needs a watchdog. A watchdog is a time limit that restarts or reports a stopped agent. The docs agent stopped at 12:03 AM and was not restarted.
- 2026-11-27, `sdlc-retro`: keep model, token and cost tracking per phase. Added in version 1.1.0.

## Changelog

- 1.0.0 - first version
- 1.1.0 - record model, tokens and cost per phase, and how that spend lined up with rework
- 1.2.0 - add the 2026-11-27 async-pdf-processing lessons as checks and as a worked example
