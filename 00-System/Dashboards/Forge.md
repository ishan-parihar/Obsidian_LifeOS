---
dashboard_type: forge
created: 2025-10-14
---
# The Forge

> **Execution Engine** - Project and task management hub

## 🏗️ Active Projects

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  priority as "Priority",
  project_progress as "Progress",
  deadline as "Deadline"
FROM "15-Projects"
WHERE status = "Active"
SORT priority DESC, deadline ASC
```

## 🚀 Current Sprint

**Sprint Period**: <% tp.date.now("YYYY-MM-DD", 0, -tp.date.now().weekday) %> - <% tp.date.now("YYYY-MM-DD", 6, -tp.date.now().weekday) %>

### Sprint Tasks

```dataview
TASK
WHERE contains(text, "#sprint/current") AND !completed
GROUP BY file.link
```

### Sprint Backlog

```dataview
TASK
WHERE contains(text, "#sprint/backlog") AND !completed
LIMIT 10
```

## 📋 Task Pipeline

### Up Next (Ready to Start)
```dataview
TASK
WHERE status = "Up Next" AND !completed
SORT priority DESC
LIMIT 5
```

### In Progress
```dataview
TASK
WHERE status = "Active" AND !completed
SORT priority DESC
```

### Recently Completed
```dataview
TASK
WHERE completed AND completion >= date(today) - dur(7 days)
SORT completion DESC
LIMIT 10
```

## 📊 Project Health Matrix

```dataview
TABLE WITHOUT ID
  choice(project_progress >= 80, "🟢", choice(project_progress >= 50, "🟡", "🔴")) as "Health",
  file.link as "Project",
  project_progress as "Progress",
  status as "Status"
FROM "15-Projects"
WHERE status = "Active"
SORT project_progress DESC
```

## 🎯 Strategic Execution

### Quarterly Goal Alignment

```dataview
TABLE WITHOUT ID
  quarterly_goals as "Q-Goal",
  count(rows) as "Active Projects"
FROM "15-Projects"
WHERE status = "Active"
GROUP BY quarterly_goals
```

### Annual Goal Progress

```dataview
TABLE WITHOUT ID
  annual_goals as "Annual Goal",
  sum(rows.project_progress) / count(rows) as "Avg Progress"
FROM "Projects"
WHERE status = "Active"
GROUP BY annual_goals
```

## ⚡ Quick Actions

- [ ] Move task to Current Sprint
- [ ] Create new project
- [ ] Sprint retrospective
- [ ] Replan next sprint

## 🌐 Hierarchical Navigation

### From Projects → Tasks
```dataview
TABLE WITHOUT ID
  file.link as "Task",
  status as "Status",
  priority as "Priority",
  due_date as "Due"
FROM "16-Tasks"
WHERE contains(projects, "Active")
SORT priority DESC, due_date ASC
LIMIT 10
```

---

*Last updated: 2025-10-14*
