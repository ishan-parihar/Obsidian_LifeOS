```dataview
// Weekly Synthesis Rollup
const weekNum = `W${moment().isoWeek()}`;
const week = dv.page(`Reviews/Weeks/${moment().format('YYYY')}-${weekNum}`);

dv.header(2, `Week ${moment().format('YYYY')}-${weekNum} Review`);

// Aggregate all days in this week
const days = dv.pages('"Reviews/Days"')
  .where(p => p.weeks && p.weeks.includes(week.file.link))
  .sort(p => p.file.name, 'asc');

dv.header(3, "Daily Syntheses");
for (let day of days) {
  dv.header(4, day.file.name);
  dv.paragraph(day.day_synthesis || "No synthesis available");
}

// Task completion rate
const tasksThisWeek = dv.pages('"Projects"')
  .file.tasks
  .where(t => t.weeks && t.weeks.includes(week.file.link));

const completed = tasksThisWeek.where(t => t.completed).length;
const total = tasksThisWeek.length;

dv.paragraph(`**Task Completion**: ${completed}/${total} (${Math.round(completed/total*100)}%)`);
```

## Strategic Alignment
```dataview
// Show current Annual Goal → Quarterly Goal → Projects → Tasks hierarchy
const currentYear = dv.date("today").year;
const currentQuarter = `${currentYear}-Q${Math.ceil(dv.date("today").month / 3)}`;

// Annual Goals
const annualGoals = dv.pages('"Strategy/AnnualGoals"')
  .where(p => p.status === "Active" && p.years.includes(String(currentYear)));

for (let goal of annualGoals) {
  dv.header(3, "🎯 " + goal.title);

  // Quarterly Goals under this annual goal
  const qGoals = dv.pages('"Strategy/QuarterlyGoals"')
    .where(p => p.annual_goals && p.annual_goals.includes(goal.file.link)
                && p.quarters.includes(currentQuarter));

  for (let qGoal of qGoals) {
    dv.header(4, "📊 " + qGoal.title);
    dv.paragraph(`**KR1**: ${qGoal.key_result_1}`);
    dv.paragraph(`**KR2**: ${qGoal.key_result_2}`);
    dv.paragraph(`**KR3**: ${qGoal.key_result_3}`);

    // Projects under this quarterly goal
    const projects = dv.pages('"Projects"')
      .where(p => p.quarterly_goals && p.quarterly_goals.includes(qGoal.file.link)
                  && p.status === "Active");

    if (projects.length > 0) {
      dv.header(5, "Active Projects:");
      dv.list(projects.map(p => p.file.link + " (" + p.status + ")"));
    }
  }
}
```