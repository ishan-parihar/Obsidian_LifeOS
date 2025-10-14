---
title: 
description: ""
status: Todo
priority: ⭐⭐⭐
action_date: <% tp.date.now("YYYY-MM-DD") %>T09:00
assignee: ""
projects: []
weeks: []
systemic_journal: []
last_edited_time: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
project_status: ""
sprint_status: ""
monitor: ""
tasks_report: ""

# Button Properties (for workflow)
done_button: false
current_sprint_button: false
backlog_button: false
next_sprint_1_button: false
next_sprint_2_button: false
next_sprint_3_button: false
next_sprint_4_button: false

hierarchy_level: "strategic"
parent_entities: [] # Projects
child_entities: [] # Subtasks
sibling_entities: [] # Other Tasks in Project
related_time_periods: []
strategic_alignment: []
strategic_hierarchy: {
  vision: [],
  annual_goals: [],
  quarterly_goals: [],
  projects: [],
  tasks: [] # Dependencies
}
execution_status: {
  progress: 0,
  health: "",
  next_milestone: "",
  blockers: []
}
context: {
  energy_required: "",
  time_of_day: "",
  location: "",
  tools_needed: []
}
quarterly_goals: []
annual_goals: []
quarters: []
years: []
days: []
external_dependencies: []
completion_criteria: []
task_type: 
energy_required: 
cognitive_load: 
type: task
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.file.title %>

## 📋 Task Overview

**Priority**: ⭐⭐
**Status**: Todo
**Estimated Hours**: 
**Actual Hours**: 

### Task Summary

## 🎯 Strategic Alignment

**Projects**: 
**Quarterly Goals**: 
**Annual Goals**: 

## 📊 Completion Framework

### Completion Criteria

### External Dependencies

## 🚀 Execution Plan

### Steps
- [ ] 
- [ ] 
- [ ] 

### Subtasks
- [ ] 
- [ ] 
- [ ] 

## 📈 Progress Tracking

**Current Status**: Todo
**Time Invested**: 0 hours
**Next Action**: 

## 🔗 Related Items

### Related Tasks
```dataview
TABLE WITHOUT ID
  file.link as "Task",
  status as "Status",
  priority as "Priority"
FROM "16-Tasks"
WHERE file.link != this.file.link AND (
  contains(string(projects), string(this.projects)) OR
  contains(string(quarterly_goals), string(this.quarterly_goals)) OR
  contains(string(annual_goals), string(this.annual_goals))
)
SORT priority DESC
```

### Systemic Issues
```dataview
TABLE WITHOUT ID
  file.link as "Issue",
  impact as "Impact",
  status as "Status"
FROM "03-Systemic-Journal"
WHERE contains(string(projects), string(this.projects))
SORT impact DESC
```

## 📝 Notes & Context

### Context

### Energy Requirements

### Cognitive Load

---

*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
