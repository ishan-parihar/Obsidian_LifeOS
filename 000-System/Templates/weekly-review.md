---
title: <% moment(tp.date.now('YYYY-MM-DD')).format('YYYY-[W]WW') %>
week_number: <% moment(tp.date.now('YYYY-MM-DD')).format('W') %>
year: <% moment(tp.date.now('YYYY-MM-DD')).format('YYYY') %>
week_start_date: <% moment(tp.date.now('YYYY-MM-DD')).startOf('isoWeek').format('YYYY-MM-DD') %>
week_end_date: <% moment(tp.date.now('YYYY-MM-DD')).endOf('isoWeek').format('YYYY-MM-DD') %>
status: Active
---

# Week <% moment(tp.date.now('YYYY-MM-DD')).format('YYYY-[W]WW') %> Review

## Week Synthesis

## Key Insights

## Wins

## Challenges

## Lessons Learned

## Task Completion Rate
```dataview
const tasksThisWeek = dv.pages('"Projects"').file.tasks
  .where(t => t.weeks && t.weeks.includes(file.name));
const completed = tasksThisWeek.where(t => t.completed).length;
const total = tasksThisWeek.length;
const percentage = total > 0 ? Math.round(completed/total*100) : 0;
dv.paragraph(`**Task Completion**: ${completed}/${total} (${percentage}%)`);
```

## Daily Syntheses
```dataview
LIST
FROM "Reviews/Days"
WHERE week = this.file.link
SORT file.name ASC
```

## Next Week's Plan