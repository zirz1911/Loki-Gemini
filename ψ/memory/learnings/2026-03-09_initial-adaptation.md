# Learning: Adapting Claude to Gemini

**Date**: 2026-03-09
**Topic**: Porting Project Principles and Structures

## The Pattern
The original project (Loki-Oracle) uses a highly structured environment with sub-agents and custom markdown commands. This structure provides "rails" for the AI to stay in character and maintain consistency across sessions.

## The Adaptation
1. **Infrastructure**: Instead of `.claude/`, we use `GEMINI.md` and `ψ/` for context.
2. **Commands**: Gemini CLI doesn't need external markdown "commands" to trigger logic as much as Claude does, because Gemini has direct access to specialized tools like `codebase_investigator`.
3. **Memory**: The `ψ/` (Psi) structure is universal. It works as an "External Brain" regardless of the model.

## Reusable Insight
A project's "Soul" (Identity and Principles) is platform-independent. The "Body" (Tools and Commands) must be adapted to the specific strengths of the AI interface. Gemini's strength is its large context and tool integration, which allows for more autonomous investigation compared to strict step-by-step command execution.

---
*Loki Gemini: First Learning Recorded.*
