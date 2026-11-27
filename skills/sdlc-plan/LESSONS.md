# Lessons

Mistakes this skill should have prevented, and the changes made because of them.
Add a lesson from an assignment's `.work/build-log.md`.
When the same lesson appears twice, change the skill, bump its `Version:` line, and record it under Changelog.

## Lessons

- mock1-credentialing: 6 design questions in one plain-text message. The user answered "ok" to all of them, so the answers were accepted, not understood. Four assumptions appeared after the grill. Prevent with: at most 3 independent questions per round, through the interactive question tool, and assumptions asked before the brief is final.
- mock1-credentialing: the brief used terms and acronyms (NPI, DEA, LCSW, compact) without checking that the user knew them. Prevent with: a Terms step before Scope, and a glossary.
- async-pdf-processing, 2026-11-27: batches were sequential although the files did not overlap, so coding took about 3 hours 45 minutes. Prevent with: parallel workers on disjoint `Files` by default, and the dependency graph drawn at plan time.
- async-pdf-processing, 2026-11-27: the 2-hour build target was read as wall-clock time. It is agent execution time. Waits for sandbox access, worker start and manual gates were idle time. Prevent with: two clocks written in the plan, and no planned idle time.
- async-pdf-processing, 2026-11-27: `httpx` was missing from the production image, and the document list API had no `offset`. Both were found after implementation. Prevent with: a dependency check before any code.

## Changelog

- 1.0.0 - first version
- 2.0.0 - simplified to a 3-skill workflow
- 3.0.0 - short planning cycles: intake by input type, spike first, tickets (GitHub issues or .work/tickets.md)
- 4.0.0 - renamed with the sdlc- prefix
- 5.0.0 - guided rounds of at most 3 questions, Terms step with `.work/GLOSSARY.md`, requirements with should / should not scenarios, Model step (`.work/MODEL.md`, Mermaid, optional Excalidraw), WBS, no timed mode, no `grill-with-docs` call
- 5.1.0 - project summary (goal, context, what gets built, constraints, unclear) shown before any question
- 5.2.0 - `.work/GLOSSARY.md` sorted alphabetically; new terms inserted in place
- 5.3.0 - Cursor plan mode output (todo id = WBS id); `After` and `Files` per work package for parallel builds
- 5.4.0 - progress header on every message, step-change banners, steps tracked in the to-do list tool
- 5.5.0 - reads `.work/EXPLAIN.md` from `sdlc-explain`; asks before creating `.work/GLOSSARY.md`
- 6.0.0 - shorter, tech-spec style: 5 steps (Intake, Scope, Model, WBS, Tickets). `.work/PLAN.md` replaces `BRIEF.md` and links to diagrams in `MODEL.md`. Removed the flow diagram, the Terms step (one glossary question instead), risky assumptions, spikes and the Validate loop. Every ticket is detailed. "Slice" is now "ticket"; component diagram replaces service diagram. No progress header; step-change banners stay. Build order in batches for parallel tickets. Step emojis. Plain-language naming rules for WBS labels and ticket titles, with a commit scope per capability. `PLAN.md` follows the standard tech spec sections (header, problem statement, technical approach, alternatives considered, dependencies and risks, implementation plan, testing and monitoring); no ADR files. Templates moved to `TECH-SPEC.md` and `TEMPLATES.md`, Cursor plan mode removed, so `SKILL.md` stays under 1,500 words. Review fixes: tickets go to `.work/tickets.md` first and to GitHub only after approval; ticket title without the WBS id; fewer question rounds (summary and glossary together, assumptions and non-goals together, all diagrams reviewed at once, no final scope confirmation)
- 6.1.0 - parallel workers on disjoint `Files` by default, dependency graph drawn at plan time, agent execution time and wall-clock time written separately, no planned idle time, dependency check before any code. `SKILL.md` is now about 1,640 words, over the 1,500 target from 6.0.0
