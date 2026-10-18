# Edit Director - Hybrid Pipeline

## When To Use

This stage creates the layered edit logic for a source-led video with support elements. The order matters: anchor cut first, support layers second.

## Prerequisites

| Layer | Resource | Purpose |
|-------|----------|---------|
| Schema | `schemas/artifacts/edit_decisions.schema.json` | Artifact validation |
| Prior artifacts | `state.artifacts["assets"]["asset_manifest"]`, `state.artifacts["scene_plan"]["scene_plan"]`, `state.artifacts["script"]["script"]` | Source/support assets and timeline intent |
| Playbook | Active style playbook | Typography and motion consistency |

## Process

### 1. Lock The Anchor Cut First

The viewer should understand the story before support overlays are added. If the anchor cut is weak, support layers will not save it.

### 2. Add Support In Priority Order

Typical order:

1. subtitles,
2. speaker or context labels,
3. diagrams or stat cards,
4. optional inserts,
5. CTA elements.

### 3. Protect Readability & Safe Zones

Never stack too many support layers in one moment. If subtitles, labels, charts, and overlays collide, simplify.
For 9:16 vertical social reels (`1080x1920`):
- **Keep all captions and callouts strictly within `x = 135..935` and `y = 175..1380`**: Never place text in the bottom `540px` (`y > 1380`, blocked by profile/caption/audio UI) or outer horizontal edges (`x < 135` edge crop, `x > 935` right-side Like/Comment/Share icon stack).
- **Progressive word-by-word active captions (no grey pre-text)**: Hide unspoken future words (`opacity: 0` in their flex layout slots) so words pop in cleanly as spoken without grey pre-text or horizontal jitter.
- **90/10 color restraint**: Keep ~90% of text in crisp white/ivory over contoured dark strokes + halo shadows (no opaque pill/box backgrounds), reserving ~10% single-hue accent color strictly for focal numbers and active keywords.

### 4. Presenter + B-Roll Hybrid Sequencing Rules

- **Prioritize complete spoken thoughts over rigid 30s caps**: Never clip words or syllables to force a 30s duration. Verify every speech cut against a `10ms–50ms` RMS waveform envelope (`-35 dB` to `-50 dB` silence valley) with `40–100ms` audio micro-fades.
- **Cover mid-take audio excisions with B-roll bridges**: When removing a clause or sentence from the middle of an on-camera presenter clip, switch the video track to 4K B-roll at the audio splice point so the cut is invisible (zero jump-cut on the speaker).
- **Re-inventory source media on user deletions**: If the user deletes unwanted clips from the source folder, re-scan the directory before re-sequencing so zero deleted files are referenced.

### 5. Use Metadata For Layering Logic

Recommended metadata keys:

- `anchor_cut_notes`
- `layer_order`
- `overlay_windows`
- `variant_edit_rules`

### 6. Quality Gate

- the anchor cut works on its own with zero clipped syllables,
- support layers clarify instead of distract and obey the 90/10 color restraint rule,
- all text and callouts stay inside `x = 135..935`, `y = 175..1380` on 9:16 vertical outputs,
- variants remain consistent.

## Common Pitfalls

- Trying to fix a weak cut with extra graphics.
- Cutting speech on raw Whisper timestamps without checking the acoustic RMS silence valley.
- Placing captions in the bottom `540px` or right `145px` of a 9:16 reel where social platform UI blocks them.
- Pre-rendering unspoken caption words in grey text instead of keeping them at `opacity: 0` until spoken.
- Letting support layers compete with the source or overusing gaudy accent colors.
