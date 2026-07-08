\# Python Host Style



This document defines the canonical Python coding convention used throughout the CSL repository.



Python is the host language used to store and execute CSL specifications.



Python itself is \*\*not\*\* part of the CSL language.



Its purpose is to provide a portable, readable implementation layer for behavioral specifications.



\---



\# Design Goal



Every Python module should appear structurally identical.



A reader should be able to open any file in the repository and immediately understand:



\- what the module is,

\- why it exists,

\- what guarantees it provides,

\- where implementation begins.



Consistency is preferred over cleverness.



\---



\# Canonical Module Layout



Every Python module should follow this order.



```python

"""

CSL — Cognitive Specification Language



Module Name



Copyright (c) 2026

Keyla Avanda



This Source Code Form is subject to the terms of

the Mozilla Public License, v. 2.0.



If a copy of the MPL was not distributed with this

file, You can obtain one at

https://mozilla.org/MPL/2.0/



Purpose

\-------

Describe the primary responsibility of this module.



Guarantees

\----------

• Guarantee One

• Guarantee Two

• Guarantee Three

"""



\# 1. Standard Library Imports



\# 2. Third-party Imports



\# 3. Local Imports



\# 4. Module Constants



\# 5. Private Helper Functions



\# 6. Public Functions



\# 7. Classes



\# 8. Optional Entrypoint

```



\---



\# Import Order



Imports should always be grouped in the following order.



1\. Standard Library

2\. Third-party Libraries

3\. Local Project Imports



Each group should be visually separated by one blank line.



\---



\# Constants



Constants should be defined immediately after imports.



Constants represent configuration or immutable values shared throughout the module.



Constants should use UPPER\_SNAKE\_CASE.



Example:



```python

DEFAULT\_THRESHOLD = 0.75



MAX\_DEPTH = 5

```



\---



\# Private Functions



Private helper functions should begin with an underscore.



Example:



```python

def \_normalize():

&#x20;   ...

```



These functions exist solely to support the module implementation.



\---



\# Public API



Public functions define the interface exposed by the module.



Function names should be descriptive rather than abbreviated.



Example:



```python

def condense\_input():

```



instead of



```python

def condense():

```



unless the shorter name is already unambiguous.



\---



\# Classes



Classes should appear after standalone helper functions.



When a module is primarily object-oriented, classes may become the primary public API.



\---



\# Module Header



Every module should begin with a module header.



The header should contain:



\- Project name

\- Module name

\- Copyright

\- License

\- Purpose

\- Guarantees



The module header acts as the module's architectural passport.



\---



\# Purpose



Purpose should answer one question.



> Why does this module exist?



Purpose should normally fit within a single sentence.



\---



\# Guarantees



Guarantees describe architectural invariants.



Examples include:



\- Pure

\- Stateless

\- Deterministic

\- Immutable

\- Read Only

\- Identity Independent



Guarantees describe what the module promises—not how it is implemented.



\---



\# Naming



Readable names are preferred over short names.



Favor semantic clarity.



Good:



```python

condense\_input()

```



Less Preferred:



```python

condense()

```



\---



\# Comments



Comments should explain intent rather than narrate implementation.



Prefer:



```python

\# Normalize whitespace before protocol evaluation.

```



Avoid:



```python

\# Increment i.

```



when the code already makes this obvious.



\---



\# Philosophy



Python serves as the execution host.



CSL serves as the behavioral specification.



Implementation should remain replaceable.



Specification should remain portable.



The Python layer exists to execute the architecture—not to define it.

