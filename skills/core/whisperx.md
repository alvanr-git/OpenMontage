# WhisperX / Transcription Skill

## When to Use

Use the `transcriber` tool whenever you need to convert speech to text from
audio or video files. This is the entry point for all transcript-dependent
workflows: subtitle generation, edit decisions based on spoken content, and
scene analysis from dialogue.

## Tool

| Tool | Capability |
|------|-----------|
| `transcriber` | Speech-to-text with word timestamps, language detection, optional diarization |

## How It Works

1. **Model loading:** faster-whisper loads the specified model size (tiny through large-v3). Defaults to `base` for speed. Use `large-v3` for production quality.
2. **Transcription:** VAD filter removes silence. Word-level timestamps are always enabled.
3. **Diarization (optional):** WhisperX alignment + pyannote speaker diarization assigns speaker labels. Requires `HF_TOKEN` environment variable.

## Model Size Guide

| Model | RAM | Speed (CPU) | Quality | When to Use |
|-------|-----|-------------|---------|-------------|
| `tiny` | ~1 GB | ~10x real-time | Low | Quick drafts, iteration |
| `base` | ~1 GB | ~5x real-time | Good | Default for development |
| `small` | ~2 GB | ~3x real-time | Better | Short content |
| `medium` | ~5 GB | ~1.5x real-time | High | Important content |
| `large-v3` | ~10 GB | ~0.5x real-time | Best | Final production |

## Key Patterns

### Choosing When to Diarize

- **Single speaker (talking head):** Skip diarization — it adds latency with no benefit.
- **Multiple speakers (interview, podcast):** Enable diarization to label who said what.
- **Diarization requires** `whisperx` and `HF_TOKEN`. If unavailable, the tool proceeds without speaker labels.

### Word Timestamps for Subtitles

The transcriber produces word-level timestamps with confidence scores. The `subtitle_gen` tool consumes these directly:

```
word_timestamps: [
  {"word": "Hello", "start": 0.5, "end": 0.8, "probability": 0.95},
  {"word": "world", "start": 0.9, "end": 1.2, "probability": 0.92},
  ...
]
```

### Language Detection

- Pass `language: null` to auto-detect only on clean studio audio.
- **Always pass an explicit ISO 639-1 code (`language="en"`, `es`, `ja`, etc.) on outdoor/street presenter footage:** Broadband traffic or crowd noise in the opening seconds frequently causes Whisper's language detector to misclassify English speech as Malay/Indonesian (`ms`/`id`) or another language, corrupting the entire transcript.

### PyAV `metadata_errors` Compatibility Workaround

When calling `faster_whisper` directly in Python on environments with newer PyAV builds where `av.open(..., metadata_errors="ignore")` raises `TypeError: open() got an unexpected keyword argument 'metadata_errors'`, decode the audio stream to raw `16kHz` mono PCM via `ffmpeg` and pass the `np.float32` array directly to `model.transcribe()`:

```python
raw = subprocess.check_output(
    ["ffmpeg", "-v", "error", "-i", src_path, "-vn", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"]
)
audio = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
segments, info = model.transcribe(audio, language="en", word_timestamps=True)
```

## Quality Checklist

- [ ] Transcript text is accurate (spot-check 3-5 segments)
- [ ] Word timestamps align with actual speech when played back (verify cut points against 10ms–50ms RMS envelope before trimming)
- [ ] No missing segments or large gaps in the transcript
- [ ] Explicit `language` code passed for outdoor/noisy recordings
- [ ] Speaker labels are correct (if diarization was used)
