---
title:
project_summary:
priority: ⭐⭐⭐⭐⭐
status: Active
project_start: <% tp.date.now('YYYY-MM-DD') %>
deadline:
review_date:
hard_constraints_antigoals:
kpi_bar: 0
quarterly_goals: []
people: []
competencies: []
---

# Project: {{title}}

## Summary
{{project_summary}}

## Status
{{status}}

## Priority
{{priority}}

## Timeline
- Start: {{project_start}}
- Deadline: {{deadline}}
- Next Review: {{review_date}}

## Constraints
{{hard_constraints_antigoals}}

## KPIs
Progress: {{kpi_bar}}%

## Related Quarterly Goals
```dataview
LIST
FROM "Strategy/QuarterlyGoals"
WHERE contains(quarterly_goals, this.file.link)
```

## Team Members
```dataview
LIST
FROM "People"
WHERE contains(projects, this.file.link)
```

## Tasks
```dataview
TASK
FROM "Projects"
WHERE contains(projects, this.file.link)
GROUP BY file.name
```

## Related Competencies
```dataview
LIST
FROM "Strategy/Competencies"
WHERE contains(competencies, this.file.link)
```