---
weekNumber: 42
year: 2025
startDate: 2025-10-13
endDate: 2025-10-19
status: active
quarter: Q4 2025
month: October 2025
tags: [week, planning, review]
---

# Week - {{weekNumber}} {{year}}

## 📅 Week Overview
- **Week Number**: {{weekNumber}}
- **Year**: {{year}}
- **Start Date**: {{startDate}}
- **End Date**: {{endDate}}
- **Quarter**: {{quarter}}
- **Month**: {{month}}

## 🎯 Weekly Planning

### Intentions & Focus Areas
**Primary Focus**:
**Secondary Focuses**:
**Energy Management**:

### Key Results to Achieve
1. [ ]
2. [ ]
3. [ ]

### Time Blocking
- **Deep Work Blocks**:
- **Meetings/Coordination**:
- **Rest/Recovery**:
- **Relationship Nurturing**:

## 📋 Weekly Review

### Days Synthesis
```dataview
TABLE status, energyLevel, productivityScore
FROM "03 - The Workbench/Act I - The Ignition Sequence"
WHERE type = "day" AND week = "{{weekNumber}} {{year}}"
SORT date ASC
```

### Tasks Completed This Week
```dataview
TABLE project, priority, context, completionDate
FROM "03 - The Workbench/Act II - The Co-Pilot Stream/Tasks"
WHERE completionDate >= {{startDate}} AND completionDate <= {{endDate}}
SORT completionDate ASC
```

### Tasks Carried Forward
```dataview
TABLE project, priority, dueDate, status
FROM "03 - The Workbench/Act II - The Co-Pilot Stream/Tasks"
WHERE status != "completed" AND dueDate <= {{endDate}}
SORT priority DESC
```

### Financial Summary
```dataview
TABLE sum(amount) as totalSpent, category
FROM "03 - The Workbench/Act I - The Ignition Sequence/Financial Accounts"
WHERE date >= {{startDate}} AND date <= {{endDate}}
GROUP BY category
```

### Key Insights & Patterns
- **What worked well**:
- **What needs adjustment**:
- **Emerging patterns**:
- **Energy insights**:

## 🔄 Forward Planning

### Next Week Preview
- **Key commitments**:
- **Potential challenges**:
- **Preparation needed**:

### Quarterly Goal Progress
```dataview
TABLE progress, health, kpis
FROM "03 - The Workbench/Act I - The Ignition Sequence/Quarterly Goals"
WHERE quarter = "{{quarter}}"
```

## 🔗 Related Items
- **Days**: (Links to individual days)
- **Month**: [[Month - {{month}}]]
- **Quarter**: [[Quarter - {{quarter}}]]
- **Projects Active**:

## 📊 Weekly Metrics
- **Task Completion Rate**:
- **Energy Average**:
- **Focus Quality**:
- **Relationship Investment**:
- **Health Compliance**:

> **Review Tip**: Complete weekly review on Sunday evening or Monday morning. Spend 30-60 minutes for thorough integration.