---
title: <% tp.date.now("YYYY-[Q]Q") %> Review
quarter_number: <% tp.date.now("[Q]Q") %>
year: <% tp.date.now("YYYY") %>
quarter_start: <% tp.date.now("YYYY-MM-DD", 0, -tp.date.now().quarter + 1) %>
quarter_end: <% tp.date.now("YYYY-MM-DD", 0, -tp.date.now().quarter + 1 + 90) %>
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
```dataview
TABLE WITHOUT ID
  file.link as "Month",
  choice(length(month_synthesis) > 0, "✅", "⏳") as "Synthesized"
FROM "Reviews/Months"
WHERE contains(string(this.file.name), string(quarters))
SORT file.name DESC
```

### Goal Progress
```dataview
TABLE WITHOUT ID
  file.link as "Quarterly Goal",
  status as "Status",
  goal_progress as "Progress"
FROM "Strategy/QuarterlyGoals"
WHERE contains(string(this.file.name), string(quarters))
SORT goal_progress DESC
```

### Task Completion
```dataview
TABLE WITHOUT ID
  count(rows) as "Total",
  sum(choice(rows.completed, 1, 0)) as "Completed",
  round(sum(choice(rows.completed, 1, 0)) / count(rows) * 100) as "%"
FROM "16-Tasks"
WHERE contains(string(this.file.name), string(quarters))
FLATTEN file.tasks as t
```

### Financial Summary
```dataview
TABLE WITHOUT ID
  sum(rows.Total_Income) as "Income",
  sum(rows.Total_Expenses) as "Expenses",
  sum(rows.Net_Cashflow) as "Net"
FROM "Financial Log"
WHERE contains(string(this.file.name), string(quarters))
```

### Systemic Issues
```dataview
TABLE WITHOUT ID
  file.link as "Issue",
  impact as "Impact",
  status as "Status"
FROM "03-Systemic-Journal"
WHERE date >= this.quarter_start AND date <= this.quarter_end
SORT impact DESC
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