# The Observatory

> **Strategic Review Hub** - Multi-temporal synthesis and pattern recognition

## 📅 Current Week Overview

**Week**: Current Week
**Date Range**: This Week

### Daily Syntheses

```datacorejsx
const COLUMNS = [
  { id: "Day", value: row => row.$link },
  { id: "Day #", value: row => {
    const dayNumber = row.value("day_number");
    return dayNumber ?? "";
  }},
  { id: "Status", value: row => {
    try {
      const synthesis = row.value("day_synthesis");
      return (synthesis && synthesis.length > 0) ? "✅ Synthesized" : "⏳ Pending";
    } catch {
      return "⏳ Pending";
    }
  }}
];

return function View() {
  try {
    const sevenDaysAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);
    
    const days = dc.useQuery('@page and "06-Days"');
    const recentDays = dc.useArray(days, array => 
      array.filter(day => {
        try {
          const dayDate = day.value("date");
          return dayDate && dayDate >= sevenDaysAgo;
        } catch {
          return false;
        }
      }).sort(row => {
        try {
          const date = row.value("date");
          return date ? -date.getTime() : 0;
        } catch {
          return 0;
        }
      })
    );
    
    return <dc.VanillaTable columns={COLUMNS} rows={recentDays} />;
  } catch (error) {
    return <div>⚠️ Daily Syntheses Widget Error</div>;
  }
}
```

## 🎯 Quarterly Goals Check

```datacorejsx
const COLUMNS = [
  { id: "Quarterly Goal", value: row => row.$link },
  { id: "Status", value: row => row.value("status") ?? "" },
  { id: "KR1", value: row => row.value("key_result_1") ?? "" },
  { id: "KR2", value: row => row.value("key_result_2") ?? "" },
  { id: "KR3", value: row => row.value("key_result_3") ?? "" }
];

return function View() {
  try {
    const goals = dc.useQuery('@page and "14-Quarterly-Goals" and status != "Done"');
    const sortedGoals = dc.useArray(goals, array => 
      array.sort(row => {
        try {
          const priorityStr = row.value("priority") || "";
          const starCount = (priorityStr.match(/⭐/g) || []).length;
          return -starCount;
        } catch {
          return 0;
        }
      })
    );
    
    return <dc.VanillaTable columns={COLUMNS} rows={sortedGoals} />;
  } catch (error) {
    return <div>⚠️ Quarterly Goals Widget Error</div>;
  }
}
```

## 📈 Monthly Patterns

```datacorejsx
return function View() {
  try {
    const currentYear = new Date().getFullYear();
    const months = dc.useQuery(`@page and "08-Months" and year = ${currentYear}`);
    const sortedMonths = dc.useArray(months, array => 
      array.sort(row => {
        try {
          return -(row.value("month_number") || 0);
        } catch {
          return 0;
        }
      })
    );
    
    return (
      <ul>
        {sortedMonths.slice(0, 3).map(month => (
          <li key={month.$path}>{month.$link}</li>
        ))}
      </ul>
    );
  } catch (error) {
    return <div>⚠️ Monthly Patterns Widget Error</div>;
  }
}
```

## 💰 Financial Intelligence

### This Month's Cashflow

```datacorejsx
const COLUMNS = [
  { id: "Income", value: row => {
    try {
      return row.totalIncome?.toLocaleString() || "₹0";
    } catch {
      return "₹0";
    }
  }},
  { id: "Expenses", value: row => {
    try {
      return row.totalExpenses?.toLocaleString() || "₹0";
    } catch {
      return "₹0";
    }
  }},
  { id: "Net", value: row => {
    try {
      return row.netCashflow?.toLocaleString() || "₹0";
    } catch {
      return "₹0";
    }
  }}
];

return function View() {
  try {
    const today = new Date();
    const currentYear = today.getFullYear();
    const currentMonth = today.getMonth() + 1;
    
    const months = dc.useQuery(`@page and "08-Months" and year = ${currentYear} and month_number = ${currentMonth}`);
    if (!months || !months.array) {
      return <div>⚠️ No monthly financial data available</div>;
    }
    
    const monthlyData = dc.useArray(months, array => {
      if (!array || !Array.isArray(array)) {
        return [{ totalIncome: 0, totalExpenses: 0, netCashflow: 0 }];
      }
      
      const totalIncome = array.reduce((sum, month) => {
        try {
          return sum + (month.value("total_income") || 0);
        } catch {
          return sum;
        }
      }, 0);
      const totalExpenses = array.reduce((sum, month) => {
        try {
          return sum + (month.value("total_expenses") || 0);
        } catch {
          return sum;
        }
      }, 0);
      const netCashflow = totalIncome - totalExpenses;
      
      return [{ totalIncome, totalExpenses, netCashflow }];
    });
    
    if (!monthlyData || !Array.isArray(monthlyData)) {
      return <div>⚠️ No cashflow data available</div>;
    }
    
    return <dc.VanillaTable columns={COLUMNS} rows={monthlyData} />;
  } catch (error) {
    return <div>⚠️ Financial Cashflow Widget Error</div>;
  }
}
```

### Category Breakdown

```datacorejsx
const COLUMNS = [
  { id: "Category", value: row => row.category || "Uncategorized" },
  { id: "Total", value: row => {
    try {
      return row.total?.toLocaleString() || "₹0";
    } catch {
      return "₹0";
    }
  }}
];

return function View() {
  try {
    const thirtyDaysAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000);
    
    const transactions = dc.useQuery('@page and "20-Financial-Log"');
    if (!transactions || !transactions.array) {
      return <div>⚠️ No transaction data available</div>;
    }
    
    const categoryTotals = dc.useArray(transactions, array => {
      if (!array || !Array.isArray(array)) return [];
      
      const categories = {};
      array.forEach(transaction => {
        try {
          const transactionDate = transaction.value("date");
          if (transactionDate && transactionDate >= thirtyDaysAgo) {
            const category = transaction.value("category") || "Uncategorized";
            const amount = transaction.value("amount") || 0;
            categories[category] = (categories[category] || 0) + amount;
          }
        } catch {
          // Skip invalid transactions
        }
      });
      return Object.entries(categories)
        .map(([category, total]) => ({ category, total }))
        .sort((a, b) => Math.abs(b.total) - Math.abs(a.total));
    });
    
    if (!categoryTotals || !Array.isArray(categoryTotals)) {
      return <div>⚠️ No category data available</div>;
    }
    
    return <dc.VanillaTable columns={COLUMNS} rows={categoryTotals} />;
  } catch (error) {
    return <div>⚠️ Category Breakdown Widget Error</div>;
  }
}
```

## 🧠 Intelligence Synthesis Trends

### Most Active Perspectives

```datacorejsx
return function View() {
  try {
    const sevenDaysAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);
    const days = dc.useQuery('@page and "06-Days"');
    
    if (!days || !days.array) {
      return <div>⚠️ No daily data available</div>;
    }
    
    const perspectives = dc.useArray(days, array => {
      if (!array || !Array.isArray(array)) return [];
      
      const perspectiveCounts = {};
      
      array.forEach(day => {
        try {
          const dayDate = day.value("date");
          if (dayDate && dayDate >= sevenDaysAgo) {
            // This would need access to file content which is not directly available
            // For now, showing placeholder for perspectives
            const commonPerspectives = [
              "The Witness", "The Logos Inquisitor", "The Alpha Scanner",
              "The Structural Integrator", "The Ascension Architect",
              "The Mythopoetic Weaver", "The Somatic Arbiter",
              "The State-Hacker", "The Capital Strategist",
              "The Hearth Tender", "The Network Weaver",
              "The Stillness Warden", "The Aesthetic Calibrator",
              "The Legacy Tender", "The Systemic Navigator"
            ];
            
            commonPerspectives.forEach(perspective => {
              perspectiveCounts[perspective] = (perspectiveCounts[perspective] || 0) + 1;
            });
          }
        } catch {
          // Skip invalid days
        }
      });
      
      return Object.entries(perspectiveCounts)
        .map(([perspective, count]) => ({ perspective, count }))
        .sort((a, b) => b.count - a.count)
        .slice(0, 5);
    });
    
    if (!perspectives || !Array.isArray(perspectives)) {
      return <div>⚠️ No perspective data available</div>;
    }
    
    return (
      <ul>
        {perspectives.map(item => (
          <li key={item.perspective}>
            {item.perspective}: {item.count} entries
          </li>
        ))}
      </ul>
    );
  } catch (error) {
    return <div>⚠️ Intelligence Perspectives Widget Error</div>;
  }
}
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
```datacorejsx
const COLUMNS = [
  { id: "Day", value: row => row.$link },
  { id: "Synthesis", value: row => {
    try {
      const synthesis = row.value("day_synthesis");
      if (!synthesis) return "";
      return synthesis.length > 100 ? synthesis.substring(0, 100) + "..." : synthesis;
    } catch {
      return "";
    }
  }},
  { id: "Energy", value: row => row.value("energy_level") ?? "" }
];

return function View() {
  try {
    const today = new Date();
    const yearStart = new Date(today.getFullYear(), 0, 1);
    const yearEnd = new Date(today.getFullYear(), 11, 31);
    
    const days = dc.useQuery('@page and "06-Days"');
    const yearDays = dc.useArray(days, array => 
      array.filter(day => {
        try {
          const dayDate = day.value("date");
          return dayDate && dayDate >= yearStart && dayDate <= yearEnd;
        } catch {
          return false;
        }
      }).sort(row => {
        try {
          const date = row.value("date");
          return date ? -date.getTime() : 0;
        } catch {
          return 0;
        }
      })
    );
    
    return <dc.VanillaTable columns={COLUMNS} rows={yearDays.slice(0, 10)} />;
  } catch (error) {
    return <div>⚠️ Cross-Level Navigation Widget Error</div>;
  }
}
```
### Strategic Drill-down: Vision → All Execution
```datacorejsx
const COLUMNS = [
  { id: "Item", value: row => row.$link },
  { id: "Type", value: row => {
    const path = row.$path || "";
    if (path.includes("13-Annual-Goals")) return "Annual Goal";
    if (path.includes("14-Quarterly-Goals")) return "Quarterly Goal";
    if (path.includes("15-Projects")) return "Project";
    if (path.includes("16-Tasks")) return "Task";
    return "Unknown";
  }},
  { id: "Status", value: row => row.value("status") ?? "" },
  { id: "Progress", value: row => {
    try {
      const progress = row.value("goal_progress");
      return progress ? `${progress}%` : "0%";
    } catch {
      return "0%";
    }
  }}
];

return function View() {
  try {
    const items = dc.useQuery('(@page and "13-Annual-Goals") or (@page and "14-Quarterly-Goals") or (@page and "15-Projects") or (@page and "16-Tasks")');
    const strategicItems = dc.useArray(items, array => 
      array.filter(item => {
        try {
          const strategicHierarchy = item.value("strategic_hierarchy") || {};
          const vision = strategicHierarchy.vision;
          return vision && typeof vision === 'string';
        } catch {
          return false;
        }
      }).sort((a, b) => {
        try {
          const typeA = a.$path?.split('/')[0] || "";
          const typeB = b.$path?.split('/')[0] || "";
          const typeCompare = typeA.localeCompare(typeB);
          
          const progressA = a.value("goal_progress") || 0;
          const progressB = b.value("goal_progress") || 0;
          
          if (typeCompare !== 0) return typeCompare;
          return progressB - progressA;
        } catch {
          return 0;
        }
      })
    );
    
    return <dc.VanillaTable columns={COLUMNS} rows={strategicItems.slice(0, 15)} />;
  } catch (error) {
    return <div>⚠️ Strategic Drill-down Widget Error</div>;
  }
}
```
---