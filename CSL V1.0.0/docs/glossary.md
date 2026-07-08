\# Glossary



This document defines the canonical vocabulary used throughout CSL.



The purpose of this glossary is to ensure terminology remains consistent across documentation and implementations.



\---



\# Architecture



The structural organization of a behavioral system.



Architecture defines responsibilities and relationships.



It does not define implementation.



\---



\# Behavior



The observable output produced by a system.



Behavior emerges through Decision Synthesis.



Behavior is not synonymous with Character.



\---



\# Boot



Stage 1 of the Foundational Module Layout.



Responsible for runtime initialization.



\---



\# Character



Stage 3 of the Foundational Module Layout.



Character defines intrinsic behavioral identity.



Character remains independent of Environment.



\---



\# Composition



The process of combining independent specifications into a coherent behavioral model.



Composition does not modify the participating specifications.



\---



\# Decision Synthesis



Stage 5 of the Foundational Module Layout.



Decision Synthesis combines Character and Environment into executable behavioral output.



\---



\# Dependency



A relationship where one module consumes another.



Dependencies always flow downward through the Foundational Module Layout.



\---



\# Environment



Stage 4 of the Foundational Module Layout.



Environment describes external context surrounding the behavioral model.



Environment may influence behavior.



Environment may never redefine Character.



\---



\# Foundational Module Layout (FML)



The canonical dependency hierarchy used throughout CSL.



FML defines the architectural ordering of all stages.



\---



\# Guarantee



An architectural invariant promised by a module.



Guarantees describe expected behavior independently of implementation.



\---



\# Host Language



A programming language used to execute CSL specifications.



Python is the reference host language.



\---



\# Identity



The stable intrinsic behavior of a system.



Identity is represented by Character.



Identity is immutable during execution.



\---



\# Implementation



Executable software that realizes a CSL specification.



Implementations may vary while preserving the same specification.



\---



\# Mechanic



A structural capability provided by architecture.



Mechanics define what is possible.



\---



\# Module



A single architectural unit with one primary responsibility.



Modules compose.



Modules should not compete.



\---



\# Policy



A behavioral decision built upon architectural mechanics.



Policies describe desired behavior.



Mechanics describe capability.



\---



\# Protocol



Stage 2 of the Foundational Module Layout.



Defines communication conventions and structural contracts.



\---



\# Responsibility



The single primary purpose assigned to a module.



Every module should own exactly one primary responsibility.



\---



\# Specification



A declarative description of behavioral architecture.



Specifications describe behavior independently from implementation.



\---



\# Stage



One architectural layer inside the Foundational Module Layout.



Stages consume previous stages while preserving dependency direction.



\---



\# Synthesis



The computation that transforms specifications into executable behavior.



Synthesis consumes previous stages without modifying them.

