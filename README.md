# CivicBin AI

CivicBin AI explores an evidence-led workflow for reviewing possible waste-disposal incidents in authorized CCTV or sample video. The initial use case is a possible missed disposal: waste that may have missed a bin and remained on the ground.

The system is intended to prepare evidence for a human reviewer. It is not intended to identify people or make enforcement decisions.

## Intended workflow

1. Load an authorized short video clip.
2. Select frames around a possible disposal event.
3. Analyze the selected frames with a compatible multimodal vision model.
4. Check the model's description against the Civic Waste Investigator review rules.
5. Prepare a structured candidate incident with evidence and uncertainty.
6. Require a human to review the evidence before any action.

## Candidate outcomes

- `CORRECT_DISPOSAL` — the available evidence supports that the waste entered the bin.
- `MISSED_DISPOSAL` — the evidence supports that waste missed the bin or was left outside.
- `BIN_OVERFLOW` — waste appears to exceed the bin's capacity.
- `UNCERTAIN` — the frames are unclear, obstructed, or insufficient.

These are proposed labels, not measured model capabilities. A single frame may not show the full disposal event.

## Project status

**This GitHub repository is currently documentation-only. It is not a runnable application.**

The repository contains the workflow design, architecture notes, and the Civic Waste Investigator review rules. It does not currently contain the video-processing source, model integration, dependency definitions, sample footage, model weights, a dashboard, or an executable test suite.

The project documents Gemma 4 as its intended vision-model direction and Python/OpenCV as the planned video-processing tools. The exact model variant, runtime, dependencies, hardware requirements, and working inference command have not been verified in this repository.

No accuracy score, deployment, customer adoption, or production readiness is claimed here.

## Repository layout

- [Architecture](docs/ARCHITECTURE.md) — components, boundaries, and implementation status.
- [Gemma 4 workflow](docs/GEMMA4_WORKFLOW.md) — proposed model workflow, output example, and evaluation plan.
- [Civic Waste Investigator skill](skills/civic-waste-investigator/SKILL.md) — evidence-review rules for a human-facing agent.

## Documentation check

Run the repository's documentation checks with Python 3:

```sh
python3 tests/check_docs.py
```

The check validates local Markdown links, fenced code blocks, JSON examples, and the Investigator skill front matter. It does not test video processing, model inference, or detection quality.

## Validation plan

Before relying on incident flags, evaluate the implementation on authorized clips labeled by human reviewers. Record the expected outcome, model output, evidence timestamps, false positives, false negatives, uncertain cases, and processing time.

Do not present illustrative examples as real model outputs or measured results. Publish performance numbers only with the dataset, evaluation method, and test conditions that produced them.

## Privacy and human review

- Process only footage the operator is authorized to use.
- Do not perform face recognition, identity profiling, or personal-attribute inference.
- Retain only the footage and frames needed for review, and restrict access to them.
- Treat model output as a hypothesis, not a verified event.
- Require a human to verify evidence before cleanup, escalation, or any other real-world action.

## Current limitations

The documented workflow has not been validated by a runnable implementation in this repository. Model output may be incomplete or wrong, and video frames may not capture the full event. Human review is required.

## Author

Created by [prabhtheone](https://github.com/prabhtheone).
