# Verification

Verified on 2026-10-05 with macOS 27 (Apple silicon), Node.js 22.12.0, HyperFrames 0.8.121, GSAP 3.15.0, and FFmpeg/ffprobe 9.0.2.

## Rendered artifact

- [Demo MP4](media/studio-demo.mp4): H.264, 1080 × 1920, 30 fps, 180 frames, no audio.
- Measured duration: **6.000000** seconds.
- SHA-256: `8d693da89b8c97498a78d947ac19d8ba6f98fae6e2baada8b1cb0f6ce9897d26`.
- Screenshot capture with hardware GPU; the local render completed in 19.4 seconds. This is one observed run, not a performance promise.

## Commands and results

Run from the copied demo project:

```sh
npm ci
npm run setup
npm run lint
npm run check
npm run render
ffprobe -v error -show_entries format=duration -of csv=p=0 out.mp4
```

- Lint: 0 errors, 0 warnings.
- Browser check at 0, 0.5, 1, 2, 3, 4, 5, and 5.966666 seconds: 8 layout samples, 0 layout issues, 0 runtime or motion findings, 67/67 contrast checks passing.
- Render: completed, 180/180 frames.
- ffprobe output: `6.000000`.
- Six Python helper tests passed: portable copy, overwrite refusal, symlink refusal, mismatched duration rejection, invalid timestamp rejection, and actual frame/manifest output.
- Codex skill frontmatter validator: valid.

The engine also reports that the 3.7 MB Korean font exceeds its 2 MB HTML-inlining threshold. The font is intentionally shipped as a local file. Keep the **whole project folder**, including assets; copying only `index.html` is insufficient. This notice does not prevent the project-folder check or MP4 render.

## Visual review

Frames were decoded from the final MP4 at 0, 0.25, 0.5, 1, 1.5, 2.5, 3.5, 4.5, and 5.966666 seconds and inspected as a contact sheet. The initial background, sequential panel entrances, Korean text, moving path, film-strip progression, and final hold were visible as authored. The final frame was also reviewed at full resolution. No reference-fidelity score is claimed for this original demo.

## Authored timing

There is no input SRT in this example.

| Element | Entrance | Motion / final hold |
|---|---:|---|
| Header and title | 0.00–0.73 s | Hold through 6.00 s |
| Reference panel | 0.15–0.80 s | Art motion settles by 4.15 s |
| Motion panel | 0.64–1.29 s | Path animates 1.25–4.05 s |
| Film panel | 1.12–1.77 s | Film strip and playhead settle by 4.70 s |
| Footer | 1.60–2.10 s | Hold through 6.00 s |

Rendering on other browser/OS versions may change pixels or encoding bytes. Duration and structural checks should still be rerun locally.

## Public installation check

The repository and raw skill file were accessible without authentication. The Skills CLI installed the skill from the public GitHub URL into a clean temporary Codex project:

```sh
npx -y skills add dearyour/hyperframe-reference-studio --skill hyperframe-reference-studio --agent codex --copy --yes
```

All 18 installed skill files matched the published source. The installed helper created a new project containing the font, licenses, lockfile, and source. `npm ci`, setup, lint (0 errors and 0 warnings), and rendering succeeded from that new project. Its MP4 again measured `6.000000` seconds. The project-scoped install was used for this test to avoid altering an existing global skill directory.

These are local execution results. GitHub Actions is not enabled; `ci-example.yml` is an optional workflow example.
