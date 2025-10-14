---
title: LifeOS Hierarchical Dashboard
dashboard_type: master
type: dashboard
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# 🌟 LifeOS Hierarchical Dashboard

> **Complete bidirectional data flow across all time horizons and strategic levels**

---

## 🎯 Strategic Execution Hierarchy

### Vision → Annual Goals
```dataview
TABLE WITHOUT ID
  file.link as "Annual Goal",
  status as "Status",
  goal_progress as "Progress",
  round(goal_progress) + "%" as "Complete"
FROM "Strategy/AnnualGoals"
WHERE status != "Archived"
SORT goal_progress DESC
```

### Annual → Quarterly Goals
```dataview
TABLE WITHOUT ID
  annual_goals[0] as "Annual Goal",
  file.link as "Quarterly Goal",
  status as "Status",
  goal_progress as "Progress"
FROM "Strategy/QuarterlyGoals"
WHERE status != "Archived"
SORT annual_goals[0], goal_progress DESC
```

### Quarterly → Projects
```dataview
TABLE WITHOUT ID
  quarterly_goals[0] as "Quarterly Goal",
  file.link as "Project",
  status as "Status",
  project_progress as "Progress"
FROM "Projects"
WHERE status != "Archived"
SORT quarterly_goals[0], project_progress DESC
```

### Projects → Tasks
```dataview
TABLE WITHOUT ID
  projects[0] as "Project",
  file.link as "Task",
  status as "Status",
  priority as "Priority"
FROM "16-Tasks"
WHERE status != "Done"
SORT projects[0], priority DESC
```

---

## 📅 Temporal Hierarchy

### Year → Quarters → Months → Weeks → Days

#### Current Year Overview
```dataview
TABLE WITHOUT ID
  file.link as "Quarter",
  count(rows) as "Monthly Reviews",
  sum(rows.goal_progress) / count(rows) as "Avg Progress"
FROM "Reviews/Quarters"
WHERE contains(string(year), "<% tp.date.now('YYYY') %>")
SORT file.name DESC
```

#### Current Quarter Overview
```dataview
TABLE WITHOUT ID
  file.link as "Month",
  count(rows) as "Weekly Reviews",
  choice(length(month_synthesis) > 0, "✅", "⏳") as "Synthesized"
FROM "Reviews/Months"
WHERE contains(string(quarters), "<% tp.date.now('YYYY-[Q]Q') %>")
SORT file.name DESC
```

#### Current Month Overview
```dataview
TABLE WITHOUT ID
  file.link as "Week",
  choice(length(day_synthesis) > 0, "✅", "⏳") as "Days Synthesized"
FROM "Reviews/Weeks"
WHERE contains(string(months), "<% tp.date.now('YYYY-MM') %>")
SORT file.name DESC
```

#### Current Week Overview
```dataview
TABLE WITHOUT ID
  file.link as "Day",
  choice(length(day_synthesis) > 0, "✅", "⏳") as "Synthesized",
  choice(length(night_wind_down) > 0, "✅", "⏳") as "Reflected"
FROM "Reviews/Days"
WHERE contains(string(weeks), "<% tp.date.now('YYYY-[W]WW') %>")
SORT date DESC
```

---

## 🧠 Atomic Log Rollup

### Subjective Journal → Daily Reviews
```dataview
TABLE WITHOUT ID
  file.link as "Day",
  count(rows) as "Subjective Entries",
  join(rows.primary_emotion, ", ") as "Emotions"
FROM "Reviews/Days"
WHERE date >= date(today) - dur(7 days)
FLATTEN file.lists as L
WHERE L.primary_emotion
GROUP BY file.link
SORT date DESC
```

### Relational Journal → Daily Reviews
```dataview
TABLE WITHOUT ID
  file.link as "Day",
  count(rows) as "Relational Entries",
  join(rows.people, ", ") as "People"
FROM "Reviews/Days"
WHERE date >= date(today) - dur(7 days)
FLATTEN file.lists as L
WHERE L.people
GROUP BY file.link
SORT date DESC
```

### Activity Log → Daily Reviews
```dataview
TABLE WITHOUT ID
  file.link as "Day",
  count(rows) as "Activities",
  sum(rows.duration) as "Total Duration"
FROM "Reviews/Days"
WHERE date >= date(today) - dur(7 days)
FLATTEN file.lists as L
WHERE L.duration
GROUP BY file.link
SORT date DESC
```

### Systemic Journal → All Levels
```dataview
TABLE WITHOUT ID
  file.link as "Issue",
  impact as "Impact",
  status as "Status",
  "⚠️ " + impact as "Priority"
FROM "03-Systemic-Journal"
WHERE impact >= 7
SORT impact DESC
LIMIT 10
```

---

## 🔗 Cross-System Intelligence

### Tasks Across Strategic Levels
```dataview
TABLE WITHOUT ID
  file.link as "Task",
  status as "Status",
  priority as "Priority",
  join(annual_goals, ", ") as "Annual Goals",
  join(quarterly_goals, ", ") as "Quarterly Goals",
  join(projects, ", ") as "Projects"
FROM "16-Tasks"
WHERE status != "Done" AND (length(annual_goals) > 0 OR length(quarterly_goals) > 0 OR length(projects) > 0)
SORT priority DESC
LIMIT 15
```

### Systemic Issues by Strategic Impact
```dataview
TABLE WITHOUT ID
  file.link as "Issue",
  impact as "Impact",
  join(annual_goals, ", ") as "Annual Goals",
  join(projects, ", ") as "Projects",
  status as "Status"
FROM "03-Systemic-Journal"
WHERE impact >= 5
SORT impact DESC
LIMIT 10
```

---

## 📊 System Health Metrics

### Completion Rates by Level
```dataview
LIST
  "Annual Goals: " + round(sum(choice(status = "Completed", 1, 0)) / count * 100) + "%"
FROM "Strategy/AnnualGoals"
WHERE status != "Archived"
```

```dataview
LIST
  "Quarterly Goals: " + round(sum(choice(status = "Completed", 1, 0)) / count * 100) + "%"
FROM "Strategy/QuarterlyGoals"
WHERE status != "Archived"
```

```dataview
LIST
  "Projects: " + round(sum(choice(status = "Completed", 1, 0)) / count * 100) + "%"
FROM "Projects"
WHERE status != "Archived"
```

```dataview
LIST
  "Tasks: " + round(sum(choice(status = "Done", 1, 0)) / count * 100) + "%"
FROM "16-Tasks"
```

---

## 🎯 Quick Navigation

- **Strategic Level**: [[Vision]] → [[Annual Goals]] → [[Quarterly Goals]] → [[Projects]] → [[Tasks]]
- **Temporal Level**: [[Year Review]] → [[Quarterly Review]] → [[Monthly Review]] → [[Weekly Review]] → [[Daily Note]]
- **Atomic Logs**: [[Subjective Journal]] → [[Relational Journal]] → [[Systemic Journal]] → [[Activity Log]] → [[Diet Log]]

---

*Dashboard Generated: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
