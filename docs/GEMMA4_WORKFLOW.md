# Gemma 4 Vision Workflow

This document captures the intended CivicBin AI workflow around Gemma 4. It is technical project documentation, not a benchmark report.

## Core use case

Flag a possible missed waste-disposal event in authorized CCTV footage, even when the bin is not full. The system should help a human reviewer understand what happened, not identify or punish a person.

## Processing stages

1. **Input:** an authorized short clip or sample video.
2. **Frame extraction:** use Python/OpenCV to select frames around a possible disposal attempt.
3. **Multimodal analysis:** pass the selected visual context to a compatible Gemma 4 vision model through the chosen runtime (Ollama is the current runtime path to verify).
4. **Event interpretation:** ask the model to distinguish what is visible from what is uncertain. A single frame may not prove whether waste entered the bin.
5. **Agent validation:** apply the Civic Waste Investigator rules in `../skills/civic-waste-investigator/SKILL.md`.
6. **Human review:** show the proposed classification and evidence frames to a reviewer before any action.

## Candidate outcomes

- `CORRECT_DISPOSAL` — evidence supports that waste entered the bin.
- `MISSED_DISPOSAL` — evidence supports that waste missed the bin or was left outside.
- `BIN_OVERFLOW` — visible waste appears to exceed the bin's capacity.
- `UNCERTAIN` — evidence is insufficient, contradictory, or obstructed.

These are proposed labels. Their definitions and model behaviour must be tested against labeled examples before they are treated as reliable.

## Suggested output format

```json
{
  "event_type": "UNCERTAIN",
  "summary": "Insufficient visual evidence to determine the disposal outcome.",
  "evidence_frames": [],
  "confidence": null,
  "uncertainty_reason": "The relevant disposal outcome is not clearly visible.",
  "human_review_required": true
}
```

This is an illustrative schema example, not a recorded model result. Confidence should only be populated if the implementation defines and validates what that number means; model-generated confidence is not automatically calibrated.

## Runtime details to record

- Exact Gemma 4 model identifier and variant
- Ollama/runtime version and model settings
- Python version and package versions
- GPU/CPU configuration and memory use
- Actual input clip, selected frame timestamps, and raw model response
- Processing latency and failure cases

## Validation plan

Use authorized sample clips labeled by human reviewers. Compare predicted labels with ground truth, preserve evidence timestamps, and document false positives, false negatives, uncertain cases, and processing time. Do not claim accuracy or production readiness until measured.

## Privacy and safety

- Use only video the operator is authorized to process.
- Do not perform face recognition or identity profiling.
- Minimize retained footage and restrict access.
- Human review is mandatory before action.