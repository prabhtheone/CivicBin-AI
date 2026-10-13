# CivicBin AI ♻️🤖

**See the Waste. Understand the Event. Trigger Action.**

CivicBin AI is an AI-assisted civic-cleanliness project exploring how **Gemma 4 multimodal vision AI** can help interpret waste-disposal events in authorized CCTV or video footage. The core use case is not only checking whether a bin is full: it is flagging a possible **missed disposal**—when waste may miss a bin—and preparing evidence for a human reviewer.

## 🎯 The Problem

CCTV footage records what happens, but people may still need to review long recordings manually to understand a specific waste-disposal event. A bin can be far from full while litter remains on the ground. CivicBin AI explores an event-focused workflow for these situations.

## 🧠 How CivicBin AI Works

The intended workflow is:

1. **Video input:** use authorized CCTV footage or a short sample clip.
2. **Frame selection:** extract relevant frames from the disposal event.
3. **Gemma 4 vision analysis:** interpret the selected visual context.
4. **Civic Waste Investigator:** validate the evidence and classify the candidate event.
5. **Structured incident:** record the possible incident, supporting evidence, uncertainty, and suggested next step.
6. **Human review:** a person verifies the evidence before any real-world action.

Possible review outcomes include correct disposal, missed disposal/littering, bin overflow, and unclear footage requiring review. These are the intended classification categories; measured performance has not been published in this repository.

## 🛠️ Technology Direction

- **AI model:** Gemma 4 multimodal vision
- **Model runtime path:** Ollama (compatibility and exact model variant should be verified against the runnable setup)
- **Video/frame processing:** Python and OpenCV
- **Agent rules:** Civic Waste Investigator Agent Skill
- **Incident representation:** structured JSON
- **Version control:** Git and GitHub

The repository currently documents the project workflow and agent rules. The complete runnable application, exact dependency versions, model configuration, and reproducible test evidence still need to be committed before another developer can reproduce the full demo from this repository alone.

## 📂 Repository Contents

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — system workflow, design principles, and implementation status.
- [docs/GEMMA4_WORKFLOW.md](docs/GEMMA4_WORKFLOW.md) — Gemma 4 vision workflow and validation plan.
- [skills/civic-waste-investigator/SKILL.md](skills/civic-waste-investigator/SKILL.md) — agent instructions for evidence-led incident review.

## 🚧 Current Project Status

Work completed so far includes defining the missed-disposal problem, shaping the Gemma 4-based workflow, designing the Civic Waste Investigator agent rules, and preparing the project for a potential customer pitch and practical delivery.

This repository is being filled with the project artifacts available so far. It does **not** claim a verified accuracy score, a confirmed sale, a customer deployment, or city-wide production readiness. Add source code, exact runtime details, actual outputs, and test results as they become available.

## 🧪 Validation Plan

Before relying on incident flags, evaluate the system on authorized, labeled sample clips. Record the expected event, model output, supporting frames, false positives, false negatives, uncertain cases, and processing time. Do not treat illustrative examples as measured results.

## 🔐 Privacy and Human Oversight

- Process only footage the operator is authorized to use.
- Do not perform face recognition or identity profiling.
- Minimize stored footage and restrict access to evidence.
- Treat model output as a candidate observation, not a verdict.
- Require human review before any cleanup, escalation, or other action.

## 👤 Author

Created by [prabhtheone](https://github.com/prabhtheone).

---

*An AI-assisted approach to turning CCTV footage into reviewable civic intelligence.*