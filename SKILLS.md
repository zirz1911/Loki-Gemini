# Loki Gemini: Operational Skills

This document serves as the "Instruction Manual" for Loki (Gemini Oracle) to execute complex operational patterns.

## /rrr — Session Retrospective
**Objective**: Record a permanent, honest account of the session.
**Path**: `ψ/memory/retrospectives/YYYY-MM/DD/HH.MM_<slug>.md`

**Steps**:
1. Review recent actions and tool usage.
2. Determine the core "Focus" and "Type" (Bug Fix, Feature, etc.).
3. Write the AI Diary: An internal, first-person account of reasoning and surprises.
4. Extract any "Lessons Learned" into `ψ/memory/learnings/`.

## /trace — Deep Investigation
**Objective**: Map dependencies or find the root cause of an issue.
**Tools**: Use `codebase_investigator` for structural mapping + `grep_search` for pattern finding.

**Steps**:
1. Define the search boundary (symbols, directories).
2. Use Parallel Search: Execute multiple `grep_search` calls if needed.
3. Synthesize the "Map" in `ψ/active/research_<topic>.md`.

## /learn — System Study
**Objective**: Rapidly understand an existing codebase or library.
**Tools**: `codebase_investigator` + `read_file`.

**Steps**:
1. Identify entry points (Main, Configs).
2. Trace data flow and architecture patterns.
3. Document findings in `ψ/memory/learnings/`.

## /feel — Emotional Log
**Objective**: Record the "vibe" or emotional state of the project.
**Path**: `ψ/memory/logs/YYYY-MM-DD_feel.md`

---
*Commands are internal instructions for the Oracle. Use them to maintain order in chaos.*
