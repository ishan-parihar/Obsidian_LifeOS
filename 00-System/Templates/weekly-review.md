---
title: <% tp.date.now("YYYY-[W]WW") %>
week_number: <% tp.date.now("WW") %>
year: <% tp.date.now("YYYY") %>
week_start: <% tp.date.now("YYYY-MM-DD", 0, -tp.date.now().weekday) %>
week_end: <% tp.date.now("YYYY-MM-DD", 6, -tp.date.now().weekday) %>
months: [[<% tp.date.now("YYYY-MM") %>]]
quarters: [[<% tp.date.now("YYYY-[Q]Q") %>]]
years: [[<% tp.date.now("YYYY") %>]]
days: []
type: weekly-review
status: Active
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

```dataview
TABLE WITHOUT ID
  file.link as "Day",
  choice(length(day_synthesis) > 0, "✅", "⏳") as "Synthesized",
  choice(length(night_wind_down) > 0, "✅", "⏳") as "Reflected"
FROM "Reviews/Days"
WHERE contains(string(this.file.name), string(weeks))
SORT date DESC
```

### Task Completion

```dataview
TABLE WITHOUT ID
  count(rows) as "Total",
  sum(choice(rows.completed, 1, 0)) as "Completed",
  round(sum(choice(rows.completed, 1, 0)) / count(rows) * 100) as "%"
FROM "16-Tasks"
WHERE contains(string(this.file.name), string(weeks))
FLATTEN file.tasks as t
```

### Financial Summary

```dataview
TABLE WITHOUT ID
  sum(rows.Total_Income) as "Income",
  sum(rows.Total_Expenses) as "Expenses",
  sum(rows.Net_Cashflow) as "Net"
FROM "Financial Log"
WHERE contains(string(this.file.name), string(weeks))
```

### Systemic Issues

```dataview
TABLE WITHOUT ID
  file.link as "Issue",
  impact as "Impact",
  status as "Status"
FROM "Logs/Systemic"
WHERE date >= this.week_start AND date <= this.week_end
SORT impact DESC
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