# Life Management Dashboard

Welcome to your Life Management System! This dashboard serves as your central hub for organizing all aspects of your personal and professional life.

## 🎯 Quick Actions
- [ ] Review weekly goals
- [ ] Check upcoming deadlines
- [ ] Process inbox items
- [ ] Update project statuses

## 📊 System Overview

### Areas of Responsibility
```dataview
TABLE status, priority
FROM "03 - Areas of Responsibility"
SORT priority DESC
```

### Active Projects
```dataview
TABLE status, deadline, priority
FROM "01 - Projects"
WHERE status != "Completed" AND status != "Archived"
SORT deadline ASC
```

### Upcoming Tasks
```dataview
TABLE priority, project, status
FROM "02 - Tasks"
WHERE status != "Completed" AND (dueDate = null OR dueDate >= date(today))
SORT dueDate ASC
```

### Recent Activity
```dataview
TABLE file.mtime as "Last Modified"
FROM ""
WHERE file.name != "Life Management Dashboard"
SORT file.mtime DESC
LIMIT 10
```

## 🗂️ Navigation

- **[[Life Management Overview]]** - Complete system documentation
- **[[Areas of Responsibility]]** - Your key life domains
- **[[Projects Inbox]]** - Capture new project ideas
- **[[Tasks Inbox]]** - Capture new tasks
- **[[Weekly Review Template]]** - Regular system maintenance

## 🔄 System Maintenance

### Daily
- Review today's tasks
- Process inbox items
- Update task statuses

### Weekly
- Complete weekly review
- Plan upcoming week
- Review project progress
- Clean up completed items

### Monthly
- Review areas of responsibility
- Assess life balance
- Set monthly goals
- Archive completed work

> **Tip**: Use the `#inbox` tag for items that need processing, and `#review` for items needing attention during your weekly review.