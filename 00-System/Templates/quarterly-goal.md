---
title: ""
key_result_1: ""
key_result_2: ""
key_result_3: ""
key_learning: ""
status: Planning
hierarchy_level: "strategic"
parent_entities: "[] # Annual Goals"
child_entities: "[] # Projects"
sibling_entities: "[] # Other Quarterly Goals"
related_time_periods: []
strategic_alignment: []
strategic_hierarchy: "{"
  vision: "[],"
  annual_goals: "[],"
  quarterly_goals: "[],"
  projects: "[],"
  tasks: []
}
execution_status: "{"
  progress: 0,
  health: "",
  next_milestone: "",
  blockers: []
}
annual_goals: []
quarters: []
years: []
projects: []
tasks: []
failure_scenarios: []
current_quarter_goal: ""
goal_progress: 0
health: ""
entity_type: "quarterly-goal"
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

```datacorejsx
const COLUMNS = [
  { id: "Project", value: row => row.$link },
  { id: "Status", value: row => row.value("project_status") },
  { id: "Progress", value: row => row.value("project_progress") }
];

return function View() {
  const projects = dc.useQuery(`@page and "15-Projects" and quarterly_goals = "{{TITLE}}"`); // Placeholder for tp.file.title
  const sortedProjects = dc.useArray(projects, array =>
    array.sort(row => row.value("project_progress"))
  );

  return <dc.VanillaTable columns={COLUMNS} rows={sortedProjects} />;
}
```

### Task Rollup

```datacorejsx
const COLUMNS = [
  { id: "Task", value: row => row.$link },
  { id: "Status", value: row => row.value("task_status") },
  { id: "Priority", value: row => row.value("task_priority") }
];

return function View() {
  const tasks = dc.useQuery(`@page and "16-Tasks" and quarterly_goals = "{{TITLE}}"`); // Placeholder for tp.file.title
  const sortedTasks = dc.useArray(tasks, array =>
    array.sort(row => row.value("task_priority"))
  );

  return <dc.VanillaTable columns={COLUMNS} rows={sortedTasks} />;
}
```

## ⚠️ Risk Management

```datacorejsx
const COLUMNS = [
  { id: "Risk", value: row => row.$link },
  { id: "Impact", value: row => row.value("impact") },
  { id: "Likelihood", value: row => row.value("likelihood") },
  { id: "Status", value: row => row.value("status") }
];

return function View() {
  const risks = dc.useQuery(`@page and "24-Failure-Scenarios" and quarterly_goals = "{{TITLE}}"`); // Placeholder for tp.file.title
  const sortedRisks = dc.useArray(risks, array => 
    array.sort(row => row.value("impact"))
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedRisks} />;
}
```

---

*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
