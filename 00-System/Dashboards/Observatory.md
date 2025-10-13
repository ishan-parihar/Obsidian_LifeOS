---
dashboard_type: observatory
created: 2025-10-14
---
# The Observatory

> **Strategic Review Hub** - Multi-temporal synthesis and pattern recognition

## 📅 Current Week Overview

**Week**: <% tp.date.now("YYYY-[W]WW") %>
**Date Range**: <% tp.date.now("YYYY-MM-DD", 0, -tp.date.now().weekday) %> - <% tp.date.now("YYYY-MM-DD", 6, -tp.date.now().weekday) %>

### Daily Syntheses

```dataview
TABLE WITHOUT ID
  file.link as "Day",
  day_number as "Day #",
  choice(length(day_synthesis) > 0, "✅ Synthesized", "⏳ Pending") as "Status"
FROM "Reviews/Days"
WHERE date >= date(today) - dur(7 days)
SORT date DESC
```

## 🎯 Quarterly Goals Check

```dataview
TABLE WITHOUT ID
  file.link as "Quarterly Goal",
  status as "Status",
  key_result_1 as "KR1",
  key_result_2 as "KR2",
  key_result_3 as "KR3"
FROM "Strategy/QuarterlyGoals"
WHERE status != "Done"
SORT priority DESC
```

## 📈 Monthly Patterns

```dataview
LIST
FROM "Reviews/Months"
WHERE year = date(today).year
SORT month_number DESC
LIMIT 3
```

## 💰 Financial Intelligence

### This Month's Cashflow

```dataview
TABLE WITHOUT ID
  sum(rows.Total_Income) as "Income",
  sum(rows.Total_Expenses) as "Expenses",
  sum(rows.Net_Cashflow) as "Net"
FROM "Reviews/Months"
WHERE year = date(today).year AND month_number = date(today).month
```

### Category Breakdown

```dataview
TABLE WITHOUT ID
  category as "Category",
  sum(amount) as "Total"
FROM "Financial Log"
WHERE date >= date(today) - dur(30 days)
GROUP BY category
SORT sum(amount) DESC
```

## 🧠 Intelligence Synthesis Trends

### Most Active Perspectives

```dataview
LIST
FROM "Reviews/Days"
WHERE date >= date(today) - dur(7 days)
FLATTEN file.lists as L
WHERE contains(L.text, "## The ")
GROUP BY split(L.text, "## The ")[1]
```

## 🔍 Pattern Recognition

**Emergent Themes**:
- 
- 
- 

**Potential Shifts**:
- 
- 
- 

---

*Last updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>*