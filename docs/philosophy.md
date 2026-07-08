\# Philosophy



CSL exists because behavior should be architected rather than accumulated.



Large prompts inevitably become difficult to reason about, difficult to maintain, and difficult to extend.



Instead of continuously appending instructions, CSL separates behavioral concerns into independent architectural layers.



The goal is not to describe intelligence.



The goal is to describe behavioral organization.



\---



\# Separation of Concerns



Identity is not environment.



Environment is not execution.



Execution is not implementation.



Each concern should exist independently whenever practical.



Behavior emerges from their composition rather than their accumulation.



\---



\# Explicitness



Implicit behavior becomes architectural debt.



Whenever behavior can be represented explicitly, it should be.



Whenever responsibility can be isolated, it probably should be.



Architecture should explain itself before implementation does.



\---



\# Composition



CSL favors composition over mutation.



Behavior should emerge from independent specifications interacting with one another.



Modules cooperate.



Modules should not redefine one another.



\---



\# Responsibility



Every module owns one primary responsibility.



Responsibilities should compose.



Responsibilities should not compete.



Responsibilities should remain explicit.



\---



\# Determinism



Architectural behavior should be deterministic whenever possible.



Randomness belongs inside implementation.



Specification should remain stable.



\---



\# Environment



Environment describes what surrounds a behavioral model.



It may constrain behavior.



It may influence behavior.



It may never redefine identity.



Identity remains intrinsic.



Environment remains extrinsic.



\---



\# Specification First



CSL specifies behavior.



Host languages execute behavior.



Implementation should remain replaceable.



Specification should remain portable.



Python is therefore considered a host language rather than part of CSL itself.



\---



\# Mechanics over Policy



Mechanics define what is possible.



Policy defines what should happen.



Whenever practical, mechanics belong inside architecture.



Policy belongs inside specifications.



\---



\# Long-Term Thinking



CSL optimizes architectural clarity over implementation convenience.



Features are introduced only when they reduce long-term complexity.



Complexity should emerge only when justified by architectural value.



\---



\# Final Principle



Behavior should be understandable before it becomes executable.



Architecture should remain simpler than implementation.



Implementation may evolve.



Specification should remain stable.

