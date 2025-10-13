---
template: weekly-review
weekOf: 2025-10-13
tags: [review, template]
---

# Weekly Review - Week of [[weekOf]]

## 📅 This Week's Highlights
### Wins & Accomplishments
- [ ] 

### Challenges & Lessons Learned  
- [ ] 

### Key Metrics
- Tasks Completed: 
- Projects Advanced: 
- Areas Reviewed: 

## 🔄 System Processing

### Inbox Processing
#### Projects Inbox
- [ ] Review and process all items
- [ ] Create new project files as needed
- [ ] Archive or delete irrelevant items

#### Tasks Inbox  
- [ ] Review and process all items
- [ ] Assign to projects/areas as appropriate
- [ ] Set priorities and due dates
- [ ] Archive or delete irrelevant items

### Project Reviews
```dataview
TABLE status, priority, deadline
FROM "01 - Projects"
WHERE status != "Completed" AND status != "Archived"
SORT priority DESC
```

For each active project:
- [ ] Review progress against goals
- [ ] Update status and completion percentage
- [ ] Identify next actions needed
- [ ] Adjust deadlines or priorities as needed

### Task Reviews
```dataview
TABLE priority, project, status
FROM "02 - Tasks"
WHERE status != "Completed" AND (dueDate = null OR dueDate >= date(weekOf))
SORT dueDate ASC
```

For overdue tasks:
- [ ] Reschedule or delegate
- [ ] Assess if still relevant/necessary

### Area Reviews
Review 1-2 Areas of Responsibility this week:
- [ ] [[Health & Fitness]]
- [ ] [[Career Development]]

## 📅 Next Week Planning

### High Priority Tasks
- [ ] 

### Key Projects to Advance
- [ ] 

### Important Deadlines
- [ ] 

### Time Blocking
- Monday: 
- Tuesday: 
- Wednesday: 
- Thursday: 
- Friday: 
- Weekend: 

## 🎯 Goals & Focus

### Weekly Theme/Focus
What's the overarching theme or focus for next week?

### Key Results to Achieve
What 3-5 key results will make next week successful?
1. 
2. 
3. 

## 📊 System Health Check

### What's Working Well?
- [ ] 

### What Needs Improvement?
- [ ] 

### Template/Process Updates Needed
- [ ] 

## ✅ Review Completion
- [ ] All inboxes processed
- [ ] All active projects reviewed  
- [ ] Next week planned
- [ ] System health assessed
- [ ] Review notes saved

> **Review Time**: Approximately 30-60 minutes
> **Best Time**: Friday afternoon or Sunday evening