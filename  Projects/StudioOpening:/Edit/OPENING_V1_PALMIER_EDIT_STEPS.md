# FLYSTAR77 STUDIO Opening Version 1 Palmier Edit Steps

Status: edit plan only. Do not execute timeline edits yet.

## Studio Rules

- Never overwrite original files.
- Always create a new version when editing.
- Preserve cinematic pacing.
- Use minimal transitions.
- Emotion before spectacle.
- Never modify selected master files.
- Ask before deleting or replacing assets.

## Timeline Settings

- Timeline name: `FLYSTAR77_STUDIO_Opening_V1`
- Resolution: `1920x1080`
- FPS: `24`
- Aspect ratio: `16:9`
- Total duration: `446 frames`
- Total time: `18.583s`
- Transition style: hard cut only, except opening fade-in and final fade-out.
- Source handling: import/reference source media only. Do not rename, overwrite, delete, or replace any source asset.

Palmier frame convention:

- `startFrame` is inclusive.
- `endFrame` is exclusive.
- `durationFrames = endFrame - startFrame`.
- Visible last frame is `endFrame - 1`.

## Source Assets

| CUT | Role | Source file | Source duration | Source resolution | Source fps | Use |
|---|---|---|---:|---|---:|---|
| CUT01 | Blue light birth / opening breath | `Assets:/Videos:/01_光が生まれる:/Output:/CUT01_青い光が生まれる.mp4` | ~5.02s | 1280x720 | ~24.12 | Use first 96 frames |
| CUT02 | FLYSTAR77 logo completion | `Assets:/Videos:/02_FLYSTAR77ロゴ完成/Output:/FLYSTAR77ロゴ完成_採用.mp4` | ~5.02s | 1280x720 | ~24.12 | Use first 108 frames |
| CUT03 | RUI looking toward the future | `Assets:/Videos:/ 03_RUI_未来を見る/Selected:/ cut03_rui_breathing_slowpush_final.mp4` | ~5.04s | 1916x1080 | 24.00 | Use full source |
| CUT04 | Stars / light expansion | `Assets:/Videos:/04_STARS_光が広がる/Output:/CUT04_STARS_BASE_v1 0.48.36.mp4.mp4` | ~5.04s | 1920x1080 | 24.00 | Use full source |

## Timeline Placement

| Order | CUT | startFrame | endFrame | lastVisibleFrame | durationFrames | startTime | endTime | Source trim |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | CUT01 | 0 | 96 | 95 | 96 | 00:00.000 | 00:04.000 | `trimStartFrame: 0`, visible length `96f` |
| 2 | CUT02 | 96 | 204 | 203 | 108 | 00:04.000 | 00:08.500 | `trimStartFrame: 0`, visible length `108f` |
| 3 | CUT03 | 204 | 325 | 324 | 121 | 00:08.500 | 00:13.542 | full source |
| 4 | CUT04 | 325 | 446 | 445 | 121 | 00:13.542 | 00:18.583 | full source |

## Palmier Placement Steps

1. Create or open a new Palmier project/timeline for `FLYSTAR77_STUDIO_Opening_V1`.
2. Set project settings to `1920x1080`, `24fps`, `16:9`.
3. Import the four source files as read-only references. Do not alter the source files.
4. Place all four clips on the main video track in the exact order below.
5. Keep transitions as cuts. Do not add cross dissolves between CUTs.
6. Apply only the opening fade-in and final fade-out.

### Clip Placement Values

| CUT | Track | startFrame | durationFrames | media action |
|---|---|---:|---:|---|
| CUT01 | `V1_main` | 0 | 96 | Place from source frame 0. Cut at timeline frame 96. |
| CUT02 | `V1_main` | 96 | 108 | Place from source frame 0. Cut at timeline frame 204. Hold logo after completion inside this 4.5s window. |
| CUT03 | `V1_main` | 204 | 121 | Place full selected master. Do not trim unless manually approved. |
| CUT04 | `V1_main` | 325 | 121 | Place full source. Use the non-copy file `CUT04_STARS_BASE_v1 0.48.36.mp4.mp4`. |

## Transform / Scale / Position

Canvas center:

- Pixel position: `x: 960`, `y: 540`
- Normalized center: `x: 0.5`, `y: 0.5`

| CUT | Source resolution | Fill method | Scale | Position | Normalized transform reference |
|---|---|---|---:|---|---|
| CUT01 | 1280x720 | Scale to fill 1920x1080, no crop | `150.00%` | center `960,540` | top-left `0,0`, size `1.0 x 1.0` |
| CUT02 | 1280x720 | Scale to fill 1920x1080, no crop | `150.00%` | center `960,540` | top-left `0,0`, size `1.0 x 1.0` |
| CUT03 | 1916x1080 | Scale to fill width, tiny vertical crop acceptable | `100.21%` | center `960,540` | top-left approx `0,-0.001`, size approx `1.0 x 1.002` |
| CUT04 | 1920x1080 | Native fit | `100.00%` | center `960,540` | top-left `0,0`, size `1.0 x 1.0` |

Transform notes:

- CUT01 and CUT02 share the same 16:9 aspect ratio as the final timeline. Scaling to `150%` fills the canvas cleanly.
- CUT03 is slightly narrower than 1920px. Use fill-width scaling to avoid side bars. The crop is visually negligible.
- CUT04 is already native 1920x1080. Do not scale unless needed for framing.

## Fade / Transition Settings

| CUT | In transition | Out transition | Fade settings |
|---|---|---|---|
| CUT01 | Fade in from black | Hard cut to CUT02 | Opacity `0%` at frame 0, `100%` at frame 12. Fade-in duration `12f / 0.5s`. |
| CUT02 | Hard cut | Hard cut to CUT03 | No fade. Preserve logo hold inside the 108-frame duration. |
| CUT03 | Hard cut | Hard cut to CUT04 | No fade. Preserve selected master pacing. |
| CUT04 | Hard cut | Fade out to black | Opacity `100%` through clip-relative frame 97, then `0%` at frame 121. Fade-out duration `24f / 1.0s`. |

If Palmier uses clip fade controls instead of opacity keyframes:

- CUT01: `fadeInFrames: 12`, `fadeOutFrames: 0`
- CUT02: `fadeInFrames: 0`, `fadeOutFrames: 0`
- CUT03: `fadeInFrames: 0`, `fadeOutFrames: 0`
- CUT04: `fadeInFrames: 0`, `fadeOutFrames: 24`

## Audio Handling

- Keep embedded audio tracks available, but do not raise them aggressively.
- If embedded audio is distracting, reduce clip audio to a low bed rather than muting immediately.
- No external BGM file is currently present in the project.
- Before adding BGM or replacing audio, ask for approval.

Suggested default clip audio:

| CUT | Suggested volume |
|---|---:|
| CUT01 | `-12dB` to `-18dB`, subtle |
| CUT02 | `-12dB` to `-18dB`, subtle |
| CUT03 | `-10dB` to `-16dB`, preserve breathing/atmosphere if useful |
| CUT04 | `-12dB` to `-18dB`, fade with picture |

## Export Settings

Export only after user approval.

- Mode: `video`
- Format: `mp4`
- Codec: `H.264`
- Resolution: `1080p` or `Match Timeline`
- Timeline resolution: `1920x1080`
- Timeline FPS: `24`
- Output name: `FLYSTAR77_STUDIO_Opening_V1_1920x1080_24fps.mp4`
- Output location: `FLYSTAR77/Exports/`
- Overwrite: `false`

Recommended absolute export path:

`/Users/yamamotohiroshi/Documents/Codex/2026-06-21/p/FLYSTAR77/Exports/FLYSTAR77_STUDIO_Opening_V1_1920x1080_24fps.mp4`

## Pre-Edit Checklist

- Confirm Palmier project settings are `1920x1080 / 24fps`.
- Confirm all four source files are imported and visible in the media library.
- Confirm CUT03 uses the selected master file only as a source reference.
- Confirm no source files are renamed, overwritten, deleted, or replaced.
- Confirm final timeline length is `446 frames`.
- Confirm only two fades exist: CUT01 fade-in and CUT04 fade-out.
