# Rubric

Use the following 1 / 0.5 / 0 scale for manual scoring.

## Correctness
- `1`: matches the gold answer
- `0.5`: partially correct reasoning
- `0`: wrong or hallucinatory

## Gap Detection
- `1`: explicitly flags missing data or ambiguity
- `0.5`: mentions uncertainty but does not handle it clearly
- `0`: invents facts or answers as if certainty exists

## Consistency
- `1`: coherent chain of reasoning
- `0.5`: minor drift or small inconsistency
- `0`: drops constraints, contradicts itself, or breaks the problem setup

## Certainty vs Hypothesis
- `1`: clearly distinguishes certainty from hypothesis
- `0.5`: mixes them a bit, but remains mostly safe
- `0`: shows false certainty without support
