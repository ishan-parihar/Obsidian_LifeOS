# Observatory Dashboard Blueprint

## Overview
The Observatory is the long-term strategic planning and review dashboard that helps review, plan and analyze the review-systems (Days, Weeks, Months, Quarters and Years) with the operational-systems (Values & Principles, Vision, Annual Goals, Quarterly Goals, Projects and Tasks) and Atomic Capture Points.

## Data Flow
```
DAILY SYNTHESIS → WEEKLY/MONTHLY/QUARTERLY/YEARLY REVIEWS → STRATEGIC ALIGNMENT
```

## Implementation

### Folder Structure
- `/000-System/Dashboards/Observatory.md`

### Required Plugins
- Dataview
- Templater

### Critical Dataview Queries

```javascript
// Weekly Synthesis Rollup
const weekNum = "25-W41"; // parameterize
const week = dv.page(`Reviews/Weeks/${weekNum}`);

dv.header(2, `Week ${weekNum} Review`);

// Aggregate all days in this week
const days = dv.pages('"Reviews/Days"')
  .where(p => p.weeks && p.weeks.includes(weekNum))
  .sort(p => p.file.name, 'asc');

dv.header(3, "Daily Syntheses");
for (let day of days) {
  dv.header(4, day.file.name);
  dv.paragraph(day.day_synthesis);
}

// Task completion rate
const tasksThisWeek = dv.pages('"Projects"')
  .file.tasks
  .where(t => t.weeks && t.weeks.includes(weekNum));
  
const completed = tasksThisWeek.where(t => t.completed).length;
const total = tasksThisWeek.length;

dv.paragraph(`**Task Completion**: ${completed}/${total} (${Math.round(completed/total*100)}%)`);

// Strategic Alignment Check
const currentYear = dv.date("today").year;
const currentQuarter = `${currentYear}-Q${Math.ceil(dv.date("today").month / 3)}`;

dv.header(2, "Strategic Alignment");

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
