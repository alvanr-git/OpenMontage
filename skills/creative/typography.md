# Typography for Video Production

> Sources: School of Motion typography guides, legibility.info video text rules, Wave.video font
> pairing research, EBU/SMPTE broadcast standards, Netflix subtitle spec, BBC subtitle guidelines,
> WCAG 2.1 contrast requirements, Easings.net, postplanify.com safe zone data (2026)

## Quick Reference Card

```
TITLE SIZE:       60-90px at 1080p  |  120-180px at 4K
BODY SIZE:        40-60px at 1080p  |  80-120px at 4K
SUBTITLE SIZE:    42px+ at 1080p    |  3-5% of video height
MAX CHARS/LINE:   32-42 (subtitles) |  30 (overlays)
MAX LINES:        2 (subtitles)     |  3 (overlays)
READING SPEED:    21 chars/sec      |  160-200 WPM
TITLE SAFE:       80% of frame (192px margin at 1080p)
ACTION SAFE:      90% of frame (96px margin at 1080p)
FONT FAMILIES:    1-2 per video maximum
CONTRAST:         4.5:1 minimum, 7:1 optimal
FADE DURATION:    0.3s opacity  |  0.5-1.0s slide/scale
```

## Font Selection

### Recommended Video Fonts

| Category | Fonts | Use For |
|----------|-------|---------|
| **Body / Captions** | Inter, Open Sans, Roboto, Source Sans Pro, Lato, DM Sans | All body text, subtitles, captions |
| **Headlines** | Montserrat Bold, Bebas Neue, Oswald Bold, Poppins Bold | Titles, section headers, key stats |
| **Editorial** | Playfair Display, Roboto Slab | Luxury, cinematic, documentary |
| **System Safe** | Helvetica Neue, Arial, Avenir Next | When custom fonts unavailable |

### Font Pairing Rules

- Limit to **1-2 font families** per video — more creates visual noise
- Pair a **display/bold heading** font with a **neutral body** font
- Size difference between title and body: at least **50% larger**
- **Sans-serif** for motion graphics and captions (holds up in motion)
- **Serif** only for cinematic title cards and editorial content
- **Script/decorative** fonts: hero titles only, never body, never in motion

### Proven Pairings

| Heading | Body | Style |
|---------|------|-------|
| Bebas Neue | Open Sans | High-impact, social ads |
| Montserrat Bold | Lato | Clean modern |
| Oswald Bold | Raleway | Strong contrast |
| Playfair Display | Inter | Editorial |
| Poppins Bold | Poppins Light | Single-family hierarchy |

## Text Sizing

### Minimum Readable Sizes

| Element | 1080p (px) | 4K (px) | Notes |
|---------|-----------|---------|-------|
| Title / Hero text | 60-90 | 120-180 | Must be readable as thumbnail |
| Body text | 40-60 | 80-120 | Absolute minimum for readability |
| Subtitles | 42+ | 84+ | Accessibility requirement |
| Lower third name | 48-60 | 96-120 | Bold weight |
| Lower third role | 36-44 | 72-88 | Light/regular weight |
| Thumbnail text | — | — | Must read at 120-160px wide display |

## Safe Zones

### Broadcast Standard

| Zone | Coverage | Margin at 1080p | Purpose |
|------|----------|----------------|---------|
| **Title Safe** | 80% of frame | 192px H, 108px V | All text must stay within |
| **Action Safe** | 90% of frame | 96px H, 54px V | All important content |

At 1920x1080: Title Safe = inner **1536x864px**
At 3840x2160: Title Safe = inner **3072x1728px**

### Platform-Specific Safe Zones (Vertical 1080x1920)

| Platform | Safe Zone | Top Dead | Bottom Dead | Right Dead |
|----------|-----------|----------|-------------|------------|
| **TikTok** | 900x1492 | 108px | 320px | 120px |
| **Instagram Reels** | 996x1400 | 210px | 310px | 84px |
| **YouTube Shorts** | 984x1500 | 120px | 300px | 96px |
| **Facebook Reels** | 1080x1520 | 100px | 300px | 60px |
| **Instagram Stories** | 1080x1620 | 100px | 200px | — |

**Universal cross-platform safe zone: 900x1400px centered** — works on all platforms.

## Text Animation Timing

### Duration on Screen

- Reading speed: **13 characters per second** minimum dwell time
- 30-character line: minimum **2.3 seconds**
- General rule: **3 seconds per 63 characters**
- Title cards: **3-6 seconds**
- After animation completes, hold motionless for **1 second per 13 characters**

### Animation Durations

| Animation Type | Duration | Use Case |
|---------------|----------|----------|
| Fade in/out | 0.3-0.5s | Subtle, universal |
| Slide / scale entrance | 0.5-1.0s | Standard motion graphics |
| Kinetic text entrance | 1.0-2.0s | Bold, energetic |
| Lower third entrance | 1.0-2.0s | Speaker identification |
| Lower third exit | 0.5-1.0s | Quick departure |

### Easing Curves

| Easing | Cubic Bezier | Use For |
|--------|-------------|---------|
| **easeOutCubic** | `(0.33, 1, 0.68, 1)` | Text entrances (decelerates into place) — **default choice** |
| **easeOutQuart** | `(0.25, 1, 0.5, 1)` | Snappier entrance, kinetic type |
| **easeInOutQuad** | `(0.45, 0, 0.55, 1)` | Smooth position transitions |
| **easeInOutCubic** | `(0.65, 0, 0.35, 1)` | Scale and opacity changes |
| **easeInCubic** | `(0.32, 0, 0.67, 0)` | Exits (accelerates out) |

**Never use linear easing** for text animations — it feels robotic.

### Reveal Techniques

| Technique | Feel | Best For |
|-----------|------|----------|
| Mask reveal | Cinematic | Title cards, premium content |
| Scale pop | Energetic | Social media, short-form |
| Character stagger | Natural flow | Kinetic typography |
| Word-by-word sync | Engaging | Talking-head captions, TikTok |
| Fade | Subtle | Professional, corporate |

## Subtitle & Caption Typography

### Specifications

| Parameter | Value | Source |
|-----------|-------|--------|
| Font size | 42px+ at 1080p | Accessibility standard |
| Max characters per line | 32-42 | Platform dependent (see below) |
| Max lines | 2 per block | Universal standard |
| Line spacing | 1.3x | Readability standard |
| Background | Semi-transparent black, 70-80% opacity | Contrast requirement |
| Alternative style | White text + 2-4px dark stroke | No-box style |
| Minimum contrast | 4.5:1 (white on black = 21:1) | WCAG AA |
| Bottom margin | 60px from edge minimum | Mobile gesture clearance |
| Within frame width | 90% maximum | Title safe compliance |

### Character Limits by Platform

| Platform | Max Chars/Line |
|----------|---------------|
| YouTube | 42 |
| Netflix | 42 |
| BBC | 37 |
| TV broadcast | 37-42 |
| Cinema | 40-45 |

### Caption Timing

| Parameter | Value |
|-----------|-------|
| Minimum duration | 1 second |
| Maximum duration | 6-7 seconds |
| Reading speed | 21 characters/second |
| Fade-in transition | 0.3 seconds |
| Gap between captions | 2 frames |
| Sync tolerance | 3 frames of audio |

### Reading Speed by Platform

| Platform | WPM |
|----------|-----|
| TikTok / Instagram Reels | 180-200 |
| YouTube | 160-180 |
| LinkedIn | 140-160 |
| Educational content | 120-140 |

## Lower Thirds

### Standard Specs (1080p)

- Overlay region: **1920x360px** (bottom third)
- Sans-serif fonts (Helvetica, Open Sans, Roboto)
- White text with drop shadow or semi-transparent background bar
- Name: bold, larger weight
- Role/subtitle: lighter weight, smaller

### Timing

| Phase | Duration |
|-------|----------|
| Entrance animation | 1-2 seconds |
| Display | 3-6 seconds |
| Exit animation | 0.5-1 second |

## Contrast & Readability

### WCAG Requirements

| Element | Min Ratio | Standard |
|---------|----------|----------|
| Body text | 4.5:1 | WCAG AA |
| Large text (>18pt) | 3:1 | WCAG AA |
| Enhanced body | 7:1 | WCAG AAA |
| UI components | 3:1 | WCAG 2.1 |

### Text-Over-Video Techniques

1. **Contoured dark stroke + multi-layer halo shadow** — `4-6px` deep charcoal stroke (`#0E0E12`, `paintOrder: "stroke fill"`) plus multi-layer dark drop/halo shadows (preferred for presenter & property reels; avoids clunky opaque boxes covering footage)
2. **Semi-transparent box** — 70-80% black opacity behind text (use only when requested for broadcast/news style)
3. **Text stroke** — 2-4px dark outline around light text
4. **Darkened region** — subtle gradient vignette behind text area
5. **Full-screen overlay** — 30-50% dark overlay for text-heavy screens

## 9:16 Social Reel Caption & Kinetic Callout Rules

When authoring vertical (`1080x1920`) presenter, real estate, or social marketing reels:

1. **Strict Horizontal & Vertical Safe Box (`x = 135..935`, `y = 175..1380`)**:
   - **Bottom `540px` (`y = 1380..1920`) is off-limits**: Creator handle, caption description, audio ticker, and bottom navigation cover this zone across Instagram Reels, TikTok, and YouTube Shorts.
   - **Left `135px` (`x < 135`) & Right `145px` (`x > 935`) are off-limits**: Narrow phone aspect-ratio cropping clips the outer edges, and the right-hand Like/Comment/Share/Bookmark icon stack occupies `x = 935..1080` in the lower-mid frame.
   - When pre-rendering 3D/RGBA text plates, programmatically verify every PNG with `PIL.Image.getbbox()` so `left >= 135` and `1080 - right >= 140`.
2. **The 90/10 Color Restraint Rule**:
   - Keep **~90%** of on-screen text in crisp white (`#FFFFFF`) and warm ivory (`#F5F2EB`) over deep charcoal (`#0E0E12`) contoured strokes.
   - Reserve **~10%** single-hue accent color (e.g., Sunset Coral `#FF6E5A`) strictly for focal numbers, key metrics, and active keyword highlights — never rainbow-color every line.
3. **Progressive Word Pop-In (No Grey Unspoken Pre-Text)**:
   - In word-synced active caption blocks, **do not display upcoming unspoken words in dimmed/grey text** (`opacity: 0.4–0.5`); over dark strokes, semi-transparent text looks muddy and distracting.
   - Instead, keep unspoken words at `opacity: 0` inside their flex layout slots (preventing horizontal layout jitter as words appear) and pop each word in (`opacity: 0 -> 1` over 2 frames, spring `scale(0.86 -> 1.14 -> 1.0)`, `translateY(8px -> -6px -> 0)`, active underline `scaleX`) at the exact word onset (`curSec >= word.start`).
4. **Cap Kinetic Entrance Scale Overshoot (`<= 1.14x`)**:
   - For `slam`, `pulse`, and `swing` entrances on wide hero plates, cap initial spring scale at `1.12x–1.14x` (rather than `1.35x+`) so the plate never breaches the left/right safe zones during the first 3 frames.

## Applying to OpenMontage

When generating text for video in the compose/asset stages:

1. **Font selection** — use the recommended video fonts above; prefer Inter or Open Sans for body, Montserrat Bold for titles
2. **Size check** — never go below 40px at 1080p for any text element (34-38px acceptable for contoured-stroke multi-word active caption blocks within `x = 135..935`)
3. **Safe zones** — all text within 80% title-safe area; for 9:16 vertical short-form, enforce `x = 135..935` and `y = 175..1380`
4. **Subtitle styling** — prefer contoured charcoal stroke + halo shadows (no background pills/boxes) with progressive word pop-in (`opacity: 0` until spoken)
5. **Animation** — use easeOutCubic or physics springs for entrances, hold text for at least 1 second per 13 characters after animation
6. **Contrast** — verify 4.5:1 minimum on a representative graded frame; follow the 90/10 color restraint rule
7. **Platform targeting** — check the platform safe zone table above and adjust text placement accordingly
8. **Remotion rendering** — all font families must be loaded via `@font-face` (`staticFile("fonts/...")`) or `@remotion/google-fonts`; verify fonts render in headless Chromium
