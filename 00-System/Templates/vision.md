---
vision_statement: 
guiding_question: 
strategic_pillars: []
priority: ⭐⭐⭐
status: Planning
review_date: 
last_review_date: 
hierarchy_level: "strategic"
parent_entities: [] # None (top level)
child_entities: [] # Annual Goals
sibling_entities: [] # Other Vision statements
related_time_periods: []
strategic_alignment: []
strategic_hierarchy: {
  vision: [],
  annual_goals: [],
  quarterly_goals: [], 
  projects: [],
  tasks: []
}
execution_status: {
  progress: 0,
  health: "",
  next_milestone: "",
  blockers: []
}
life_aspects: []
values: []
annual_goals: []
quarterly_goals: []
entity_type: "vision"
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.file.title %>

## 👁️ Vision Statement

## 🎯 Guiding Question

## 🏛️ Strategic Pillars

## 📊 Priority & Status

**Priority**: 
**Status**: 

**Next Review**: 
**Last Reviewed**: 

## 🔗 Strategic Alignment

**Life Aspects**: 
**Core Values**: 

## 📈 Manifestation

### Annual Goals

```datacorejsx
const COLUMNS = [
  { id: "Annual Goal", value: row => row.$link },
  { id: "Status", value: row => row.value("status") },
  { id: "Progress", value: row => row.value("goal_progress") }
];

return function View() {
  const goals = dc.useQuery(`@page and "13-Annual-Goals" and vision = "<% tp.file.title %>"`);
  const sortedGoals = dc.useArray(goals, array => 
    array.sort(row => row.value("goal_progress"))
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedGoals} />;
}
```

### Quarterly Progress

```datacorejsx
return function View() {
  const quarterlyGoals = dc.useQuery(`@page and "14-Quarterly-Goals" and vision = "<% tp.file.title %>"`);
  
  const total = quarterlyGoals.length;
  const completed = quarterlyGoals.filter(goal => goal.value("status") === "Done").length;
  const percentage = total > 0 ? Math.round((completed / total) * 100) : 0;
  
  return (
    <table>
      <thead>
        <tr>
          <th>Q-Goals</th>
          <th>Completed</th>
          <th>%</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{total}</td>
          <td>{completed}</td>
          <td>{percentage}</td>
        </tr>
      </tbody>
    </table>
  );
}
```

## 🧼 Vision Review

### What's Working

### What Needs Adjustment

### Emerging Insights

---

*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
