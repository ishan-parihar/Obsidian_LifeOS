---
title: "<% tp.date.now('YYYY-MM') %>"
month_number: <% tp.date.now("MM") %>
year: <% tp.date.now("YYYY") %>
time_period_start: "<% tp.date.now('YYYY-MM-01') %>"
time_period_end: "<% tp.date.now('YYYY-MM-DD', 0, tp.date.now('YYYY-MM-01'), 1, 'month') %>"
containing_period: "[[<% tp.date.now('YYYY-[Q]Q') %>]]"
contained_periods: []
parallel_periods: []
hierarchy_level: "review"
parent_entities: []
child_entities: []
sibling_entities: []
related_time_periods: []
strategic_alignment: []
quarters: ["[[<% tp.date.now('YYYY-[Q]Q') %>]]"]
years: ["[[<% tp.date.now('YYYY') %>]]"]
weeks: []
days: []
entity_type: "monthly-review"
status: "Active"
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.date.now("MMMM YYYY") %> Review

**Date Range**: <% tp.date.now("YYYY-MM-DD", 1) %> - <% tp.date.now("YYYY-MM-DD", 0, 1) %>

---

## 🧠 Intelligence Synthesis

### Month Synthesis

### The Witness
*Monthly Awareness and Observation*

### The Logos Inquisitor
*Monthly Rational Analysis*

### The Alpha Scanner
*Monthly Opportunities and Threats*

### The Structural Integrator
*Monthly Systems Thinking*

### The Ascension Architect
*Monthly Growth and Development*

### The Mythopoetic Weaver
*Monthly Narrative and Meaning*

### The Somatic Arbiter
*Monthly Body Wisdom*

### The State-Hacker
*Monthly Consciousness States*

### The Capital Strategist
*Monthly Financial Intelligence*

### The Hearth Tender
*Monthly Home and Family Dynamics*

### The Network Weaver
*Monthly Relationship Intelligence*

### The Stillness Warden
*Monthly Peace and Rest*

### The Aesthetic Calibrator
*Monthly Beauty and Design*

### The Legacy Tender
*Monthly Long-term Impact*

### The Systemic Navigator
*Monthly Operational Intelligence*

---

## 🎯 Meta-Synthesis

### Month Oracle Synthesis
*Monthly Wisdom Perspective*

### Month Phoenix Synthesis
*Monthly Transformation Perspective*

### Month Sovereign Synthesis
*Monthly Power and Agency*

---

## 📊 Monthly Metrics

### Weekly Summaries
```datacorejsx
const COLUMNS = [
  { id: "Week", value: row => row.$link },
  { id: "Synthesized", value: row => row.value("day_synthesis") ? "✅" : "⏳" }
];

return function View() {
  const weeks = dc.useQuery(`@page and "07-Weeks" and months = "<% tp.file.title %>"`);
  const sortedWeeks = dc.useArray(weeks, array => 
    array.sort(row => row.$name)
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedWeeks} />;
}
```

### Task Completion
```datacorejsx
return function View() {
  const tasks = dc.useQuery(`@page and "16-Tasks" and months = "<% tp.file.title %>"`);
  
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
  const financialLogs = dc.useQuery(`@page and "Financial Log" and months = "<% tp.file.title %>"`);
  
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
    array.sort(row => row.value("impact"))
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedIssues} />;
}
```

---

## 🎭 Monthly Reflection

### Key Learnings

**What did I learn this month?**

### Wins

**What went well?**

### Challenges

**What were the obstacles?**

### Pattern Recognition

**What patterns do I notice?**

### Next Month Focus

**What needs attention next month?**

---

## 🚀 Next Month Planning

**Primary Focus Areas**

---

*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
