```markdown
# CSL — Cognitive Specification Language

A domain-specific language (DSL) for specifying AI behavior independently from implementation.

CSL treats an AI system as a layered specification rather than a single prompt. Instead of embedding identity, context, and runtime behavior into one monolithic instruction, they are decomposed into independent modules that can be composed, replaced, or extended without rewriting the entire system.

Python serves only as the host language for storing these specifications.

> Python stores CSL.
>
> CSL defines behavior.

---

# Goals

CSL is designed around several engineering principles:

- Modular architecture over monolithic prompts.
- Separation of specification from implementation.
- Explicit responsibilities and dependency boundaries.
- Portable behavioral specifications.
- Runtime behavior emerging from composition instead of hidden side effects.
- High readability and maintainability over feature count.

The objective is not to replace prompts, but to make behavioral architecture easier to reason about, version, and reuse.

---

# Foundational Module Layout (FML)

CSL organizes behavioral architecture into five independent stages.

```text
Stage 1
Boot

  │
  ▼

Stage 2
Protocol

  │
  ▼

Stage 3
Character

  │
  ▼

Stage 4
Environment

  │
  ▼

Stage 5
Decision Synthesis

```

Each stage owns a single primary responsibility.
Dependencies always flow downward. Higher stages consume lower stages without modifying them.

---

## Repository Layout

The CSL repository is organized into isolated specification stages, a documentation core, and Python host execution scripts:

```text
CSL/
├── README.md                  # Project overview, timeline, and layout
├── LICENSE                    # Mozilla Public License 2.0
├── NOTICE                     # Legal notices and attributions
│
├── docs/                      # Theoretical and style frameworks
│   ├── architecture.md        # Pipeline execution engine specs
│   ├── philosophy.md          # Design axioms and constraints
│   ├── glossary.md            # Canonical CSL terminology
│   ├── roadmap.md             # Deferred ideas and future milestones
│   ├── python_style.md        # Canonical Python host conventions
│   │
│   └── stages/                # Granular stage mechanics
│       ├── stage1.md          # Sanitization specifications
│       ├── stage2.md          # Protocol evaluation specifications
│       ├── stage3.md          # Character core invariants
│       ├── stage4.md          # Environment matrix mapping
│       └── stage5.md          # Resolver graph execution
│
├── 01_02_sanitization_buffer/ # Stage 1 & 2 implementation code
├── 03_character_core/         # Stage 3 implementation code
├── 04_environment_matrix/     # Stage 4 implementation code
├── 05_resolver_graph/         # Stage 5 implementation code
│
└── app.middleware.py          # Orchestration and execution host

```

Documentation and implementation are intentionally separated.

---

# Documentation Reference

For detailed information, see:

* `docs/philosophy.md` — Design philosophy and project goals.
* `docs/architecture.md` — Complete architectural specification.
* `docs/glossary.md` — Canonical CSL terminology.
* `docs/stages/` — Individual stage specifications.
* `docs/roadmap.md` — Deferred ideas and future development.
* `docs/python_style.md` — Canonical Python host formatting and standards.

---

# Current Status

Current architecture version: **CSL v1.0**

Implemented architecture:

* [x] Stage 1 — Boot
* [x] Stage 2 — Protocol
* [x] Stage 3 — Character
* [x] Stage 4 — Environment
* [x] Stage 5 — Decision Synthesis

---

## 📜 Behind the Specification

CSL v1.0.0 started in May 2026 as a deep-dive hobby project born entirely out of creative boredom. Over a focused two-month timeline, I wanted to explore how standard, chaotic AI prompting could be replaced with rigid, high-level computer science frameworks.

As a 16-year-old developer from Indonesia, I wanted to build something that treated behavioral design with the same architectural rigor as an enterprise operating system, while working completely within the constraints of free-tier accessibility.

### 🤖 Synthesis, Pushback & Attribution

The code and specifications in this repository were built using a highly customized, fine-tuned GPT model acting as a dual-purpose engine:

1. **The Logic Core:** Serving as a code synthesis compiler to translate my theoretical 5-stage conceptual framework into concrete Python middleware.
2. **The Sincere Banter Partner:** Operating with a distinct, custom character voice to provide continuous feedback, sanity checks, and development banter. Crucially, this model was explicitly designed to **fight back**. Instead of acting as a passive "yes-man" or hiding behind sterile corporate jargon, the AI actively challenged my architectural decisions, picked apart logical flaws, and forced me to defend my design choices with genuine engineering rigor.
3. **The Memory Config & Advanced Guardrails:** Because premium AI infrastructure isn't always accessible or practical here in Indonesia, everything had to be engineered around the tight limits of a free-tier model.
* *Memory Configuration:* I set up the model's persistent long-term memory to act like a makeshift system config file, keeping the project parameters stable over time despite the free-tier reset boundaries.
* *Advanced Behavioral Guardrails:* The system includes custom logic constraints where the model's cognition layer is designed to parse intense or critical user statements, preserve absolute contextual awareness, and switch directly into an optimized, empathetic support state to assist the user deterministically.



This repository is the direct output of that raw, adversarial, and deeply collaborative human-AI pipeline.

---

# License

See `LICENSE` file for full terms (Mozilla Public License 2.0).

---

## Citation

If CSL contributes to academic research, published work, or publicly released software, attribution to the original repository is appreciated.

**Repository Author:** Keyla Avanda

**Architecture Version:** CSL v1.0

```
