# The Observatory

> **Strategic Review Hub** - Multi-temporal synthesis and pattern recognition

## 📅 Current Week Overview

**Week**: Current Week
**Date Range**: This Week

### Daily Syntheses

```datacorejsx
const COLUMNS = [
  { id: "Day", value: row => row.$link },
  { id: "Day #", value: row => row.value("day_number") || "" },
  { id: "Status", value: row => {
    const synthesis = row.value("day_synthesis");
    return synthesis && synthesis.length > 0 ? "✅ Synthesized" : "⏳ Pending";
  }}
];

return function View() {
  const sevenDaysAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);
  
  const days = dc.useQuery('@page and "06-Days"');
  const recentDays = dc.useArray(days, array => 
    array.filter(day => {
      const dayDate = day.value("date");
      return dayDate && dayDate >= sevenDaysAgo;
    }).sort(row => {
      const date = row.value("date");
      return date ? -date.getTime() : 0;
    })
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={recentDays} />;
}
```

## 🎯 Quarterly Goals Check

```datacorejsx
const COLUMNS = [
  { id: "Quarterly Goal", value: row => row.$link },
  { id: "Status", value: row => row.value("status") },
  { id: "KR1", value: row => row.value("key_result_1") },
  { id: "KR2", value: row => row.value("key_result_2") },
  { id: "KR3", value: row => row.value("key_result_3") }
];

return function View() {
  const goals = dc.useQuery('@page and "14-Quarterly-Goals" and status != "Done"');
  const sortedGoals = dc.useArray(goals, array => 
    array.sort(row => -(parseInt(row.value("priority")?.match(/⭐/g)?.length || 0)))
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedGoals} />;
}
```

## 📈 Monthly Patterns

```datacorejsx
return function View() {
  const currentYear = new Date().getFullYear();
  const months = dc.useQuery(`@page and "08-Months" and year = ${currentYear}`);
  const sortedMonths = dc.useArray(months, array => 
    array.sort(row => -(row.value("month_number") || 0))
  );
  
  return (
    <ul>
      {sortedMonths.slice(0, 3).map(month => (
        <li key={month.$path}>{month.$link}</li>
      ))}
    </ul>
  );
}
```

## 💰 Financial Intelligence

### This Month's Cashflow

```datacorejsx
const COLUMNS = [
  { id: "Income", value: row => row.totalIncome.toLocaleString() },
  { id: "Expenses", value: row => row.totalExpenses.toLocaleString() },
  { id: "Net", value: row => row.netCashflow.toLocaleString() }
];

return function View() {
  const today = new Date();
  const currentYear = today.getFullYear();
  const currentMonth = today.getMonth() + 1;
  
  const months = dc.useQuery(`@page and "08-Months" and year = ${currentYear} and month_number = ${currentMonth}`);
  const monthlyData = dc.useArray(months, array => {
    const totalIncome = array.reduce((sum, month) => sum + (month.value("total_income") || 0), 0);
    const totalExpenses = array.reduce((sum, month) => sum + (month.value("total_expenses") || 0), 0);
    const netCashflow = totalIncome - totalExpenses;
    
    return [{ totalIncome, totalExpenses, netCashflow }];
  });
  
  return <dc.VanillaTable columns={COLUMNS} rows={monthlyData} />;
}
```

### Category Breakdown

```datacorejsx
const COLUMNS = [
  { id: "Category", value: row => row.category },
  { id: "Total", value: row => row.total.toLocaleString() }
];

return function View() {
  const thirtyDaysAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000);
  
  const transactions = dc.useQuery('@page and "20-Financial-Log"');
  const categoryTotals = dc.useArray(transactions, array => {
    const categories = {};
    array.forEach(transaction => {
      const transactionDate = transaction.value("date");
      if (transactionDate && transactionDate >= thirtyDaysAgo) {
        const category = transaction.value("category") || "Uncategorized";
        const amount = transaction.value("amount") || 0;
        categories[category] = (categories[category] || 0) + amount;
      }
    });
    return Object.entries(categories)
      .map(([category, total]) => ({ category, total }))
      .sort((a, b) => Math.abs(b.total) - Math.abs(a.total));
  });
  
  return <dc.VanillaTable columns={COLUMNS} rows={categoryTotals} />;
}
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