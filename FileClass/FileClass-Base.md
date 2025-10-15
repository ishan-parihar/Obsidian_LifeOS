
# FileClass Base Configuration

This file defines the base FileClass that all other FileClasses will extend. Place this in your configured FileClass folder.

---
fileClass: base-entity
mapWithTag: false

fields:
  # Universal Metadata
  - name: entity_type
    type: Select
    options:
      valuesList:
        "0": "subjective-journal"
        "1": "relational-journal"
        "2": "systemic-journal"
        "3": "activity-log"
        "4": "diet-log"
        "5": "daily-review"
        "6": "weekly-review"
        "7": "monthly-review"
        "8": "quarterly-review"
        "9": "yearly-review"
        "10": "values"
        "11": "vision"
        "12": "annual-goal"
        "13": "quarterly-goal"
        "14": "project"
        "15": "task"
        "16": "person"
        "17": "community"
        "18": "financial-account"
        "19": "financial-log"
        "20": "note"
        "21": "document"
        "22": "story"
        "23": "failure-scenario"

  - name: entity_hierarchy_level
    type: Select
    options:
      valuesList:
        "0": "atomic"
        "1": "review"
        "2": "strategic"
        "3": "resource"
        "4": "risk"

  - name: created
    type: DateTime
    options:
      dateFormat: "YYYY-MM-DDTHH:mm:ss"

  - name: modified
    type: DateTime
    options:
      dateFormat: "YYYY-MM-DDTHH:mm:ss"

  # Strategic Relationships
  - name: parent_entities
    type: MultiFile
    options:
      dvQueryString: "dv.pages()"

  - name: child_entities
    type: MultiFile
    options:
      dvQueryString: "dv.pages()"

  - name: sibling_entities
    type: MultiFile
    options:
      dvQueryString: "dv.pages()"

  # Status Tracking
  - name: status
    type: Select
    options:
      valuesList:
        "0": "Active"
        "1": "Archived"
        "2": "Draft"
        "3": "Planning"
        "4": "Paused"
        "5": "Completed"

  - name: progress
    type: Number

  - name: health
    type: Select
    options:
      valuesList:
        "0": "On Track"
        "1": "At Risk"
        "2": "Blocked"
        "3": "Unknown"

  - name: next_milestone
    type: Input

  - name: blockers
    type: Multi
    options:
      sourceType: "ValuesList"
      valuesList:
        "0": "Resource Constraint"
        "1": "Dependency"
        "2": "Technical Blocker"
        "3": "Decision Needed"
        "4": "External Factor"

---

# Base Entity FileClass

This is the base FileClass that provides universal fields for all entities in the LifeOS system.

## Inheritance Pattern

All specific entity FileClasses should extend this base:

```yaml
---
extends: base-entity
---
```

## Field Descriptions

### Universal Metadata
- **entity_type**: Categorizes the note within the LifeOS taxonomy
- **entity_hierarchy_level**: Indicates position in the system hierarchy
- **created/modified**: Timestamp tracking

### Strategic Relationships
- **parent_entities**: Higher-level entities this belongs to
- **child_entities**: Lower-level entities contained within
- **sibling_entities**: Related entities at same level

### Status Tracking
- **status**: Current lifecycle state
- **progress**: Numeric completion percentage (0-100)
- **health**: Qualitative health indicator
- **next_milestone**: Next key deliverable
- **blockers**: Current impediments