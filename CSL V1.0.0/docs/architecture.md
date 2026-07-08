\# Architecture



This document defines the canonical architecture of CSL.



Unlike the philosophy document, which explains \*why\* CSL exists, this document explains \*how\* the system is organized.



The architecture defines structural rules rather than implementation details.



Implementations may evolve.



The architecture should remain comparatively stable.



\---



\# Foundational Module Layout (FML)



CSL follows a fixed dependency hierarchy known as the \*\*Foundational Module Layout (FML).\*\*



```text

┌───────────────────────────────┐

│            STAGE 1            │

│             Boot              │

└───────────────┬───────────────┘

&#x20;               │

&#x20;               ▼

┌───────────────────────────────┐

│            STAGE 2            │

│           Protocol            │

└───────────────┬───────────────┘

&#x20;               │

&#x20;               ▼

┌───────────────────────────────┐

│            STAGE 3            │

│           Character           │

└───────────────┬───────────────┘

&#x20;               │

&#x20;               ▼

┌───────────────────────────────┐

│            STAGE 4            │

│          Environment          │

└───────────────┬───────────────┘

&#x20;               │

&#x20;               ▼

┌───────────────────────────────┐

│            STAGE 5            │

│      Decision Synthesis       │

└───────────────────────────────┘



```



Every higher stage may consume lower stages.



Lower stages must never depend upon higher stages.



Dependency direction is considered an architectural invariant.



\---



\# Stage Responsibilities



\## Stage 1 — Boot



Responsible for runtime initialization.



Boot establishes the execution environment.



Boot should remain intentionally minimal.



\---



\## Stage 2 — Protocol



Defines communication contracts.



Protocol specifies structural conventions and data exchange.



Protocol does not define behavior.



\---



\## Stage 3 — Character



Defines intrinsic behavioral identity.



Character represents the stable behavioral core.



Character should remain independent of runtime context.



\---



\## Stage 4 — Environment



Defines contextual constraints surrounding the behavioral model.



Environment may influence behavior.



Environment may never redefine identity.



Environment remains externally descriptive.



\---



\## Stage 5 — Decision Synthesis



Produces executable behavioral decisions.



Decision Synthesis consumes Character and Environment.



Decision Synthesis should not redefine either.



Behavior emerges through synthesis rather than mutation.



\---



\# Dependency Rules



Dependencies always flow downward.



Valid:



```text

&#x20; ┌───────────┐

&#x20; │  Stage 5  │

&#x20; └─────┬─────┘

&#x20;       │

&#x20;       ▼

&#x20; ┌───────────┐

&#x20; │  Stage 4  │

&#x20; └─────┬─────┘

&#x20;       │

&#x20;       ▼

&#x20; ┌───────────┐

&#x20; │  Stage 3  │

&#x20; └───────────┘



```



Invalid:



```text

&#x20; ┌───────────┐

&#x20; │  Stage 3  │

&#x20; └─────┬─────┘

&#x20;       │

&#x20;       ▲  X (STRICT CONSTRAINT)

&#x20;       │

&#x20; ┌───────────┐

&#x20; │  Stage 5  │

&#x20; └───────────┘



```



Lower stages remain unaware of higher stages.



\---



\# Architectural Invariants



> ### 🛑 System Invariants

> 

> 

> \* Identity is immutable.

> \* Environment cannot overwrite identity.

> \* Modules own one primary responsibility.

> \* Specifications remain implementation-independent.

> \* Runtime behavior is synthesized rather than accumulated.

> \* Host implementations remain replaceable.

> 

> 



\---



\# Specification Layers



CSL separates four conceptual layers.



```text

&#x20;┌────────────────┐

&#x20;│ Specification  │

&#x20;└───────┬────────┘

&#x20;        │

&#x20;        ▼

&#x20;┌────────────────┐

&#x20;│  Composition   │

&#x20;└───────┬────────┘

&#x20;        │

&#x20;        ▼

&#x20;┌────────────────┐

&#x20;│   Execution    │

&#x20;└───────┬────────┘

&#x20;        │

&#x20;        ▼

&#x20;┌────────────────┐

&#x20;│ Implementation │

&#x20;└────────────────┘



```



Specification defines behavior.



Execution realizes behavior.



Implementation provides the runtime.



\---



\# Host Language



Python functions as the reference host language.



Python stores and executes CSL specifications.



Python itself is not part of the CSL language.



Host-language conventions are documented separately in:



```text

docs/python\_style.md



```



\---



\# Environment Model



Environment represents the area surrounding the behavioral model.



Environment is intentionally external.



Environment may:



\* provide context,

\* constrain decisions,

\* modify runtime interpretation.



Environment may never redefine Character.



\---



\# Decision Synthesis



Decision Synthesis computes behavioral output.



Its primary responsibility is combining Character and Environment into executable behavior.



Decision Synthesis should remain deterministic whenever possible.



Implementation-specific optimization belongs outside the architectural specification.



\---



\# Scope



CSL specifies behavioral architecture.



CSL does not define:



\* model weights,

\* neural architectures,

\* optimization algorithms,

\* inference engines,

\* hardware execution.



These remain responsibilities of host implementations.



\---



\# Out of Scope



The following concepts intentionally remain outside the core specification.



\* Plugin systems

\* Multi-runtime execution

\* Rollback systems

\* Reflection engines

\* Dynamic architecture mutation



These may be explored by future versions but are not required by CSL v1.0.



\---



\# Versioning



Architectural changes should occur less frequently than implementation changes.



Implementation evolves.



Architecture accumulates.



Specification persists.



Current version:



\*\*CSL v1.0\*\*



```

