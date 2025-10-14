# The Observatory

> **Strategic Review Hub** - Multi-temporal synthesis and pattern recognition

## 📅 Current Week Overview

**Week**: Current Week
**Date Range**: This Week

### Daily Syntheses

```dataview
TABLE WITHOUT ID
  file.link as "Day",
  day_number as "Day #",
  choice(length(day_synthesis) > 0, "✅ Synthesized", "⏳ Pending") as "Status"
FROM "06-Days"
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
FROM "14-Quarterly-Goals"
WHERE status != "Done"
SORT priority DESC
```

## 📈 Monthly Patterns

```dataview
LIST
FROM "08-Months"
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
FROM "08-Months"
WHERE year = date(today).year AND month_number = date(today).month
```

### Category Breakdown

```dataview
TABLE WITHOUT ID
  category as "Category",
  sum(amount) as "Total"
FROM "20-Financial-Log"
WHERE date >= date(today) - dur(30 days)
GROUP BY category
SORT sum(amount) DESC
```

## 🧠 Intelligence Synthesis Trends

### Most Active Perspectives

```dataview
LIST
FROM "06-Days"
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

## 🌐 Hierarchical Navigation

### Cross-Level Navigation: Years → Days
```dataview
TABLE WITHOUT ID
  file.link as "Day",
  day_synthesis as "Synthesis",
  energy_level as "Energy"
FROM "06-Days"
WHERE date >= date("2025-01-01") AND date <= date("2025-12-31")
SORT date DESC
LIMIT 10
```

### Strategic Drill-down: Vision → All Execution
```dataview
TABLE WITHOUT ID
  file.link as "Item",
  type as "Type",
  status as "Status",
  goal_progress as "Progress"
FROM "13-Annual-Goals" OR "14-Quarterly-Goals" OR "15-Projects" OR "16-Tasks"
WHERE contains(strategic_hierarchy.vision, "Vision")
SORT type ASC, goal_progress DESC
LIMIT 15
```

---

*Last updated: Real-time*