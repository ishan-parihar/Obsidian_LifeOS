---
title: 
goal_archetype: 
strategic_intent: 
strategic_approach: 
the_epic: 
target_value: 
success_condition: 
key_risks: 
status: Draft
vision: []
quarters: []
quarterly_goals: []
projects: []
tasks: []
primary_metric: []
current_annual_goal: 
goal_progress: 0
planned_range: 
type: annual-goal
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.file.title %>

## 🎯 Goal Overview

**Goal Archetype**: 
**Status**: 
**Progress**: 0%

### Strategic Intent

### Strategic Approach

### The Epic

## 📊 Success Framework

**Target Value**: 
**Success Condition**: 

### Key Metrics

## ⚠️ Risk Assessment

**Key Risks**: 

## 🔗 Strategic Alignment

**Vision Connection**: 
**Values Alignment**: 

## 📈 Progress Tracking

### Quarterly Breakdown

```dataview
TABLE WITHOUT ID
  file.link as "Quarterly Goal",
  status as "Status",
  goal_progress as "Progress"
FROM "Strategy/QuarterlyGoals"
WHERE contains(string(annual_goals), string("<% tp.file.title %>"))
SORT file.name DESC
```

### Supporting Projects

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  project_progress as "Progress"
FROM "Projects"
WHERE contains(string(annual_goals), string("<% tp.file.title %>"))
SORT project_progress DESC
```

### Task Rollup

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  status as "Status",
  priority as "Priority"
FROM "16-Tasks"
WHERE contains(string(annual_goals), string("<% tp.file.title %>"))
SORT priority DESC
```

---

*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
