# Hyperframe Reference Studio

**An independent Codex skill for turning visual references into verified, editable motion graphics.**

Read the reference. Rebuild its layout and timing. Render locally with [HyperFrames](https://github.com/heygen-com/hyperframes). Inspect the actual MP4.

[한국어 안내](README.ko.md) · [Demo video](docs/media/studio-demo.mp4) · [Verification](docs/VERIFICATION.md)

<img src="docs/media/studio-demo.gif" width="360" alt="Original six-second demo: a reference composition, a moving path, and a film strip entering in sequence">

## Install in Codex

```sh
npx skills add dearyour/hyperframe-reference-studio --skill hyperframe-reference-studio --agent codex --global --copy --yes
```

This uses the open-source [Skills CLI](https://github.com/vercel-labs/skills). Restart Codex or start a new session after installation. Omit `--global` to install only in the current project. Installing this skill does not install video dependencies or connect an account.

Then ask Codex:

> $hyperframe-reference-studio Analyze this reference video and rebuild its card layout and motion with my text. Make a 1080×1920 MP4. Preserve the supplied SRT exactly, render locally, and inspect the final video before reporting completion.

**No Manus login, Manus credits, or hosted video account is required.** Codex writes the project; the HyperFrames CLI renders it. The local workflow needs Node.js 22+, Python 3.10+, FFmpeg/ffprobe, and disk space for dependencies and Chromium. Network access is needed for initial installation and optional upstream components. Your AI coding assistant's own usage limits and charges still apply.

## What it includes

- A reference analysis workflow: composition, typography, material, entrances, exits, holds, and evidence.
- Exact SRT rules: one block per scene, unchanged text and timing, gaps preserved, measured final duration.
- Guidance on when to consult the official Keyframes, Registry, animation, and internal Seam Craft documents. These upstream skills are **linked, not bundled or automatically installed**.
- A portable, original six-second example with a locally bundled Korean font and editable HTML/GSAP.
- A safe project copier and an FFmpeg helper that checks duration and extracts frames for inspection.

The skill teaches a process. It is not an automatic pixel-matching model, a hosted service, or a guarantee that any reference can be reproduced exactly. User references and project-specific content are supplied separately. The demo is an optional starting point, not a style imposed on every project.

## Try the bundled project

After a global installation:

```sh
python3 ~/.codex/skills/hyperframe-reference-studio/scripts/new_project.py ./my-video
cd my-video
npm ci
npm run setup
npm run lint
npm run check
npm run render
ffprobe -v error -show_entries format=duration -of csv=p=0 out.mp4
```

Expected duration: `6.000000`. The copier refuses an existing destination. Change the script path if your Codex skill directory is customized. The example pins HyperFrames `0.8.121` and GSAP `3.15.0`; first rendering may download Chromium. `npm run setup` copies GSAP and its upstream license notice from the installed dependency into project-local assets.

For a repository checkout, use `python3 skills/hyperframe-reference-studio/scripts/new_project.py ./my-video` instead. See [the demo guide](skills/hyperframe-reference-studio/references/studio-demo.md) and [upstream capabilities](skills/hyperframe-reference-studio/references/upstream-capabilities.md).

## Evidence, not just a successful command

The workflow requires lint, sampled browser checks, an actual MP4 render, exact duration measurement, and inspection of frames decoded from that MP4. The helper alone does not judge visual quality. If duration, a render command, or a visual requirement fails, report the failure and next action instead of claiming completion.

Automated helper tests run with `python3 -m unittest discover -s tests -v`. FFmpeg/ffprobe are required for the video tests. An optional [GitHub Actions example](docs/ci-example.yml) is included as documentation; no CI workflow is enabled by this repository.

## License and attribution

Original skill text, helper code, and demo composition: [Apache-2.0](LICENSE). Bundled Noto Sans KR: SIL Open Font License 1.1. Installed GSAP: its own Standard License. See [third-party notices](skills/hyperframe-reference-studio/THIRD_PARTY_NOTICES.md).

This is an independent project, not an official HeyGen, HyperFrames, Manus, or OpenAI product. It does not contain a proprietary Manus skill export. The upstream HyperFrames project supplies the engine and public technical documentation. Only redistribute reference artwork, logos, fonts, footage, and audio when you have the necessary rights.
