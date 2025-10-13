```dataview
dv.header(1, "The Forge - Execution Center");

// Current Sprint
dv.header(2, "Current Sprint Tasks");
dv.taskList(
  dv.pages('"Projects"')
    .file.tasks
    .where(t => !t.completed && t.text.includes("#sprint/current"))
    .sort(t => t.priority, 'desc')
);

// Upcoming Tasks
dv.header(2, "Next 4 Sprints");
dv.taskList(
  dv.pages('"Projects"')
    .file.tasks
    .where(t => !t.completed && t.text.includes("#sprint/next"))
    .sort(t => t.priority, 'desc')
);

// Backlog
dv.header(2, "Backlog");
dv.taskList(
  dv.pages('"Projects"')
    .file.tasks
    .where(t => !t.completed && (t.text.includes("#sprint/backlog") || !t.text.includes("#sprint")))
    .sort(t => t.priority, 'desc')
    .limit(20)
);
```