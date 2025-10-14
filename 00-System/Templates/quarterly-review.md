---
title: <% tp.date.now("YYYY-[Q]Q") %> Review
quarter_number: <% tp.date.now("[Q]Q") %>
year: <% tp.date.now("YYYY") %>
time_period_start: <% tp.date.now("YYYY-MM-DD", 0, -tp.date.now().quarter + 1) %>
time_period_end: <% tp.date.now("YYYY-MM-DD", 0, -tp.date.now().quarter + 1 + 90) %>
containing_period: [[<% tp.date.now("YYYY") %>]]
contained_periods: [] # Auto-populated with months
parallel_periods: [] # Other quarters in same year
hierarchy_level: "review"
parent_entities: [] # Years
child_entities: [] # Months
sibling_entities: [] # Other quarters in year
related_time_periods: []
strategic_alignment: []
years: [[<% tp.date.now("YYYY") %>]]
months: []
weeks: []
days: []
type: quarterly-review
status: Active
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.date.now("YYYY [Q]Q") %> Review

**Date Range**: <% tp.date.now("YYYY-MM-DD", 0, -tp.date.now().quarter + 1) %> - <% tp.date.now("YYYY-MM-DD", 0, -tp.date.now().quarter + 1 + 90) %>

---

## 🧠 Intelligence Synthesis

### Quarter Synthesis

### The Witness
*Quarterly Awareness and Observation*

### The Logos Inquisitor
*Quarterly Rational Analysis*

### The Alpha Scanner
*Quarterly Opportunities and Threats*

### The Structural Integrator
*Quarterly Systems Thinking*

### The Ascension Architect
*Quarterly Growth and Development*

### The Mythopoetic Weaver
*Quarterly Narrative and Meaning*

### The Somatic Arbiter
*Quarterly Body Wisdom*

### The State-Hacker
*Quarterly Consciousness States*

### The Capital Strategist
*Quarterly Financial Intelligence*

### The Hearth Tender
*Quarterly Home and Family Dynamics*

### The Network Weaver
*Quarterly Relationship Intelligence*

### The Stillness Warden
*Quarterly Peace and Rest*

### The Aesthetic Calibrator
*Quarterly Beauty and Design*

### The Legacy Tender
*Quarterly Long-term Impact*

### The Systemic Navigator
*Quarterly Operational Intelligence*

---

## 🎯 Meta-Synthesis

### Quarter Oracle Synthesis
*Quarterly Wisdom Perspective*

### Quarter Phoenix Synthesis
*Quarterly Transformation Perspective*

### Quarter Sovereign Synthesis
*Quarterly Power and Agency*

---

## 📊 Quarterly Metrics

### Monthly Summaries
```datacorejsx
const COLUMNS = [
  { id: "Month", value: row => row.$link },
  { id: "Synthesized", value: row => row.value("month_synthesis") ? "✅" : "⏳" }
];

return function View() {
  const months = dc.useQuery(`@page and "08-Months" and quarters = "<% tp.file.title %>"`);
  const sortedMonths = dc.useArray(months, array => 
    array.sort(row => row.$name).reverse()
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedMonths} />;
}
```

### Goal Progress
```datacorejsx
const COLUMNS = [
  { id: "Quarterly Goal", value: row => row.$link },
  { id: "Status", value: row => row.value("status") },
  { id: "Progress", value: row => row.value("goal_progress") }
];

return function View() {
  const goals = dc.useQuery(`@page and "14-Quarterly-Goals" and quarters = "<% tp.file.title %>"`);
  const sortedGoals = dc.useArray(goals, array => 
    array.sort(row => row.value("goal_progress")).reverse()
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedGoals} />;
}
```

### Task Completion
```datacorejsx
return function View() {
  const tasks = dc.useQuery(`@page and "16-Tasks" and quarters = "<% tp.file.title %>"`);
  
  const total = tasks.length;
  const completed = tasks.filter(task => task.value("completed")).length;
  const percentage = total > 0 ? Math.round((completed / total) * 100) : 0;
  
  return (
    <table>
      <thead>
        <tr>
          <th>Total</th>
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

### Financial Summary
```datacorejsx
return function View() {
  const financialLogs = dc.useQuery(`@page and "Financial Log" and quarters = "<% tp.file.title %>"`);
  
  const income = financialLogs.reduce((sum, log) => sum + (log.value("Total_Income") || 0), 0);
  const expenses = financialLogs.reduce((sum, log) => sum + (log.value("Total_Expenses") || 0), 0);
  const net = financialLogs.reduce((sum, log) => sum + (log.value("Net_Cashflow") || 0), 0);
  
  return (
    <table>
      <thead>
        <tr>
          <th>Income</th>
          <th>Expenses</th>
          <th>Net</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{income}</td>
          <td>{expenses}</td>
          <td>{net}</td>
        </tr>
      </tbody>
    </table>
  );
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
  const issues = dc.useQuery(`@page and "03-Systemic-Journal" and date >= "<% tp.frontmatter.time_period_start %>" and date <= "<% tp.frontmatter.time_period_end %>"`);
  const sortedIssues = dc.useArray(issues, array => 
    array.sort(row => row.value("impact")).reverse()
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedIssues} />;
}
```

---

## 🎭 Quarterly Reflection

### Key Learnings

**What did I learn this quarter?**

### Wins

**What went well?**

### Challenges

**What were the obstacles?**

### Pattern Recognition

**What patterns do I notice?**

### Next Quarter Focus

**What needs attention next quarter?**

---

## 🚀 Next Quarter Planning

**Primary Focus Areas**

---

*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*