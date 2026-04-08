# PMF Pipeline Overview — transition map

State machine for the `pmf` skill. Each stage reads the artifacts of the previous stages and writes its own. The project folder *is* the state machine.

## Base flow (happy path)

```
Stage 0 (Setup)
   ↓ creates 00_setup.md
Stage 1 (Hypothesis)
   ↓ creates narrative-v1.md
Stage 2 (Market Research)
   ↓ creates market-research.md
Stage 3 (Synthesis)
   ↓ creates risk-prioritization.md, narrative-v2.md
Stage 4 (Validate / DVF)
   ↓ creates assumptions-map.md, experiment-brief.md
Stage 5 (Interview Prep)
   ↓ creates interview-guide.md
Stage 6 [Field — outside the skill]
   ↓ user fills interviews/notes/*.md
Stage 7 (Interview Synthesis)
   ↓ creates interview-synthesis.md, narrative-v3.md
Stage 8 [MVP Launch — outside the skill]
   ↓ user launches the MVP
Stage 9 (Metrics)
   ↓ creates metrics-dashboard.md
Stage 10 (Iterate)
   ↓ creates iteration-changelog.md → return to the appropriate stage
```

## Rules for determining the current stage

The skill checks files in the project folder in order from later stages to earlier ones. The first match = current stage.

| File found | Current stage |
|-------------|----------------|
| `iteration-changelog.md` (most recent) | Stage 10 — iteration (return to the stage indicated in the changelog) |
| `metrics-dashboard.md` | Stage 9 done |
| `narrative-v3.md` + `interview-synthesis.md` | Stage 7 done → waiting for Stage 8 |
| ≥1 file in `interviews/notes/` | Stage 6 (in progress or complete), ready for Stage 7 |
| `interview-guide.md` | Stage 5 done → waiting for Stage 6 |
| `assumptions-map.md` | Stage 4 done, ready for Stage 5 |
| `narrative-v2.md` + `risk-prioritization.md` | Stage 3 done, ready for Stage 4 |
| `market-research.md` | Stage 2 done, ready for Stage 3 |
| `narrative-v1.md` | Stage 1 done, ready for Stage 2 |
| `00_setup.md` | Stage 0 done, ready for Stage 1 |
| Folder empty | Stage 0 |

## Possible non-linear transitions

PMF does not always go in a straight line. The skill must support back-tracking and loops:

### After Stage 3 (Synthesis)

| Condition | Action |
|---------|----------|
| Overall confidence > 7 + a concrete risk-dimension exists | → Stage 4 (validate) or Stage 5 (interviews) |
| Overall confidence 4-7 | → Stage 4 mandatory |
| Overall confidence < 4 | → Return to Stage 1 (rethink hypothesis) or Stage 2 (more research) |
| Cross-fit conflict found (Channel-Model or Model-Market) | → Return to Stage 1 to rethink the conflicting dimensions |

### After Stage 4 (DVF)

| Condition | Action |
|---------|----------|
| Experiment succeeded | → Stage 5 (interviews on the other risk-dimensions) |
| Experiment failed | → Stage 1 (restart the dimension) or Stage 2 (research alternatives) |
| Need more data | → Stage 2 (research) or jump to Stage 5-6 (interviews) |

### After Stage 7 (Interview Synthesis)

| Condition | Action |
|---------|----------|
| Confidence rose, hypothesis confirmed | → Stage 8 (MVP launch) |
| Confidence dropped, corrections needed | → Stage 4 (new assumptions) or Stage 1 (new hypothesis) |
| A new risk-dimension surfaced | → Stage 4 for it |
| A pivot looks needed | → Stage 1, with an explicit "why" recorded |

### After Stage 9 (Metrics)

| Condition | Action |
|---------|----------|
| PMF achieved (Sean Ellis ≥ 40% + retention flatten + Level 3+) | → Out of scope (scale phase) |
| Intermediate signal (Level 2) | → Stage 4 (new validation iteration) or Stage 7 (new interview cycle) |
| Weak signal (Level 1, Sean Ellis < 25%) | → Stage 1 (rethink) or Stage 2 (new research) |

## Handling waiting states (Stage 6 and Stage 8)

These stages are **outside the skill**. When the skill resumes on them:

**Stage 6 (Field interviews):**
- Check that `interview-guide.md` exists → it must
- Check `interviews/notes/` — are there any files?
  - 0 files → "waiting for notes. The guide is ready: interview-guide.md. How many have you done already?"
  - 1-14 files → "keep going in the field. Once you have ≥ 15 — move to Stage 7. You can also do synthesis on the current data, but it is less reliable"
  - 15+ files → "ready to move to Stage 7. Shall we?"
- Do not offer to "conduct an interview for the user"

**Stage 8 (MVP launch):**
- Check that `narrative-v3.md` exists → it must
- Say "waiting for the MVP. Once you have ~40 active users — Stage 9"
- You can discuss technical/product launch questions as a sounding board, but not "launch the MVP"

## Narrative versioning

The narrative is the central document of the whole cycle. It is versioned at the key transitions:

| Version | When created | Based on |
|--------|----------------|----------------|
| **V1** | After Stage 1 | Initial hypothesis |
| **V2** | After Stage 3 | Market research data |
| **V3** | After Stage 7 | Interview data |
| **V4+** | After Stage 10, if iterating | Metrics + decisions |

Each version is its own file (`narrative-v1.md`, `narrative-v2.md`, ...). Do NOT overwrite the previous ones. Each new version has a "Version History" section with a changelog.

## File contracts between stages

What each stage reads and writes:

| Stage | Reads | Writes |
|-------|-------|--------|
| 0 | — | `00_setup.md` |
| 1 | `00_setup.md` | `narrative-v1.md` |
| 2 | `narrative-v1.md` | `market-research.md` |
| 3 | `narrative-v1.md`, `market-research.md` | `risk-prioritization.md`, `narrative-v2.md` |
| 4 | `narrative-v2.md`, `risk-prioritization.md` | `assumptions-map.md`, `experiment-brief.md` |
| 5 | `narrative-v2.md`, `risk-prioritization.md`, `assumptions-map.md` | `interview-guide.md`, `interviews/note-template.md` |
| 7 | `narrative-v2.md`, `interviews/notes/*.md` | `interview-synthesis.md`, `narrative-v3.md` |
| 9 | `narrative-v3.md` | `metrics-dashboard.md` |
| 10 | `metrics-dashboard.md` + everything prior | `iteration-changelog.md` |
