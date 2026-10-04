---
name: hyperframe-reference-studio
description: "Build and verify local HyperFrames motion graphics from reference videos, frames, or exact SRT timing. Use for reference matching, Korean typography, reusable compositions, and MP4 verification."
---

# Hyperframe Reference Studio

Produce a local, editable HyperFrames project and a verified MP4. Start with the user's reference and requested content. This skill provides a production workflow; HyperFrames provides the rendering engine.

## Inputs and setup

- Establish the reference, replacement text, dimensions, timing, audio, and destination from the request. Ask only about consequential missing choices; continue independent source analysis.
- Check the actual OS and `node --version`, `ffmpeg -version`, `ffprobe -version`, and `npx -y hyperframes --version`. Node.js 22+, FFmpeg/ffprobe, and Python 3.10+ are required for the included helpers. Initial package/browser installation needs network access. No hosted account or API key is required for the local workflow.
- Preserve inputs and create a new output directory. Use a project-local npm cache for cache permission failures; do not blindly use sudo or change system ownership.
- Read the current [official core contract](https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-core/SKILL.md) before authoring. Pin the working CLI version in the project's package.json and record it in the report. The included example pins HyperFrames 0.8.121.

## Inspect, then reconstruct

Read [reference matching](references/reference-match.md) for a supplied reference. Extract source frames with the bundled `scripts/inspect_video.py`, inspect them, and sample entrances and exits densely enough to understand motion. A still does not establish timing.

For a local path, attempt that exact file first. An unavailable application UI does not prove the file is unreadable. Do not search unrelated private records.

Identify the actual target shot: tutorial chrome, presenter, captions, and embedded motion examples may be different subjects. Record composition geometry, type, material, visible states, easing estimates, and held states. Preserve the selected look; do not substitute a repository's default design system. State substitutions and approximations.

Build a representative frame and short motion proof before expanding a large sequence. Continue rendering already authorized by the user without an additional approval loop. A question about capability alone does not authorize publishing or a paid generation task.

## Pick the needed capability

Read [upstream capabilities](references/upstream-capabilities.md) when selecting reusable effects, complex motion, or scene transitions. It links to the official Keyframes, Registry, animation, creative, core, and CLI documents and explains the limited role of the internal Seam Craft document. These official skills are referenced, not installed or bundled by this package.

For an original starter, run `python3 scripts/new_project.py NEW_DIRECTORY` using the path to this installed skill's script. It copies `assets/studio-demo/` without overwriting an existing directory. Read [the demo guide](references/studio-demo.md), then adapt it. This is one optional light-card example, not a mandatory style for unrelated briefs.

## Build invariants

- Ship fonts locally with `@font-face` and their licenses. Resolve assets relative to the project, never an author's Downloads directory.
- Use the composition contract and a finite, seekable timeline registered under the exact composition ID. Let the framework own clip visibility; animate inner elements. Avoid wall-clock timers and unseeded randomness.
- Initialize counters and entering elements consistently under seeking. A delayed entrance must not flash its final state before starting. Preserve readable final holds.
- Keep factual claims sourced. Sample graphics are illustrative, not performance results. Do not invent percentages or credentials to fill a chart.
- If SRT is provided, read [exact subtitle timing](references/srt-timing.md). Preserve every block, character, space, line break, and timestamp. Keep gaps; one block is one scene; root duration equals the last block's end. Without an SRT, state that scene timings were authored.
- Preserve user scope. Public distribution needs rights to supplied reference assets; rebuilding them in HTML does not establish permission to redistribute the original artwork or branding.

## Completion evidence

1. Run `hyperframes lint` while iterating. For the final gate run the pinned CLI's `hyperframes check --at ...` with meaningful entrance, settled, and transition samples. Check reruns lint. Resolve errors and report remaining warnings. A skipped browser audit or zero sampled frames is not a pass.
2. Inspect preview frames. For mounted sub-compositions, inspect every scene, not just the default five overview frames. For complex motion use the official keyframe diagnostics as appropriate.
3. Render `hyperframes render -o out.mp4` using the pinned version and retain its log. Do not silently replace a render failure with a screenshot slideshow.
4. Measure `ffprobe -v error -show_entries format=duration -of csv=p=0 out.mp4`; verify dimensions and frame rate too. Exact timing failures remain failures.
5. Decode the final MP4 with `scripts/inspect_video.py VIDEO --out NEW_REVIEW_DIR --times 0,1,2 --expected-duration 3`. Choose times for the actual duration. Inspect the images: fonts, clipping, blank frames, transitions, and final hold. The script verifies metadata and extracts evidence; it does not judge visual fidelity.
6. Deliver file links, source project, commands/version, timing table, technical results, and reference differences. Distinguish user style approval from technical validation. Never claim pixel identity or a complete visual inspection from lint alone.
