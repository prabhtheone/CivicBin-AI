# Gemma 4 vision workflow

This is a proposed workflow for the CivicBin AI vision-model component. It is a design note, not an implemented integration or benchmark.

## Use case

Review a possible missed waste-disposal event in authorized video footage. The system should describe the visible evidence and uncertainty. It should not identify or profile people.

## Processing steps

1. **Input:** provide a short video clip that the operator is authorized to process.
2. **Frame selection:** use the planned Python/OpenCV stage to extract frames around the event.
3. **Vision analysis:** send selected frames and relevant context to a compatible Gemma 4 vision model. The model runtime and exact model variant still need to be selected and tested.
4. **Evidence check:** separate what is directly visible from what is inferred. A single frame may not show whether an item entered the bin.
5. **Review rules:** apply the [Civic Waste Investigator skill](../skills/civic-waste-investigator/SKILL.md).
6. **Human review:** show the proposed outcome and supporting frames to a person before any action.

## Proposed event labels

- `CORRECT_DISPOSAL`
- `MISSED_DISPOSAL`
- `BIN_OVERFLOW`
- `UNCERTAIN`

Use `UNCERTAIN` when the selected frames do not clearly support one of the other labels. The label definitions and model behaviour must be checked against human-labeled examples.

## Example output shape

```json
{
  "event_type": "UNCERTAIN",
  "summary": "The available frames do not show the disposal outcome clearly.",
  "evidence_frames": [],
  "confidence": null,
  "uncertainty_reason": "The relevant moment is not visible in the selected frames.",
  "human_review_required": true
}
```

This is an illustrative example, not an output recorded from a model run. Do not fill in a confidence value unless the implementation defines what it measures and validates that measure. A model-generated confidence value is not automatically calibrated.

## Details to record when the integration exists

- Exact model identifier and variant
- Runtime and version, including the inference settings
- Python and package versions
- Hardware and memory requirements
- Input clip identifier, frame timestamps, and selected frame references
- Raw model response and parsed result
- Processing time, failures, and retry behaviour

## Evaluation

Use authorized video clips labeled by human reviewers. For each clip, record the expected label, predicted label, evidence timestamps, false positives, false negatives, uncertain cases, and processing time.

Do not claim accuracy or production readiness until results have been measured and the evaluation method is documented.

## Privacy

- Process only footage the operator is authorized to use.
- Do not perform face recognition or identity profiling.
- Minimize stored footage and restrict access to evidence.
- Treat model output as a hypothesis.
- Require human review before action.
