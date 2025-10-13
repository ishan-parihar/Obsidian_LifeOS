---
name: "[Project Name]"
status: planning
priority: medium
area: null
startDate: 2025-10-13
deadline: null
completedDate: null
progress: 0
health: green
quarterlyGoal: null
tags: [project, co-pilot]
---

# Project - {{name}}

## 🎯 Project Overview
**Desired Outcome**: What does success look like?
**Why This Matters**: Purpose and strategic importance
**Area of Responsibility**: {{area}}
**Quarterly Goal Alignment**: {{quarterlyGoal}}

## 📋 Project Details
- **Status**: {{status}} (planning/active/completed/archived)
- **Priority**: {{priority}} (urgent/high/medium/low)
- **Start Date**: {{startDate}}
- **Deadline**: {{deadline}}
- **Completed Date**: {{completedDate}}
- **Progress**: {{progress}}%
- **Health Status**: {{health}} (green/yellow/red)
- **Estimated Effort**: hours
- **Resources Needed**:

## ✅ Action Plan

### Current Sprint Tasks
```dataview
TABLE status, priority, context, dueDate
FROM "03 - The Workbench/Act II - The Co-Pilot Stream/Tasks"
WHERE project = "{{name}}" AND sprint = "current"
SORT priority DESC, dueDate ASC
```

### Next Sprint Pipeline
```dataview
TABLE sprint, status, priority, dueDate
FROM "03 - The Workbench/Act II - The Co-Pilot Stream/Tasks"
WHERE project = "{{name}}" AND sprint != "current" AND sprint != "backlog"
SORT sprint ASC, priority DESC
```

### Backlog Tasks
```dataview
TABLE status, priority, estimatedTime
FROM "03 - The Workbench/Act II - The Co-Pilot Stream/Tasks"
WHERE project = "{{name}}" AND sprint = "backlog"
SORT priority DESC, estimatedTime ASC
```

## 📚 Related Resources
- **Notes**:
- **Documents**:
- **People Involved**:
- **Systemic Journal Entries**:

## 🔄 Progress Notes

### Week of {{date}}
**Progress Made**:
**Challenges Encountered**:
**Resource Constraints**:
**Next Steps**:

## 🎯 Success Criteria
- [ ] Defined outcome achieved
- [ ] Quality standards met
- [ ] Timeline respected (or adjusted appropriately)
- [ ] Resources utilized efficiently
- [ ] Learning captured for future projects

## 📊 Project Metrics
- **% Complete**: {{progress}}%
- **Time Spent**: hours
- **Budget Used**:
- **Task Completion Rate**:
- **Health Trend**:

## 🔗 Related Items
- **Quarterly Goal**: [[{{quarterlyGoal}}]]
- **Area of Responsibility**: [[{{area}}]]
- **Failure Scenarios**: (Linked risks)
- **People Database**: (Key stakeholders)

> **Project Management Tip**: Review project health weekly. Adjust scope, timeline, or resources as needed to maintain green health status.