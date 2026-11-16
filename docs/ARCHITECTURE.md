# Architecture

This document describes the intended design. It does not describe a completed or validated implementation.

## Goal

Help a human reviewer find and assess possible waste-disposal incidents in authorized video footage.

## Proposed data flow

```text
Authorized video
      |
      v
Frame selection (planned: Python / OpenCV)
      |
      v
Selected frames and timestamps
      |
      v
Vision model (Gemma 4 is the documented direction)
      |
      v
Candidate event description
      |
      v
Civic Waste Investigator review rules
      |
      v
Evidence, uncertainty, and suggested review step
      |
      v
Human decision
```

## Components and status

| Component | Intended responsibility | Status in this repository |
|---|---|---|
| Video processing | Select frames from a short clip | Planned; no source code included |
| Vision model | Describe the visual event | Gemma 4 is the documented direction; integration is not included |
| Incident format | Store event label, evidence, and uncertainty | Example format is in [GEMMA4_WORKFLOW.md](GEMMA4_WORKFLOW.md); no implementation or formal schema |
| Investigator rules | Check whether the evidence supports a candidate label | Review instructions are documented in [SKILL.md](../skills/civic-waste-investigator/SKILL.md) |
| Reviewer interface | Let a person inspect evidence and decide what to do | Not implemented or documented as a working interface |
| Evaluation | Compare outputs with human-labeled events | No dataset or test results included |
| Deployment | Run the workflow in a controlled environment | No deployment configuration or live demo included |

## Design constraints

1. **Evidence first:** every proposed label should point to the frames or timestamps that support it.
2. **Do not guess:** if the event outcome is not visible, use `UNCERTAIN`.
3. **Human decision:** AI output is a candidate observation, not a verdict.
4. **Privacy:** use only authorized footage and avoid identity recognition.
5. **Measured evaluation:** report false positives, false negatives, uncertain cases, and processing time.

## Implementation work still required

1. Add the actual video-processing and model-integration code.
2. Record a tested model identifier, runtime version, dependency list, and hardware requirements.
3. Define and validate the incident data format.
4. Add permission-safe sample inputs and reproducible expected outputs.
5. Add tests for frame selection, output parsing, and uncertain cases.
6. Evaluate against human-labeled clips and publish the test conditions.
7. Add a reviewer interface only after the core workflow is reproducible.
