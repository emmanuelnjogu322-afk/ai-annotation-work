# Day One — Annotation Notes

## Core reasoning model

For each frame:
1. Observe — record what is visibly present.
2. Classify — assign the appropriate object class.
3. Count instances — each distinct object is treated as its own instance when the task calls for instance-level annotation.
4. Check visibility — distinguish fully visible, partially visible, and occluded objects according to the project rules.
5. Decide — annotate only what the evidence supports.
6. Validate — review for missing, duplicated, or incorrectly merged instances.

## Example reasoning

A frame contains:
- Car A: fully visible
- Car B: approximately 40% visible
- Motorcycle: visible

If the task is instance-level vehicle annotation, the working interpretation is:

**Vehicle instances = 3**

Visibility does not automatically merge two distinct vehicles into one instance. Visibility is a separate attribute from instance identity.

## Class vs. instance

**Class:** what the object is. Example: vehicle.

**Instance:** which individual object it is.
- vehicle instance 1 → Car A
- vehicle instance 2 → Car B
- vehicle instance 3 → Motorcycle

## Uncertainty protocol

When uncertain:
- do not invent hidden content
- state the observable evidence
- separate assumptions from observations
- check the annotation guidelines
- record the decision and why it was made

## Day One lesson

Good annotation is not only about seeing objects. It is about applying the same decision rule consistently across frames.
