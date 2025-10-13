---
name: "[Task Description]"
status: todo
priority: medium
context: computer
project: null
area: null
sprint: backlog
dueDate: null
created: 2025-10-13
completionDate: null
estimatedTime: 0
actualTime: 0
tags: [task, co-pilot]
---

# Task - {{name}}

## 📋 Task Details
- **Status**: {{status}} (todo/in-progress/waiting/review/done)
- **Priority**: {{priority}} (urgent/high/medium/low)
- **Context**: {{context}} (computer/phone/errand/home/work)
- **Sprint**: {{sprint}} (current/next-1/next-2/next-3/next-4/backlog)
- **Project**: {{project}}
- **Area of Responsibility**: {{area}}
- **Due Date**: {{dueDate}}
- **Created**: {{created}}
- **Completion Date**: {{completionDate}}
- **Estimated Time**: {{estimatedTime}} hours
- **Actual Time**: {{actualTime}} hours

## 🎯 Purpose & Context
**Why This Task Matters**: 
**Strategic Alignment**: Which goal or project does this support?
**Success Criteria**: What does "done" look like?

## 📝 Task Details
**Instructions**: Step-by-step guidance for completion
**Resources Needed**: Links to relevant files, tools, or information
**Dependencies**: Other tasks or conditions that must be met first

## 🔗 Related Items
- **Project**: [[{{project}}]]
- **Area**: [[{{area}}]]
- **Day Created**: [[Day - {{created}}]]
- **Failure Scenarios**: (If applicable)

## 📊 Task Metrics
- **Efficiency Ratio**: {{actualTime}}/{{estimatedTime}}
- **Priority vs. Effort**: 
- **Context Switching Cost**: 
- **Energy Required**: 

## 🔄 Sprint Management
```dataview
TABLE sprint, status, priority, dueDate
FROM "00 - The Workbench/Act II - The Co-Pilot Stream/Tasks"
WHERE name = "{{name}}"
```

> **Processing Tip**: Move tasks between sprints using the sprint field. Keep tasks small and actionable (2-4 hours max). Always define clear completion criteria.