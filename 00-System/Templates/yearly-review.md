---
title: <% tp.date.now("YYYY") %> Year Review
year: <% tp.date.now("YYYY") %>
year_start: <% tp.date.now("YYYY-01-01") %>
year_end: <% tp.date.now("YYYY-12-31") %>
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
```dataview
TABLE WITHOUT ID
  file.link as "Quarter",
  choice(length(quarter_synthesis) > 0, "✅", "⏳") as "Synthesized"
FROM "Reviews/Quarters"
WHERE contains(string(this.file.name), string(years))
SORT file.name DESC
```

### Annual Goal Progress
```dataview
TABLE WITHOUT ID
  file.link as "Annual Goal",
  status as "Status",
  goal_progress as "Progress"
FROM "Strategy/AnnualGoals"
WHERE contains(string(this.file.name), string(years))
SORT goal_progress DESC
```

### Task Completion
```dataview
TABLE WITHOUT ID
  count(rows) as "Total",
  sum(choice(rows.completed, 1, 0)) as "Completed",
  round(sum(choice(rows.completed, 1, 0)) / count(rows) * 100) as "%"
FROM "16-Tasks"
WHERE contains(string(this.file.name), string(years))
FLATTEN file.tasks as t
```

### Financial Summary
```dataview
TABLE WITHOUT ID
  sum(rows.Total_Income) as "Income",
  sum(rows.Total_Expenses) as "Expenses",
  sum(rows.Net_Cashflow) as "Net"
FROM "Financial Log"
WHERE contains(string(this.file.name), string(years))
```

### Systemic Issues
```dataview
TABLE WITHOUT ID
  file.link as "Issue",
  impact as "Impact",
  status as "Status"
FROM "03-Systemic-Journal"
WHERE date >= this.year_start AND date <= this.year_end
SORT impact DESC
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
