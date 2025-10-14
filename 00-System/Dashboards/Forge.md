---
dashboard_type: forge
created: 2025-10-14
---
# The Forge

> **Execution Engine** - Project and task management hub

## 🏗️ Active Projects

```datacorejsx
const COLUMNS = [
  { id: "Project", value: row => row.$link },
  { id: "Status", value: row => row.value("status") ?? "" },
  { id: "Priority", value: row => row.value("priority") ?? "" },
  { id: "Progress", value: row => {
    try {
      const progress = row.value("project_progress");
      return progress ? `${progress}%` : "0%";
    } catch {
      return "0%";
    }
  }},
  { id: "Deadline", value: row => {
    try {
      const deadline = row.value("deadline");
      return deadline?.toLocaleDateString() ?? "";
    } catch {
      return "";
    }
  }}
];

return function View() {
  try {
    const projects = dc.useQuery('@page and "15-Projects" and status = "Active"');
    const sortedProjects = dc.useArray(projects, array => 
      array.sort((a, b) => {
        try {
          const priorityStrA = a.value("priority") || "";
          const priorityStrB = b.value("priority") || "";
          const starsA = (priorityStrA.match(/⭐/g) || []).length;
          const starsB = (priorityStrB.match(/⭐/g) || []).length;
          
          if (starsA !== starsB) return starsB - starsA;
          
          const deadlineA = a.value("deadline");
          const deadlineB = b.value("deadline");
          const timeA = deadlineA?.getTime() || Infinity;
          const timeB = deadlineB?.getTime() || Infinity;
          
          return timeA - timeB;
        } catch {
          return 0;
        }
      })
    );
    
    return <dc.VanillaTable columns={COLUMNS} rows={sortedProjects} />;
  } catch (error) {
    return <div>⚠️ Active Projects Widget Error</div>;
  }
}
```

## 🚀 Current Sprint

**Sprint Period**: <% tp.date.now("YYYY-MM-DD", 0, -tp.date.now().weekday) %> - <% tp.date.now("YYYY-MM-DD", 6, -tp.date.now().weekday) %>

### Sprint Tasks

```datacorejsx
return function View() {
  try {
    const tasks = dc.useQuery('@task');
    const sprintTasks = dc.useArray(tasks, array => 
      array.filter(task => {
        try {
          const text = task.$text || "";
          const completed = task.completed;
          return text.includes('#sprint/current') && !completed;
        } catch {
          return false;
        }
      })
    );
    
    const grouped = sprintTasks.reduce((acc, task) => {
      try {
        const file = task.$file || "Unknown";
        if (!acc[file]) acc[file] = { file, tasks: [] };
        acc[file].tasks.push(task);
      } catch {
        // Skip invalid tasks
      }
      return acc;
    }, {});
    
    return (
      <div>
        {Object.values(grouped).map(group => (
          <div key={group.file}>
            <strong>{group.file}</strong>
            <ul>
              {group.tasks.map((task, i) => (
                <li key={i}>{task.$text || "Untitled Task"}</li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    );
  } catch (error) {
    return <div>⚠️ Current Sprint Widget Error</div>;
  }
}
```

### Sprint Backlog

```datacorejsx
return function View() {
  try {
    const tasks = dc.useQuery('@task');
    const backlogTasks = dc.useArray(tasks, array => 
      array.filter(task => {
        try {
          const text = task.$text || "";
          const completed = task.completed;
          return text.includes('#sprint/backlog') && !completed;
        } catch {
          return false;
        }
      }).slice(0, 10)
    );
    
    return (
      <ul>
        {backlogTasks.map((task, i) => (
          <li key={i}>{task.$text || "Untitled Task"}</li>
        ))}
      </ul>
    );
  } catch (error) {
    return <div>⚠️ Sprint Backlog Widget Error</div>;
  }
}
```

## 📋 Task Pipeline

### Up Next (Ready to Start)
```datacorejsx
const COLUMNS = [
  { id: "Task", value: row => row.$link || row.$text },
  { id: "Priority", value: row => row.value("priority") ?? "" },
  { id: "Status", value: row => row.value("status") ?? "" }
];

return function View() {
  try {
    const tasks = dc.useQuery('@task');
    const upNextTasks = dc.useArray(tasks, array => 
      array.filter(task => {
        try {
          const status = task.value("status");
          const completed = task.completed;
          return status === "Up Next" && !completed;
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
    
    return <dc.VanillaTable columns={COLUMNS} rows={upNextTasks.slice(0, 5)} />;
  } catch (error) {
    return <div>⚠️ Up Next Tasks Widget Error</div>;
  }
}

### In Progress
```datacorejsx
const COLUMNS = [
  { id: "Task", value: row => row.$link || row.$text },
  { id: "Priority", value: row => row.value("priority") ?? "" },
  { id: "Status", value: row => row.value("status") ?? "" }
];

return function View() {
  try {
    const tasks = dc.useQuery('@task');
    const activeTasks = dc.useArray(tasks, array => 
      array.filter(task => {
        try {
          const status = task.value("status");
          const completed = task.completed;
          return status === "Active" && !completed;
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
    
    return <dc.VanillaTable columns={COLUMNS} rows={activeTasks} />;
  } catch (error) {
    return <div>⚠️ In Progress Tasks Widget Error</div>;
  }
}

### Recently Completed
```datacorejsx
const COLUMNS = [
  { id: "Task", value: row => row.$link || row.$text },
  { id: "Completed", value: row => {
    try {
      const completion = row.completion;
      return completion?.toLocaleDateString() ?? "";
    } catch {
      return "";
    }
  }},
  { id: "Priority", value: row => row.value("priority") ?? "" }
];

return function View() {
  try {
    const sevenDaysAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);
    const tasks = dc.useQuery('@task');
    const recentCompleted = dc.useArray(tasks, array => 
      array.filter(task => {
        try {
          const completed = task.completed;
          const completion = task.completion;
          return completed && completion && completion >= sevenDaysAgo;
        } catch {
          return false;
        }
      }).sort((a, b) => {
        try {
          const completionA = a.completion?.getTime() || 0;
          const completionB = b.completion?.getTime() || 0;
          return completionB - completionA;
        } catch {
          return 0;
        }
      })
    );
    
    return <dc.VanillaTable columns={COLUMNS} rows={recentCompleted.slice(0, 10)} />;
  } catch (error) {
    return <div>⚠️ Recently Completed Widget Error</div>;
  }
}

## 📊 Project Health Matrix

```datacorejsx
const COLUMNS = [
  { id: "Health", value: row => {
    try {
      const progress = row.value("project_progress") || 0;
      if (progress >= 80) return "🟢";
      if (progress >= 50) return "🟡";
      return "🔴";
    } catch {
      return "🔴";
    }
  }},
  { id: "Project", value: row => row.$link },
  { id: "Progress", value: row => {
    try {
      const progress = row.value("project_progress");
      return progress ? `${progress}%` : "0%";
    } catch {
      return "0%";
    }
  }},
  { id: "Status", value: row => row.value("status") ?? "" }
];

return function View() {
  try {
    const projects = dc.useQuery('@page and "15-Projects" and status = "Active"');
    const sortedProjects = dc.useArray(projects, array => 
      array.sort((a, b) => {
        try {
          const progressA = a.value("project_progress") || 0;
          const progressB = b.value("project_progress") || 0;
          return progressB - progressA;
        } catch {
          return 0;
        }
      })
    );
    
    return <dc.VanillaTable columns={COLUMNS} rows={sortedProjects} />;
  } catch (error) {
    return <div>⚠️ Project Health Matrix Widget Error</div>;
  }
}

## 🎯 Strategic Execution

### Quarterly Goal Alignment

```datacorejsx
const COLUMNS = [
  { id: "Q-Goal", value: row => row.goal || "No Goal" },
  { id: "Active Projects", value: row => row.count }
];

return function View() {
  try {
    const projects = dc.useQuery('@page and "15-Projects" and status = "Active"');
    const goalGroups = dc.useArray(projects, array => {
      const goals = {};
      array.forEach(project => {
        try {
          const quarterlyGoals = project.value("quarterly_goals");
          if (quarterlyGoals && Array.isArray(quarterlyGoals)) {
            quarterlyGoals.forEach(goal => {
              const goalName = typeof goal === 'object' ? goal.$name || goal.name || "Unknown Goal" : goal;
              goals[goalName] = (goals[goalName] || 0) + 1;
            });
          } else {
            goals["No Goal"] = (goals["No Goal"] || 0) + 1;
          }
        } catch {
          goals["Error Reading Goal"] = (goals["Error Reading Goal"] || 0) + 1;
        }
      });
      
      return Object.entries(goals)
        .map(([goal, count]) => ({ goal, count }))
        .sort((a, b) => b.count - a.count);
    });
    
    return <dc.VanillaTable columns={COLUMNS} rows={goalGroups} />;
  } catch (error) {
    return <div>⚠️ Quarterly Goal Alignment Widget Error</div>;
  }
}

### Annual Goal Progress

```datacorejsx
const COLUMNS = [
  { id: "Annual Goal", value: row => row.goal || "No Goal" },
  { id: "Avg Progress", value: row => {
    try {
      return `${Math.round(row.avgProgress)}%`;
    } catch {
      return "0%";
    }
  }}
];

return function View() {
  try {
    const projects = dc.useQuery('@page and "15-Projects" and status = "Active"');
    const goalGroups = dc.useArray(projects, array => {
      const goals = {};
      array.forEach(project => {
        try {
          const annualGoals = project.value("annual_goals");
          const projectProgress = project.value("project_progress") || 0;
          
          if (annualGoals && Array.isArray(annualGoals)) {
            annualGoals.forEach(goal => {
              const goalName = typeof goal === 'object' ? goal.$name || goal.name || "Unknown Goal" : goal;
              if (!goals[goalName]) {
                goals[goalName] = { total: 0, count: 0 };
              }
              goals[goalName].total += projectProgress;
              goals[goalName].count += 1;
            });
          } else {
            if (!goals["No Goal"]) {
              goals["No Goal"] = { total: 0, count: 0 };
            }
            goals["No Goal"].total += projectProgress;
            goals["No Goal"].count += 1;
          }
        } catch {
          if (!goals["Error Reading Goal"]) {
            goals["Error Reading Goal"] = { total: 0, count: 0 };
          }
          goals["Error Reading Goal"].count += 1;
        }
      });
      
      return Object.entries(goals)
        .map(([goal, data]) => ({
          goal,
          avgProgress: data.count > 0 ? data.total / data.count : 0
        }))
        .sort((a, b) => b.avgProgress - a.avgProgress);
    });
    
    return <dc.VanillaTable columns={COLUMNS} rows={goalGroups} />;
  } catch (error) {
    return <div>⚠️ Annual Goal Progress Widget Error</div>;
  }
}

## ⚡ Quick Actions

- [ ] Move task to Current Sprint
- [ ] Create new project
- [ ] Sprint retrospective
- [ ] Replan next sprint

## 🌐 Hierarchical Navigation

### From Projects → Tasks
```datacorejsx
const COLUMNS = [
  { id: "Task", value: row => row.$link || row.$text },
  { id: "Status", value: row => row.value("status") ?? "" },
  { id: "Priority", value: row => row.value("priority") ?? "" },
  { id: "Due", value: row => {
    try {
      const dueDate = row.value("due_date") || row.value("action_date");
      return dueDate?.toLocaleDateString() ?? "";
    } catch {
      return "";
    }
  }}
];

return function View() {
  try {
    const tasks = dc.useQuery('@page and "16-Tasks"');
    const projectTasks = dc.useArray(tasks, array => 
      array.filter(task => {
        try {
          const projects = task.value("projects");
          if (!projects || !Array.isArray(projects)) return false;
          
          return projects.some(project => {
            if (typeof project === 'object') {
              return project.status === "Active";
            }
            return false;
          });
        } catch {
          return false;
        }
      }).sort((a, b) => {
        try {
          // Sort by priority first
          const priorityStrA = a.value("priority") || "";
          const priorityStrB = b.value("priority") || "";
          const starsA = (priorityStrA.match(/⭐/g) || []).length;
          const starsB = (priorityStrB.match(/⭐/g) || []).length;
          
          if (starsA !== starsB) return starsB - starsA;
          
          // Then by due date
          const dueDateA = a.value("due_date") || a.value("action_date");
          const dueDateB = b.value("due_date") || b.value("action_date");
          const timeA = dueDateA?.getTime() || Infinity;
          const timeB = dueDateB?.getTime() || Infinity;
          
          return timeA - timeB;
        } catch {
          return 0;
        }
      })
    );
    
    return <dc.VanillaTable columns={COLUMNS} rows={projectTasks.slice(0, 10)} />;
  } catch (error) {
    return <div>⚠️ Project Tasks Widget Error</div>;
  }
}

---

*Last updated: 2025-10-14*
