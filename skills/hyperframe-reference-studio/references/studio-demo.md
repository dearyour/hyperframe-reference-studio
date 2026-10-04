# Studio demo

`assets/studio-demo/` is an original six-second vertical composition about a reference-to-render workflow. It uses a large contact frame, a drawn motion path, and a compact film strip. It has no third-party product logo, borrowed reference footage, personal data, or account connection.

Canvas: 1080 × 1920. Duration: 6 seconds. Rate: 30 fps. Audio: none. The visible time/frame labels describe the demo timeline, not an execution benchmark or a claim that automated validation already passed.

The bundled Noto Sans KR font is distributed with its SIL OFL license. GSAP is a pinned npm dependency copied locally by `npm run setup`; its vendor file is not committed to this repository. HyperFrames is also a pinned npm dependency. After dependency installation, font and animation assets are resolved from the local project.

```sh
python3 /path/to/installed/skill/scripts/new_project.py ./my-video
cd my-video
npm ci
npm run setup
npm run lint
npm run check
npm run render
ffprobe -v error -show_entries format=duration -of csv=p=0 out.mp4
```

Expected duration: `6.000000`. `new_project.py` refuses existing destinations, so do not point it at the installed template or an existing project. Edit the copied `index.html`. Keep the example's sample caption and timing only when they fit the user's request.

For a different reference, replace the layout and motion with the measured target. This example is a starting point, not a claim of universal design quality or pixel-identical cross-platform rendering.
