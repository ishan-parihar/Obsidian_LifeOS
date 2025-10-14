
# The Workbench

> **Today's Command Center** - Real-time operational intelligence

## 🔥 Today's Focus

```datacorejsx
const COLUMNS = [
  { id: "Task", value: row => row.$link },
  { id: "Priority", value: row => row.value("priority") ?? "" },
  { id: "Status", value: row => row.value("status") ?? "" }
];

return function View() {
  try {
    const projects = dc.useQuery('@page and "15-Projects" and status = "Active"');
    const currentSprintProjects = dc.useArray(projects, array => 
      array.filter(project => {
        try {
          const tags = project.$tags || [];
          return tags.includes('#sprint/current');
        } catch {
          return false;
        }
      }).sort((a, b) => {
        try {
          const priorityStrA = a.value("priority") || "";
          const priorityStrB = b.value("priority") || "";
          const starsA = (priorityStrA.match(/⭐/g) || []).length;
          const starsB = (priorityStrB.match(/⭐/g) || []).length;
          return starsB - starsA;
        } catch {
          return 0;
        }
      })
    );
    
    return <dc.VanillaTable columns={COLUMNS} rows={currentSprintProjects.slice(0, 10)} />;
  } catch (error) {
    return <div>⚠️ Today's Focus Widget Error</div>;
  }
}
```

## ⚡ Systemic Issues

```datacorejsx
const COLUMNS = [
  { id: "Issue", value: row => row.$link },
  { id: "Impact", value: row => row.value("impact") ?? "" },
  { id: "Status", value: row => row.value("status") ?? "" }
];

return function View() {
  try {
    const issues = dc.useQuery('@page and "03-Systemic-Journal" and (status = "Triage" or status = "Escalated")');
    const sortedIssues = dc.useArray(issues, array => 
      array.sort((a, b) => {
        try {
          const impactStrA = a.value("impact") || "";
          const impactStrB = b.value("impact") || "";
          const matchA = impactStrA.match(/P(\d)/);
          const matchB = impactStrB.match(/P(\d)/);
          const priorityA = matchA ? parseInt(matchA[1]) : 0;
          const priorityB = matchB ? parseInt(matchB[1]) : 0;
          return priorityB - priorityA;
        } catch {
          return 0;
        }
      })
    );
    
    return <dc.VanillaTable columns={COLUMNS} rows={sortedIssues.slice(0, 5)} />;
  } catch (error) {
    return <div>⚠️ Systemic Issues Widget Error</div>;
  }
}
```

## 👥 People Reconnections

```datacorejsx
const COLUMNS = [
  { id: "Person", value: row => row.$link },
  { id: "Reconnect By", value: row => {
    const reconnectBy = row.value("reconnect_by");
    return reconnectBy ? reconnectBy.toLocaleDateString() : "";
  }},
  { id: "Profile", value: row => row.value("networking_profile") || "" }
];

return function View() {
  const today = new Date();
  const sevenDaysFromNow = new Date(today.getTime() + 7 * 24 * 60 * 60 * 1000);
  
  const people = dc.useQuery('@page and "17-People"');
  const filteredPeople = dc.useArray(people, array => 
    array.filter(person => {
      const reconnectBy = person.value("reconnect_by");
      return reconnectBy && reconnectBy <= sevenDaysFromNow;
    }).sort(row => {
      const reconnectBy = row.value("reconnect_by");
      return reconnectBy ? reconnectBy.getTime() : 0;
    })
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={filteredPeople.slice(0, 5)} />;
}
```

## 📊 Today's Metrics

- **Active Projects**: 
- **Current Sprint Tasks**: 
- **Systemic Dissonances**: 
- **People to Connect**: 

## 🎯 Strategic Alignment

```datacorejsx
return function View() {
  const goals = dc.useQuery('@page and "13-Annual-Goals" and status = "Active"');
  
  return (
    <ul>
      {goals.map(goal => (
        <li key={goal.$path}>{goal.$link}</li>
      ))}
    </ul>
  );
}
```

## 🌐 Hierarchical Navigation

### From Annual Goals → Tasks
```datacorejsx
const COLUMNS = [
  { id: "Task", value: row => row.$link },
  { id: "Status", value: row => row.value("status") },
  { id: "Priority", value: row => row.value("priority") },
  { id: "Due", value: row => row.value("action_date")?.toLocaleDateString() }
];

return function View() {
  const tasks = dc.useQuery('@page and "16-Tasks"');
  const alignedTasks = dc.useArray(tasks, array => 
    array.filter(task => {
      const strategicHierarchy = task.value("strategic_hierarchy") || {};
      const annualGoals = strategicHierarchy.annual_goals || [];
      return annualGoals.some(goal => typeof goal === 'object' && goal.status === "Active");
    }).sort((a, b) => {
      const priorityA = parseInt(a.value("priority")?.match(/⭐/g)?.length || 0);
      const priorityB = parseInt(b.value("priority")?.match(/⭐/g)?.length || 0);
      if (priorityA !== priorityB) return priorityB - priorityA;
      
      const dateA = a.value("action_date")?.getTime() || 0;
      const dateB = b.value("action_date")?.getTime() || 0;
      return dateA - dateB;
    })
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={alignedTasks.slice(0, 10)} />;
}
```

### Time Navigation: Current Week → Days
```datacorejsx
const COLUMNS = [
  { id: "Day", value: row => row.$link },
  { id: "Synthesis", value: row => {
    const synthesis = row.value("day_synthesis");
    if (!synthesis) return "";
    return synthesis.length > 100 ? synthesis.substring(0, 100) + "..." : synthesis;
  }},
  { id: "Energy", value: row => row.value("energy_level") || "" }
];

return function View() {
  const today = new Date();
  const weekStart = new Date(today.setDate(today.getDate() - today.getDay()));
  const weekEnd = new Date(weekStart.getTime() + 6 * 24 * 60 * 60 * 1000);
  
  const days = dc.useQuery('@page and "06-Days"');
  const weekDays = dc.useArray(days, array => 
    array.filter(day => {
      const dayDate = day.value("date");
      return dayDate && dayDate >= weekStart && dayDate <= weekEnd;
    }).sort(row => {
      const date = row.value("date");
      return date ? -date.getTime() : 0;
    })
  );
  
  return <dc.VanillaTable columns={COLUMNS} rows={weekDays.slice(0, 7)} />;
}
```

## 🔗 Quick Actions

- [ ] Create new Subjective log
- [ ] Log Systemic issue
- [ ] Add Activity entry
- [ ] Review Today's synthesis

---

*Last updated: Real-time*
