```dataview
// Today's Context
const today = dv.date("today");
const todayNote = dv.page(`Reviews/Days/${today.toFormat("yyyy-MM-dd")}`);

dv.header(1, "The Workbench");
dv.header(2, "Today: " + today.toFormat("EEEE, MMMM d, yyyy"));

// Current Sprint Tasks
dv.header(3, "Current Sprint");
dv.taskList(
  dv.pages('"Projects"')
    .file.tasks
    .where(t => !t.completed && t.text.includes("#sprint/current"))
    .sort(t => t.priority, 'desc')
);

// Active Systemic Issues
dv.header(3, "Active Systemic Dissonances");
dv.table(
  ["Issue", "Impact", "Status"],
  dv.pages('"Logs/Systemic"')
    .where(p => p.status === "Triage" || p.status === "Escalated")
    .sort(p => p.impact, 'desc')
    .limit(5)
    .map(p => [p.file.link, p.impact, p.status])
);

// Upcoming Reconnections
dv.header(3, "People to Reconnect With");
const reconnectSoon = dv.pages('"People"')
  .where(p => p.reconnect_by && p.reconnect_by <= today.plus({days: 7}))
  .sort(p => p.reconnect_by, 'asc')
  .limit(5);

dv.table(
  ["Person", "Reconnect By", "Trajectory"],
  reconnectSoon.map(p => [p.file.link, p.reconnect_by, p.desired_trajectory])
);
```