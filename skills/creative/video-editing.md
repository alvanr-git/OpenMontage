# Video Editing Skill

## When to Use

Apply this skill when making editorial decisions for talking-head content:
where to cut, what to remove, how to pace, and how to structure the final edit.

## Tools

| Tool | Role |
|------|------|
| `transcriber` | Analyze speech for filler words, dead air, false starts |
| `video_trimmer` | Execute cuts and speed adjustments |
| `frame_sampler` | Sample frames to evaluate visual quality at potential cut points |
| `video_compose` | Assemble the final edit |

## Editing Principles for Talking Heads

### What to Cut

1. **Filler words:** "um", "uh", "like", "you know" — cut at word boundaries using word timestamps.
2. **False starts:** When the speaker restarts a sentence, keep only the final take.
3. **Dead air:** Silence longer than 1.5 seconds should be trimmed to ~0.5 seconds.
4. **Off-topic tangents:** If the speaker wanders, cut to the next relevant segment.
5. **Repeated points:** Keep the best delivery, remove redundant takes.

### What NOT to Cut

- **Breath pauses:** Natural 0.3-0.8 second pauses between sentences. These sound natural.
- **Emphasis pauses:** Intentional pauses for dramatic effect.
- **Reactions and transitions:** Verbal bridges like "So..." or "Now..." that provide flow.

### Cut Technique

- **J-cut:** Audio from the next segment starts ~0.5s before the visual cut. Makes transitions feel smooth.
- **L-cut:** Audio from the current segment continues ~0.5s after the visual cut. Maintains continuity.
- **Hard cut:** Instant transition. Use at major topic changes.
- **B-roll visual bridge over mid-take removals:** When excising a sentence from the middle of a continuous on-camera walk-and-talk clip (e.g., cutting `9.60s..14.55s`), switch the video track to 4K B-roll right at the audio splice point (`9.60s`) so the cut is 100% invisible (zero facial jump-cut).

### Sample-Accurate Speech Trimming (RMS Silence Verification)

1. **Never rely on coarse Whisper word-end timestamps alone:** Whisper word boundaries can lead or lag trailing consonants (`s`, `t`, `d`, `k`) by `80–250ms`. Cutting directly on a raw Whisper timestamp frequently clips the final syllable.
2. **Inspect the 10ms–50ms RMS dB envelope around every cut point:** Locate the true acoustic silence valley (`-35 dB` to `-50 dB`) between phrases before setting `trim` / `atrim` timestamps, and apply `40–100ms` audio micro-fades (`afade=t=in:st=0:d=0.04`, `afade=t=out:st=...:d=0.08`) with dynamic normalization (`highpass=f=80,acompressor,alimiter`) so transitions never click or clip.
3. **Never force an arbitrary 30s ceiling that truncates sentences:** Let complete spoken thoughts dictate scene length.
4. **Live source-media re-inventory:** Whenever a user deletes unwanted source clips from their media folder or requests timeline re-sequencing, re-scan the directory first and verify zero deleted filenames remain referenced in any asset preparation script or manifest.

### Pacing

- **Short-form (< 90s):** High energy, visual change every 2–4s via B-roll cutaways and kinetic callouts, while preserving 100% of spoken syllables at natural phrase boundaries.
- **Medium-form (1-10 min):** Balanced. Keep natural pauses for breathing room.
- **Long-form (> 10 min):** Let scenes breathe. Only cut obvious problems.

## Edit Decision Structure

The `edit_decisions` artifact should include:

- **cuts:** Ordered list of segments to keep (source, in/out points, speed)
- **overlays:** Timed overlay placements (images, diagrams, lower thirds)
- **subtitles:** Subtitle configuration (enabled, style, source file)
- **music:** Background music settings (asset, volume, ducking, fades)
- **transitions:** Transition type and timing between cuts

## Quality Checklist

- [ ] No visible jump cuts (mid-take audio removals covered by B-roll visual bridges)
- [ ] Audio doesn't pop, click, or clip trailing consonants at cut points (verified via 10ms–50ms RMS envelope)
- [ ] Pacing matches the content energy and target platform without truncating sentences
- [ ] Speaker's face is never covered by overlays, and all text stays inside platform safe zones
- [ ] All cuts land inside verified acoustic silence valleys between words
- [ ] Zero deleted or excluded source clips are referenced in the build
