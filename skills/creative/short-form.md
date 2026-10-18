# Short-Form Video Pipeline (TikTok / Reels / Shorts)

> Sources: TikTok Creator Portal, Instagram for Business blog, YouTube Shorts documentation,
> Hootsuite Social Trends Report 2025, OpusClip retention data 2025, Shortimize 35B Shorts
> analysis, PostPlanify safe zones 2026, Kreatli platform guides, TTS Vibes hook statistics

## Quick Reference Card

```
ASPECT RATIO:     9:16 vertical (1080x1920)
SAFE ZONE:        900x1400px centered (universal cross-platform)
DURATION:         15s (highest completion) | 30s (best engagement) | 60s (most flexible)
HOOK:             First 1-2 seconds — visual or text pattern interrupt
CAPTIONS:         Mandatory (85% watch muted on mobile)
TEXT SIZE:         42px+ minimum, bold sans-serif
PACING:           Visual change every 1-3 seconds
TARGET LUFS:      -14 LUFS, true peak -1 dBTP
MUSIC:            120-140 BPM for energetic, 90-110 for explainers
```

## Platform Safe Zones (1080x1920)

| Platform | Safe Zone | Top Dead | Bottom Dead | Right Dead |
|----------|-----------|----------|-------------|------------|
| TikTok | 900x1492 | 108px | 320px | 120px |
| Instagram Reels | 996x1400 | 210px | 310px | 84px |
| YouTube Shorts | 984x1500 | 120px | 300px | 96px |
| Facebook Reels | 1080x1520 | 100px | 300px | 60px |

**Universal safe zone: `x = 135..935`, `y = 175..1380` (`800x1205px` inner box)** — works across all vertical platforms without edge clipping or UI overlap.

**Bottom and right-side dead zones are critical**:
- **Bottom `540px` (`y = 1380..1920`)**: Covered by creator profile name, caption copy, audio ticker, and bottom bar.
- **Left `135px` (`x < 135`) & Right `145px` (`x > 935`)**: Covered by phone aspect-ratio edge cropping and the right-side Like/Comment/Share/Save icon stack. Never place captions or callout graphics outside `x = 135..935`, `y = 175..1380`.

## Upload Specs

```
CODEC:       H.264 High Profile, Level 4.2
BITRATE:     8-15 Mbps VBR (below 5 Mbps triggers quality downgrade)
FORMAT:      .mp4 preferred
MAX SIZE:    500 MB (desktop), 287.6 MB (iOS), 72 MB (Android)
```

## Duration Strategy

| Duration | Avg Completion Rate | Best For |
|----------|-------------------|----------|
| 0-15s | 92% | Single fact, quick tip, visual gag |
| 16-30s | 84% | One concept explained, before/after |
| 31-60s | 68% | Mini tutorial, step-by-step, story arc |
| 60-90s | 48%+ | Presenter walkthroughs, property tours, multi-scene stories |

**Platform sweet spots:**
- TikTok: 21-34 seconds for completion; 60-180s for maximum total watch time
- Reels: 15-30 seconds for viral reach; 60-90s for highest engagement
- Shorts: Bimodal — ~13 seconds OR full 60 seconds (Shortimize 35B views analysis)

**Key formula:** A 45s video with 70% completion (31.5s watch time) outperforms a 15s video with 40% completion (6s). Total watch time is what the algorithm rewards.
**Never truncate spoken sentences to hit an arbitrary 30s ceiling:** On presenter-led or walkthrough footage, cutting mid-thought or rushing natural speech ruins credibility. Let complete spoken clauses and natural acoustic silence boundaries determine the runtime (e.g., 60–85s).

## The 1-Second Hook

**70%+ of TikTok users decide to scroll or stay within 3 seconds** (average decision point: 1.7 seconds). The hook must be immediate.

### 3-Second Retention and Algorithmic Impact

| 3-Second Retention | Algorithmic Effect | View Multiplier |
|-------------------|-------------------|-----------------|
| Below 60% | Minimal promotion | 1.0x (baseline) |
| 60-70% | Average distribution | 1.6x |
| 70-85% | Optimal reach | 2.2x |
| 85%+ | Viral potential | 2.8x |

### Retention Checkpoints

| Timestamp | Target Retention |
|-----------|-----------------|
| 3 seconds | 70%+ |
| 15 seconds | 60%+ |
| 30 seconds | 50%+ |

### Hook Techniques

| Technique | Example | When to Use |
|-----------|---------|-------------|
| **Bold text on screen** | "STOP doing this..." (text appears frame 1) | Always — text hooks work even muted |
| **Pattern interrupt** | Unexpected visual, jump cut, color flash | Attention-grabbing |
| **Question** | "Why does X happen?" (text + voiceover) | Educational |
| **Result first** | Show the finished result, then explain how | Tutorial/how-to |
| **Controversy** | "Everyone gets this wrong" | Engagement bait |

### Hook Rules

1. **Frame 1 must have visual interest** — no blank intros, no logos, no "hey guys"
2. **Text appears in the first 0.5 seconds** — viewers scan text before listening
3. **Voice starts immediately** — no silent buildup
4. **Movement in frame 1** — static opening frames get scrolled past

## Pacing

| Rule | Value | Why |
|------|-------|-----|
| Visual change frequency | Every 1-3 seconds | Mobile attention span |
| Cuts per minute | 20-40 | 2-3x faster than long-form |
| Text on screen | 2-4 seconds per text block | Fast reading pace |
| No static holds | Max 3 seconds | Anything longer feels frozen |
| Speed ramp | 1.2-1.5x for setup, 1.0x for payoff | Compress boring parts |

**Impact of pacing on retention:**
- Pattern interrupts every 2-4s: **58% average retention**
- Static talking head (no interrupts): **41% average retention**
- That's a **41% relative improvement** from pacing alone

### Script Word Counts

| Duration | Word Count |
|----------|-----------|
| 15 seconds | 35-40 words |
| 30 seconds | 70-80 words |
| 60 seconds | 125-150 words |

## Text & Captions

### Mandatory Captions

**80% of short-form viewers watch without sound** (mid-2025 data). Videos with accurate captions average **12% higher retention**. Captions are not optional.

| Parameter | Value |
|-----------|-------|
| Font size | 34-42px+ at 1080p |
| Font weight | Bold / ExtraBold (800-900) |
| Font family | Sans-serif (Inter, Montserrat, Poppins) |
| Background | Contoured dark stroke (`4-6px #0E0E12`) + multi-layer dark halo shadow (avoid opaque boxes on presenter reels) |
| Position | Strictly inside `x = 135..935`, `y = 175..1380` (clear of bottom `540px` and right `145px` social UI) |
| Max chars/line | 30 |
| Max lines | 2 |
| Word-by-word highlight | Progressive pop-in (`opacity: 0` until spoken — never show grey unspoken words ahead of speech), active word scale pop (`1.14x`) + underline sweep, and 90/10 color restraint |

### On-Screen Text (Non-Caption)

- Position in the **upper safe zone (`y = 175..450`)** during B-roll or **lower-mid safe zone (`y = 1000..1350`)** when captions sit above/below
- Follow the **90/10 color restraint rule**: ~90% crisp white/ivory, ~10% single-hue surgical accent on focal numbers/keywords
- 3-5 words maximum per text block
- Animate entrance (`slam`, `swing`, `rise`, or handwriting `wipe`, keeping entrance scale overshoot `<= 1.14x` so left/right safe zones are never breached)

## Audio

| Element | Level | Notes |
|---------|-------|-------|
| Voiceover | -12 to -14 dB peak | Primary |
| Music | -22 to -26 dB | Lower than long-form — less room |
| SFX | -18 to -14 dB | Brief pops/whooshes only |
| Target LUFS | -14 LUFS | Same as long-form YouTube |
| True peak | -1 dBTP | TikTok/Instagram spec |

### Music Selection
- **Energetic content:** 120-140 BPM
- **Explainer content:** 90-110 BPM
- **Match trending audio patterns** — short-form audiences expect music-forward content
- **Music should start immediately** — no silent intro

### Voiceover Pacing
- **180-200 WPM** for short-form (faster than long-form's 150-160)
- Speak with energy and urgency
- No long pauses — dead air = scroll

## Structure Templates

### 15-Second Quick Tip
```
[0-1s]   HOOK: Bold text + voice starts immediately
[1-3s]   CONTEXT: One sentence setup
[3-12s]  CONTENT: The tip/fact/technique (show, don't tell)
[12-15s] PAYOFF: Result or CTA text overlay
```

### 30-Second Explainer
```
[0-1s]   HOOK: Pattern interrupt or question
[1-5s]   PROBLEM: Why this matters
[5-22s]  SOLUTION: Step-by-step with visual changes every 2-3s
[22-28s] RESULT: Show the outcome
[28-30s] CTA: Follow/share/comment prompt
```

### 60-Second Mini Tutorial
```
[0-2s]   HOOK: Show finished result first
[2-8s]   SETUP: "Here's how to do X in Y steps"
[8-45s]  STEPS: 3-5 steps, ~8s each, visual change per step
[45-55s] RESULT: Before/after or final demo
[55-60s] CTA + LOOP: End connects back to start for replay
```

## Applying to OpenMontage

When building short-form content:

1. **Set output resolution to 1080x1920** (9:16) in the compose stage
2. **Keep all text within 900x1400px safe zone** — centered in frame
3. **Captions are mandatory** — use `subtitle_gen` with word-by-word timing
4. **Hook in frame 1** — text overlay + voice starts immediately, no intro
5. **Visual change every 1-3 seconds** — use quick cuts, zooms, text pops
6. **Voiceover at 180-200 WPM** — faster than long-form
7. **Music starts immediately** — set `music_gen` to energetic BPM (110-140)
8. **Target 15-30 seconds** for maximum completion rate
9. **Test on phone** — view at actual mobile size before publishing
