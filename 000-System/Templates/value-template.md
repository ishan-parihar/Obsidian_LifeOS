---
title:
core_tenet:
the_commitment:
the_boundary:
shadow_expression:
litmus_test:
status: Active
---

# Core Principle: {{title}}

## Core Tenet
{{core_tenet}}

## The Commitment
{{the_commitment}}

## The Boundary
{{the_boundary}}

## Shadow Expression
{{shadow_expression}}

## Litmus Test
{{litmus_test}}

## Alignment Check
```dataview
LIST
FROM "Strategy/Vision"
WHERE contains(values, this.file.link)
```