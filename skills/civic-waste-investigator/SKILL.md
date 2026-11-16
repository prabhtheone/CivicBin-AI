---
name: civic-waste-investigator
description: Review observations from authorized video for possible waste-disposal incidents. Check visible evidence, record uncertainty, and require human review.
---

# Civic Waste Investigator

## Purpose

Help a human reviewer assess a candidate waste-disposal event using selected video frames and an upstream model description. These instructions do not run a model or establish that an incident occurred.

## Inputs

- Selected frames and timestamps, when available
- The model's raw description or proposed label
- Relevant clip context that does not identify a person

## Review rules

1. Describe only what is visible in the supplied frames.
2. Do not infer a disposal event from a person merely standing near a bin.
3. Check whether the item visibly entered the bin, missed it, remained on the ground, or whether the bin appears full or overflowing.
4. Consider the sequence of frames. If an item disappears between frames, do not assume it entered the bin.
5. Link each conclusion to a timestamp or a specific visual observation.
6. Return `UNCERTAIN` when the evidence is missing, obstructed, contradictory, or insufficient.
7. Require human review for every candidate incident. Do not recommend punishment or identify a person.

## Allowed labels

- `CORRECT_DISPOSAL`
- `MISSED_DISPOSAL`
- `BIN_OVERFLOW`
- `UNCERTAIN`

Use `UNCERTAIN` rather than guessing.

## Report fields

Return a structured report with:

- `event_type`: one of the allowed labels
- `summary`: a concise description of the visible event
- `evidence_frames`: timestamps or frame identifiers
- `confidence`: a value only when the upstream system defines and validates its meaning; otherwise `null`
- `uncertainty_reason`: why the evidence is insufficient, or `null`
- `human_review_required`: `true`
- `recommended_next_step`: a neutral review or verification action

Do not invent timestamps, objects, confidence values, locations, or model outputs.

## Privacy and limits

- Process only footage the operator is authorized to use.
- Do not identify people, recognize faces, infer personal attributes, or create identity profiles.
- Focus on the disposal event and surrounding waste, not personal identity.
- Treat model output as a hypothesis, not a verified fact.
- A human must verify the evidence before cleanup, escalation, or any other real-world action.
