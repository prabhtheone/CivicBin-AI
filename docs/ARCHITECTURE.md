# CivicBin AI — Architecture Notes

This document records the intended technical direction for CivicBin AI. It is **design documentation**, not proof that every component has been implemented.

## Goal

Explore an AI-assisted workflow that can help a human reviewer identify possible waste-disposal incidents from authorized CCTV footage.

## Proposed workflow

```text
Authorized video / sample clip
          |
          v
Frame extraction (Python + OpenCV)
          |
          v
Selected frames and context
          |
          v
Gemma 4 multimodal model
          |
          v
Structured candidate incident
          |
          v
Civic Waste Investigator rules / validation
          |
          v
Evidence + confidence + uncertainty
          |
          v
Human review before action
```

## Proposed incident categories

- Correct disposal
- Missed disposal / littering
- Bin overflow
- Unclear event requiring human review

The categories must be validated against labeled examples before any performance claims are made.

## Design principles

1. **Evidence first:** an incident report should point to the frames or observations that support it.
2. **Human oversight:** AI output is a suggestion; a human reviewer makes the final decision.
3. **Uncertainty is allowed:** unclear or obstructed footage should be marked for review instead of forcing a classification.
4. **Privacy:** use only footage the project team is authorized to process; avoid face recognition and identity profiling; minimize retained footage.
5. **Measured performance:** record false positives, false negatives, uncertain cases, and processing time using a labeled test set.
6. **Keep the first demo small:** validate a single image or short clip before attempting multiple streams or deployment.

## Planned implementation areas

| Area | Intended responsibility | Status in this repository |
|---|---|---|
| Video processing | Extract representative frames from a clip | Design direction; source not yet included |
| Gemma 4 integration | Analyze selected visual input | Model named by project; exact variant/runtime details not yet documented here |
| Incident structure | Represent candidate event, evidence, confidence, and review status | To be specified alongside implementation |
| Investigator skill | Apply consistent validation and incident-handling rules | Design direction; skill file not yet included |
| Dashboard | Let a reviewer inspect candidate incidents | Not documented as implemented here |
| Evaluation | Compare predictions with labeled examples | Test results not yet included |
| Deployment | Provide a stable, controlled environment | No deployment link documented here |

## Evaluation checklist

Before describing the workflow as validated, test it on a small set of labeled clips and document:

- Expected label versus model output
- Evidence that supports or contradicts the prediction
- False-positive and false-negative cases
- Cases routed to human review
- Processing time and hardware/runtime configuration

Do not publish invented accuracy numbers or illustrative incident values as real results.

## Hardware and runtime

The exact Gemma 4 variant, inference runtime, Python version, dependency list, and hardware requirements should be recorded only after they have been verified against the working implementation. Do not assume a particular model size or command will work on every machine.

## Next steps

1. Add the actual notebook or source code used during development.
2. Record the exact model variant and runtime.
3. Add a small, permission-safe sample input and the corresponding real output.
4. Implement or document the structured incident schema.
5. Add tests and report measured results.
6. Add a demo link only after it is stable and accessible.
