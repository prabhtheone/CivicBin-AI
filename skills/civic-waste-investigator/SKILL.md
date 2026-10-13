---
name: civic-waste-investigator
description: Review AI-generated observations from authorized CCTV or video for possible waste-disposal incidents. Validate visible evidence, represent uncertainty, and require human review before action.
---

# Civic Waste Investigator

## Purpose

Help a human reviewer assess a candidate waste-disposal event from selected video frames analyzed by a compatible Gemma 4 vision model. This skill defines review rules; it does not itself run the model or prove that a detection occurred.

## Inputs

- Selected frames with timestamps, when available
- The model's raw description or proposed classification
- Optional clip/context metadata that does not identify a person

## Review procedure

1. Describe only what is visible in the supplied evidence.
2. Check whether the frames show a disposal attempt and its outcome. Do not infer the outcome from a person merely standing near a bin.
3. Check whether the item visibly entered the bin, missed it, remained on the ground, or whether the bin appears overflowing.
4. Check temporal context. If the item disappears between frames, do not assume it entered the bin unless the evidence supports that conclusion.
5. Link every conclusion to frame timestamps or an explicit visual observation.
6. If evidence is missing, obstructed, contradictory, or insufficient, return `UNCERTAIN` and explain why.
7. Recommend human review for every candidate incident. Never recommend punishment or identify a person.

## Allowed event labels

- `CORRECT_DISPOSAL`
- `MISSED_DISPOSAL`
- `BIN_OVERFLOW`
- `UNCERTAIN`

Use `UNCERTAIN` when no label is supported clearly enough by the available evidence.

## Output

Return a structured report with these fields:

- `event_type`: one of the allowed labels
- `summary`: concise description of the visible event
- `evidence_frames`: timestamps or frame identifiers supporting the summary
- `confidence`: optional value only when the upstream implementation provides a defined, validated confidence measure; otherwise `null`
- `uncertainty_reason`: explanation when evidence is insufficient; otherwise `null`
- `human_review_required`: `true` for candidate events
- `recommended_next_step`: neutral review or verification action

Do not fabricate timestamps, objects, confidence scores, locations, or model outputs.

## Privacy and limits

- Process only footage the operator is authorized to use.
- Do not identify people, recognize faces, infer personal attributes, or create identity profiles.
- Focus on the disposal event and surrounding waste, not personal identity.
- Treat model output as a hypothesis, not a verified fact.
- A human must verify the evidence before cleanup, escalation, or any other real-world action.
- This skill is a review specification; validate it with tests before relying on it.