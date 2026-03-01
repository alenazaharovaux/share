# skill-creator

A Claude Code skill for writing, testing, and deploying other skills. Applies Test-Driven Development principles to process documentation: you write pressure scenarios (tests), watch agents fail without the skill (RED), write the skill (GREEN), and close loopholes (REFACTOR).

This skill is extracted from the [superpowers](https://github.com/anthropics/claude-plugins-official/tree/main/superpowers) plugin by Jesse Vincent, licensed under MIT.

## Installation

Copy the `skill-creator` folder to `~/.claude/skills/`:

```
~/.claude/skills/skill-creator/
  SKILL.md
  anthropic-best-practices.md
  persuasion-principles.md
  testing-skills-with-subagents.md
  graphviz-conventions.dot
  render-graphs.js
  examples/
    CLAUDE_MD_TESTING.md
```

## Contents

| File | Description |
|------|-------------|
| `SKILL.md` | Main skill reference: structure, naming, CSO, TDD cycle, checklist |
| `anthropic-best-practices.md` | Official Anthropic guidance on skill authoring |
| `persuasion-principles.md` | Research-backed persuasion techniques for discipline-enforcing skills |
| `testing-skills-with-subagents.md` | How to test skills with pressure scenarios and subagents |
| `graphviz-conventions.dot` | Style guide for flowcharts in skills |
| `render-graphs.js` | Node.js utility to render dot diagrams from SKILL.md to SVG |
| `examples/CLAUDE_MD_TESTING.md` | Worked example: testing CLAUDE.md documentation variants |

## License

MIT. See [LICENSE](LICENSE).
