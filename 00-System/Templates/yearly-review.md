---
title: <% tp.date.now("YYYY") %> Year Review
year: <% tp.date.now("YYYY") %>
time_period_start: <% tp.date.now("YYYY-01-01") %>
time_period_end: <% tp.date.now("YYYY-12-31") %>
containing_period: ""
contained_periods: [] # Auto-populated with quarters
parallel_periods: [] # Other years
hierarchy_level: "review"
parent_entities: [] # None (top level)
child_entities: [] # Quarters
sibling_entities: [] # Other years
related_time_periods: []
strategic_alignment: []
quarters: []
months: []
weeks: []
days: []
type: yearly-review
status: Active
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.date.now("YYYY") %> Year Review

**Date Range**: <% tp.date.now("YYYY-01-01") %> - <% tp.date.now("YYYY-12-31") %>

---

## 🧠 Intelligence Synthesis

### Year Synthesis

### The Witness
*Yearly Awareness and Observation*

### The Logos Inquisitor
*Yearly Rational Analysis*

### The Alpha Scanner
*Yearly Opportunities and Threats*

### The Structural Integrator
*Yearly Systems Thinking*

### The Ascension Architect
*Yearly Growth and Development*

### The Mythopoetic Weaver
*Yearly Narrative and Meaning*

### The Somatic Arbiter
*Yearly Body Wisdom*

### The State-Hacker
*Yearly Consciousness States*

### The Capital Strategist
*Yearly Financial Intelligence*

### The Hearth Tender
*Yearly Home and Family Dynamics*

### The Network Weaver
*Yearly Relationship Intelligence*

### The Stillness Warden
*Yearly Peace and Rest*

### The Aesthetic Calibrator
*Yearly Beauty and Design*

### The Legacy Tender
*Yearly Long-term Impact*

### The Systemic Navigator
*Yearly Operational Intelligence*

---

## 🎯 Meta-Synthesis

### Year Oracle Synthesis
*Yearly Wisdom Perspective*

### Year Phoenix Synthesis
*Yearly Transformation Perspective*

### Year Sovereign Synthesis
*Yearly Power and Agency*

---

## 📊 Yearly Metrics

### Quarterly Summaries
```datacorejsx
const COLUMNS = [
  { id: "Quarter", value: row => row.$link },
  { id: "Synthesized", value: row => row.value("quarter_synthesis") ? "✅" : "⏳" }
];

return function View() {
  const quarters = dc.useQuery(`@page and "09-Quarters" and years = "<% tp.file.title %>"`);
  const sortedQuarters = dc.useArray(quarters, array => 
    array.sort(row => row.$name).reverse()
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedQuarters} />;
}
```

### Annual Goal Progress
```datacorejsx
const COLUMNS = [
  { id: "Annual Goal", value: row => row.$link },
  { id: "Status", value: row => row.value("status") },
  { id: "Progress", value: row => row.value("goal_progress") }
];

return function View() {
  const goals = dc.useQuery(`@page and "13-Annual-Goals" and years = "<% tp.file.title %>"`);
  const sortedGoals = dc.useArray(goals, array => 
    array.sort(row => row.value("goal_progress")).reverse()
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedGoals} />;
}
```

### Task Completion
```datacorejsx
return function View() {
  const tasks = dc.useQuery(`@page and "16-Tasks" and years = "<% tp.file.title %>"`);
  
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
  const financialLogs = dc.useQuery(`@page and "Financial Log" and years = "<% tp.file.title %>"`);
  
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

## 🎭 Yearly Reflection

### Key Learnings

**What did I learn this year?**

### Wins

**What went well?**

### Challenges

**What were the obstacles?**

### Pattern Recognition

**What patterns do I notice?**

### Next Year Focus

**What needs attention next year?**

---

## 🚀 Next Year Planning

**Primary Focus Areas**

---

*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
