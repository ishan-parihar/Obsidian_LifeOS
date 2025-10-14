---
title: 
key_result_1: 
key_result_2: 
key_result_3: 
key_learning: 
status: Planning
annual_goals: []
quarters: []
years: []
projects: []
tasks: []
failure_scenarios: []
current_quarter_goal: 
goal_progress: 0
health: 
type: quarterly-goal
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.file.title %>

## 🎯 OKR Framework

**Status**: 
**Progress**: 0%
**Health**: 

### Objective

## 📊 Key Results

### KR1

### KR2

### KR3

## 🧠 Key Learning

## 🔗 Strategic Alignment

**Annual Goal**: 
**Vision Connection**: 

## 📈 Supporting Projects

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  project_progress as "Progress"
FROM "Projects"
WHERE contains(string(quarterly_goals), string("<% tp.file.title %>"))
SORT project_progress DESC
```

### Task Rollup

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  status as "Status",
  priority as "Priority"
FROM "16-Tasks"
WHERE contains(string(quarterly_goals), string("<% tp.file.title %>"))
SORT priority DESC
```

## ⚠️ Risk Management

```dataview
TABLE WITHOUT ID
  file.link as "Risk",
  impact as "Impact",
  likelihood as "Likelihood",
  status as "Status"
FROM "Strategy/FailureScenarios"
WHERE contains(string(quarterly_goals), string("<% tp.file.title %>"))
SORT impact DESC
```

---

*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
