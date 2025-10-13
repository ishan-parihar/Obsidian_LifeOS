# Forge Dashboard Blueprint

## Overview
The Forge is the immediate tactical operationality of Tasks and Project Management. It's where execution happens at the task and project level.

## Data Flow
```
STRATEGIC GOALS → PROJECTS → TASKS → EXECUTION
```

## Implementation

### Folder Structure
- `/000-System/Dashboards/Forge.md`

### Required Plugins
- Dataview
- Tasks
- Buttons

### Critical Dataview Queries

```javascript
// Current Active Projects
dv.header(2, "Active Projects");
dv.table(
  ["Project", "Priority", "Progress", "Deadline"],
  dv.pages('"Projects"')
    .where(p => p.status === "Active")
    .sort(p => p.priority, 'desc')
    .map(p => [p.file.link, p.priority, p.project_progress, p.deadline])
);

// Current Sprint Tasks
dv.header(3, "Current Sprint Tasks");
dv.taskList(
  dv.pages('"Projects"')
    .file.tasks
    .where(t => !t.completed && t.text.includes("#sprint/current"))
    .sort(t => t.priority, 'desc')
);

// Next Sprint Tasks
dv.header(3, "Next Sprint Tasks");
dv.taskList(
  dv.pages('"Projects"')
    .file.tasks
    .where(t => !t.completed && t.text.includes("#sprint/next"))
    .sort(t => t.priority, 'desc')
);

// Backlog Tasks
dv.header(3, "Backlog Tasks");
dv.taskList(
  dv.pages('"Projects"')
    .file.tasks
    .where(t => !t.completed && t.text.includes("#sprint/backlog"))
    .sort(t => t.priority, 'desc')
);
```

### Button-Based Sprint Management

```markdown
# Project: [Project Name]

## Tasks
- [ ] Task 1 #priority/⭐⭐⭐⭐⭐ #sprint/backlog
- [ ] Task 2 #priority/⭐⭐⭐⭐ #sprint/current
- [ ] Task 3 #priority/⭐⭐⭐ #sprint/next1

```button
name Move to Current Sprint
type command
action QuickAdd: Move Task to Current Sprint
```

```button
name Move to Next Sprint
type command
action QuickAdd: Move Task to Next Sprint
```
```
