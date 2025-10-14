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
hierarchy_level: strategic
parent_entities: []
child_entities: []
sibling_entities: []
related_time_periods: []
strategic_alignment: []
strategic_hierarchy:
  vision: []
  annual_goals: []
  quarterly_goals: []
  projects: []
  tasks: []
execution_status:
  progress: 0
  health: ""
  next_milestone: ""
  blockers: []
vision: []
quarters: []
quarterly_goals: []
projects: []
tasks: []
primary_metric: []
current_annual_goal:
goal_progress: 0
planned_range:
entity_type: "annual-goal"
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

```datacorejsx
const COLUMNS = [
  { id: "Quarterly Goal", value: row => row.$link },
  { id: "Status", value: row => row.value("status") },
  { id: "Progress", value: row => row.value("goal_progress") }
];

return function View() {
  const goals = dc.useQuery(`@page and "14-Quarterly-Goals" and annual_goals = "<% tp.file.title %>"`);
  const sortedGoals = dc.useArray(goals, array => 
    array.sort(row => row.$name)
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedGoals} />;
}
```

### Supporting Projects

```datacorejsx
const COLUMNS = [
  { id: "Project", value: row => row.$link },
  { id: "Status", value: row => row.value("project_status") },
  { id: "Progress", value: row => row.value("project_progress") }
];

return function View() {
  const projects = dc.useQuery(`@page and "15-Projects" and annual_goals = "<% tp.file.title %>"`);
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
  const tasks = dc.useQuery(`@page and "16-Tasks" and annual_goals = "<% tp.file.title %>"`);
  const sortedTasks = dc.useArray(tasks, array =>
    array.sort(row => row.value("task_priority"))
  );

  return <dc.VanillaTable columns={COLUMNS} rows={sortedTasks} />;
}
```

---

*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
