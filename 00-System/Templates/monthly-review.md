---
title: <% tp.date.now("YYYY-MM") %>
month_number: <% tp.date.now("MM") %>
year: <% tp.date.now("YYYY") %>
month_start: <% tp.date.now("YYYY-MM-DD", 1) %>
month_end: <% tp.date.now("YYYY-MM-DD", 0, 1) %>
quarters: [[<% tp.date.now("YYYY-[Q]Q") %>]]
years: [[<% tp.date.now("YYYY") %>]]
weeks: []
days: []
type: monthly-review
status: Active
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
```dataview
TABLE WITHOUT ID
  file.link as "Week",
  choice(length(day_synthesis) > 0, "✅", "⏳") as "Synthesized"
FROM "Reviews/Weeks"
WHERE contains(string(this.file.name), string(months))
SORT file.name DESC
```

### Task Completion
```dataview
TABLE WITHOUT ID
  count(rows) as "Total",
  sum(choice(rows.completed, 1, 0)) as "Completed",
  round(sum(choice(rows.completed, 1, 0)) / count(rows) * 100) as "%"
FROM "16-Tasks"
WHERE contains(string(this.file.name), string(months))
FLATTEN file.tasks as t
```

### Financial Summary
```dataview
TABLE WITHOUT ID
  sum(rows.Total_Income) as "Income",
  sum(rows.Total_Expenses) as "Expenses",
  sum(rows.Net_Cashflow) as "Net"
FROM "Financial Log"
WHERE contains(string(this.file.name), string(months))
```

### Systemic Issues
```dataview
TABLE WITHOUT ID
  file.link as "Issue",
  impact as "Impact",
  status as "Status"
FROM "03-Systemic-Journal"
WHERE date >= this.month_start AND date <= this.month_end
SORT impact DESC
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
