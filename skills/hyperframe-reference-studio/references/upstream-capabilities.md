# Official HyperFrames capability map

This file routes to upstream documents; it does not vendor or install them. Read only the layer relevant to the task and verify commands against the project's pinned CLI. Repository `main` changes over time.

| Need | Read |
|---|---|
| Composition IDs, root duration, clip placement and media ownership | [Core](https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-core/SKILL.md) |
| CLI, diagnostics, preview and MP4 render | [CLI](https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-cli/SKILL.md) |
| Zoom, reframe, continuous subject motion, masks, SVG or 3D | [Keyframes](https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-keyframes/SKILL.md) |
| Find an existing chart, effect, caption or transition | [Registry](https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-registry/SKILL.md) |
| Broader motion choreography and runtime adapters | [Animation](https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-animation/SKILL.md) |
| Composition, typography, palette and beat planning | [Creative](https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-creative/SKILL.md) |

For named effects, search the registry before rebuilding one. Use English search descriptions even when on-screen copy is Korean. Review the selected component and its license, then adapt it to the reference. Installing a component is not evidence that its geometry or timing fits this composition. Network access is needed to fetch its files.

For demanding motion, use the official `keyframes` diagnostics and a focused rendered shot. A moving bounding box does not establish correct mask, text, WebGL or 3D behavior. Judge the visible subject and inspect the actual frames.

## Scene seams

[Seam Craft](https://github.com/heygen-com/hyperframes/blob/main/.claude/skills/seam-craft/SKILL.md) is marked `internal: true` by the upstream project. It describes render prerequisites used by a particular launch-video assembly workflow, not a general transition library. Consult it when a seam exposes the canvas, loses the outgoing hold or blends in the wrong order. Do not assume its injector scripts or placeholder tokens exist in this project.

Use the current core/animation contract to implement transitions. Verify the stage background, clip intervals, layer order and final poses immediately before, during and after every boundary. For exact SRT timing, preserve subtitle visibility boundaries even if decorative backgrounds overlap. Do not change source timestamps just to fit an upstream transition recipe.

The engine's Apache-2.0 license and upstream attribution are documented in the repository's third-party notices. Referenced skills are maintained by HeyGen; this package's workflow and demo are independent.
