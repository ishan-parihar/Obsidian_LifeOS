---
title: "<% tp.date.now('YYYY-[W]WW') %>"
weekly_week_number: <% tp.date.now("WW") %>
weekly_year: <% tp.date.now("YYYY") %>
weekly_time_period_start: "<% tp.date.now('YYYY-MM-DD', -tp.date.now().weekday()) %>"
weekly_time_period_end: "<% tp.date.now('YYYY-MM-DD', 6 - tp.date.now().weekday()) %>"
weekly_containing_period: "[[<% tp.date.now('YYYY-[Q]Q') %>]]"
entity_hierarchy_level: "review"
entity_type: "weekly-review"
weekly_months: ["[[<% tp.date.now('YYYY-MM') %>]]"]
weekly_quarters: ["[[<% tp.date.now('YYYY-[Q]Q') %>]]"]
weekly_years: ["[[<% tp.date.now('YYYY') %>]]"]
weekly_days: []
weekly_status: "Active"
weekly_week_synthesis: ""
weekly_the_witness: ""
weekly_the_logos_inquisitor: ""
weekly_the_alpha_scanner: ""
weekly_the_structural_integrator: ""
weekly_the_ascension_architect: ""
weekly_the_mythopoetic_weaver: ""
weekly_the_somatic_arbiter: ""
weekly_the_state_hacker: ""
weekly_the_capital_strategist: ""
weekly_the_hearth_tender: ""
weekly_the_network_weaver: ""
weekly_the_stillness_warden: ""
weekly_the_aesthetic_calibrator: ""
weekly_the_legacy_tender: ""
weekly_the_systemic_navigator: ""
weekly_week_oracle_synthesis: ""
weekly_week_phoenix_synthesis: ""
weekly_week_sovereign_synthesis: ""
weekly_key_learnings: ""
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# Week <% tp.date.now("YYYY-[W]WW") %> Review

**Date Range**: <% tp.date.now("YYYY-MM-DD", 0, -tp.date.now().weekday) %> - <% tp.date.now("YYYY-MM-DD", 6, -tp.date.now().weekday) %>

---

## 🧠 Intelligence Synthesis

### Week Synthesis

### The Witness
*Weekly Awareness and Observation*

### The Logos Inquisitor
*Weekly Rational Analysis*

### The Alpha Scanner
*Weekly Opportunities and Threats*

### The Structural Integrator
*Weekly Systems Thinking*

### The Ascension Architect
*Weekly Growth and Development*

### The Mythopoetic Weaver
*Weekly Narrative and Meaning*

### The Somatic Arbiter
*Weekly Body Wisdom*

### The State-Hacker
*Weekly Consciousness States*

### The Capital Strategist
*Weekly Financial Intelligence*

### The Hearth Tender
*Weekly Home and Family Dynamics*

### The Network Weaver
*Weekly Relationship Intelligence*

### The Stillness Warden
*Weekly Peace and Rest*

### The Aesthetic Calibrator
*Weekly Beauty and Design*

### The Legacy Tender
*Weekly Long-term Impact*

### The Systemic Navigator
*Weekly Operational Intelligence*

---

## 🎯 Meta-Synthesis

### Week Oracle Synthesis
*Weekly Wisdom Perspective*

### Week Phoenix Synthesis
*Weekly Transformation Perspective*

### Week Sovereign Synthesis
*Weekly Power and Agency*

---

## 📊 Weekly Metrics

### Daily Summaries

```datacorejsx
const COLUMNS = [
  { id: "Day", value: row => row.$link },
  { id: "Synthesized", value: row => row.value("day_synthesis") ? "✅" : "⏳" },
  { id: "Reflected", value: row => row.value("night_wind_down") ? "✅" : "⏳" }
];

return function View() {
  const days = dc.useQuery(`@page and "06-Days" and weeks = "<% tp.file.title %>"`);
  const sortedDays = dc.useArray(days, array => 
    array.sort(row => row.value("date"))
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedDays} />;
}
```

### Task Completion

```datacorejsx
return function View() {
  const tasks = dc.useQuery(`@page and "16-Tasks" and weeks = "<% tp.file.title %>"`);
  
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
  const financialLogs = dc.useQuery(`@page and "Financial Log" and weeks = "<% tp.file.title %>"`);
  
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
  const issues = dc.useQuery(`@page and "Logs/Systemic" and date >= "<% tp.frontmatter.time_period_start %>" and date <= "<% tp.frontmatter.time_period_end %>"`);
  const sortedIssues = dc.useArray(issues, array => 
    array.sort(row => row.value("impact"))
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedIssues} />;
}
```

---

## 🎭 Weekly Reflection

### Key Learnings

**What did I learn this week?**

### Wins

**What went well?**

### Challenges

**What were the obstacles?**

### Pattern Recognition

**What patterns do I notice?**

### Next Week Focus

**What needs attention next week?**

---

## 🚀 Next Week Planning

**Primary Focus Areas**