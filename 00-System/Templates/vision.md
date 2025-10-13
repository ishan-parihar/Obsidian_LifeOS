---
vision_statement: 
guiding_question: 
strategic_pillars: []
priority: ⭐⭐⭐
status: Planning
review_date: 
last_review_date: 
life_aspects: []
values: []
annual_goals: []
quarterly_goals: []
type: vision
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.file.title %>

## 👁️ Vision Statement

## 🎯 Guiding Question

## 🏛️ Strategic Pillars

## 📊 Priority & Status

**Priority**: 
**Status**: 

**Next Review**: 
**Last Reviewed**: 

## 🔗 Strategic Alignment

**Life Aspects**: 
**Core Values**: 

## 📈 Manifestation

### Annual Goals

```dataview
TABLE WITHOUT ID
  file.link as "Annual Goal",
  status as "Status",
  goal_progress as "Progress"
FROM "Strategy/AnnualGoals"
WHERE contains(vision, "<% tp.file.title %>")
SORT goal_progress DESC
```

### Quarterly Progress

```dataview
TABLE WITHOUT ID
  count(rows) as "Q-Goals",
  sum(choice(rows.status = "Done", 1, 0)) as "Completed",
  round(sum(choice(rows.status = "Done", 1, 0)) / count(rows) * 100) as "%"
FROM "Strategy/QuarterlyGoals"
WHERE contains(vision, "<% tp.file.title %>")
```

## 🧼 Vision Review

### What's Working

### What Needs Adjustment

### Emerging Insights

---

*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
