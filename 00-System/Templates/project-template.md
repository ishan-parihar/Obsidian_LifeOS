---
title: ""
project_summary: ""
project_priority: ⭐⭐⭐
project_status: On-Hold
project_start: ""
project_deadline: ""
project_review_date: ""
entity_hierarchy_level: "strategic"
entity_type: "project"
project_quarterly_goals: []
project_annual_goals: []
project_quarters: []
project_years: []
project_tasks: []
project_people: []
project_notes: []
project_documents: []
project_competencies: []
project_systemic_journal: []
project_hard_constraints_antigoals: ""
project_kpis: ""
project_kpi_bar: 0
project_progress: 0
project_health: ""
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.file.title %>

## 📋 Project Overview

**Priority**: <% tp.frontmatter.project_priority %>
**Status**: <% tp.frontmatter.project_status %>
**Progress**: 0%

### Project Summary

## 🎯 Strategic Alignment

**Quarterly Goals**: 
**Annual Goals**: 
**Vision Connection**: 

## 📊 Success Metrics

### KPIs

### Hard Constraints (Anti-Goals)

## 🚀 Execution Plan

### Phase 1
- [ ] 
- [ ] 
- [ ] 

### Phase 2
- [ ] 
- [ ] 
- [ ] 

### Phase 3
- [ ] 
- [ ] 
- [ ] 

## 📋 Active Tasks

```datacorejsx
const COLUMNS = [
  { id: "Task", value: row => row.$link },
  { id: "Status", value: row => row.value("task_status") },
  { id: "Priority", value: row => row.value("task_priority") }
];

return function View() {
  const tasks = dc.useQuery(`@page and "16-Tasks" and projects = "<% tp.file.title %>" and task_status != "Done"`);
  const sortedTasks = dc.useArray(tasks, array =>
    array.sort(row => row.value("task_priority"))
  );

  return <dc.VanillaTable columns={COLUMNS} rows={sortedTasks} />;
}
```

## 📈 Progress Tracking

**Current Progress**: 0%
**Next Milestone**: 

## 🤝 Resources

**People Involved**: 
**Key Documents**: 
**Required Competencies**: 

## ⚠️ Systemic Issues

```datacorejsx
const COLUMNS = [
  { id: "Issue", value: row => row.$link },
  { id: "Impact", value: row => row.value("impact") },
  { id: "Status", value: row => row.value("status") }
];

return function View() {
  const issues = dc.useQuery(`@page and "03-Systemic-Journal" and projects = "<% tp.file.title %>"`);
  const sortedIssues = dc.useArray(issues, array => 
    array.sort(row => row.value("impact"))
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedIssues} />;
}
```

---

*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
