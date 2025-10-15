---
title: ""
description: ""
task_status: Waiting
task_priority: ⭐⭐⭐
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
parent_entities: "[] # Projects"
child_entities: "[] # Subtasks"
sibling_entities: "[] # Other Tasks in Project"
related_time_periods: []
strategic_alignment: []
strategic_hierarchy: "{"
  vision: "[],"
  annual_goals: "[],"
  quarterly_goals: "[],"
  projects: "[],"
  tasks: "[] # Dependencies"
}
execution_status: "{"
  progress: 0,
  health: "",
  next_milestone: "",
  blockers: []
}
context: "{"
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
task_type: ""
task_energy_required: ""
task_cognitive_load: ""
entity_hierarchy_level: "strategic"
entity_type: "task"
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.file.title %>

## 📋 Task Overview

**Priority**: <% tp.frontmatter.task_priority %>
**Status**: <% tp.frontmatter.task_status %>
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

**Current Status**: <% tp.frontmatter.task_status %>
**Time Invested**: 0 hours
**Next Action**: 

## 🔗 Related Items

### Related Tasks
```datacorejsx
const COLUMNS = [
  { id: "Task", value: row => row.$link },
  { id: "Status", value: row => row.value("task_status") },
  { id: "Priority", value: row => row.value("task_priority") }
];

return function View() {
  const currentFile = "{{TITLE}}"; // Placeholder for tp.file.title
  const tasks = dc.useQuery(`@page and "16-Tasks" and file != "${currentFile}"`);
  const relatedTasks = tasks.filter(task => {
    const taskProjects = task.value("projects") || [];
    const taskQuarterlyGoals = task.value("quarterly_goals") || [];
    const taskAnnualGoals = task.value("annual_goals") || [];
    // Using empty arrays to prevent errors when opened as templates
    const thisProjects = [];
    const thisQuarterlyGoals = [];
    const thisAnnualGoals = [];

    return (
      taskProjects.some(p => thisProjects.includes(p)) ||
      taskQuarterlyGoals.some(qg => thisQuarterlyGoals.includes(qg)) ||
      taskAnnualGoals.some(ag => thisAnnualGoals.includes(ag))
    );
  });

  const sortedTasks = dc.useArray(relatedTasks, array =>
    array.sort(row => row.value("task_priority"))
  );

  return <dc.VanillaTable columns={COLUMNS} rows={sortedTasks} />;
}
```

### Systemic Issues
```datacorejsx
const COLUMNS = [
  { id: "Issue", value: row => row.$link },
  { id: "Impact", value: row => row.value("impact") },
  { id: "Status", value: row => row.value("status") }
];

return function View() {
  const issues = dc.useQuery(`@page and "03-Systemic-Journal" and projects = "{{TITLE}}"`); // Placeholder for tp.file.title
  const sortedIssues = dc.useArray(issues, array => 
    array.sort(row => row.value("impact"))
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedIssues} />;
}
```

## 📝 Notes & Context

### Context

### Energy Requirements

### Cognitive Load

---

*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
