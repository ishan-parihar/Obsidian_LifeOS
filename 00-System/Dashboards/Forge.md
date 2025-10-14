---
dashboard_type: forge
created: 2025-10-14
---
# The Forge

> **Execution Engine** - Project and task management hub

## 🏗️ Active Projects

```datacorejsx
const COLUMNS = [
  { id: "Project", value: row => row.$link },
  { id: "Status", value: row => row.value("status") },
  { id: "Priority", value: row => row.value("priority") },
  { id: "Progress", value: row => row.value("project_progress") + "%" },
  { id: "Deadline", value: row => row.value("deadline")?.toLocaleDateString() }
];

return function View() {
  const projects = dc.useQuery('@page and "15-Projects" and status = "Active"');
  const sortedProjects = dc.useArray(projects, array => 
    array.sort((a, b) => {
      const priorityA = parseInt(a.value("priority")?.match(/⭐/g)?.length || 0);
      const priorityB = parseInt(b.value("priority")?.match(/⭐/g)?.length || 0);
      if (priorityA !== priorityB) return priorityB - priorityA;
      
      const deadlineA = a.value("deadline")?.getTime() || Infinity;
      const deadlineB = b.value("deadline")?.getTime() || Infinity;
      return deadlineA - deadlineB;
    })
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedProjects} />;
}
```

## 🚀 Current Sprint

**Sprint Period**: <% tp.date.now("YYYY-MM-DD", 0, -tp.date.now().weekday) %> - <% tp.date.now("YYYY-MM-DD", 6, -tp.date.now().weekday) %>

### Sprint Tasks

```datacorejsx
return function View() {
  const tasks = dc.useQuery('@task');
  const sprintTasks = dc.useArray(tasks, array => 
    array.filter(task => {
      const text = task.$text || "";
      return text.includes('#sprint/current') && !task.completed;
    })
  );
  
  const grouped = sprintTasks.reduce((acc, task) => {
    const file = task.$file;
    if (!acc[file]) acc[file] = { file, tasks: [] };
    acc[file].tasks.push(task);
    return acc;
  }, {});
  
  return (
    <div>
      {Object.values(grouped).map(group => (
        <div key={group.file}>
          <strong>{group.file}</strong>
          <ul>
            {group.tasks.map((task, i) => (
              <li key={i}>{task.$text}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}
```

### Sprint Backlog

```datacorejsx
return function View() {
  const tasks = dc.useQuery('@task');
  const backlogTasks = dc.useArray(tasks, array => 
    array.filter(task => {
      const text = task.$text || "";
      return text.includes('#sprint/backlog') && !task.completed;
    }).slice(0, 10)
  );
  
  return (
    <ul>
      {backlogTasks.map((task, i) => (
        <li key={i}>{task.$text}</li>
      ))}
    </ul>
  );
}
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
