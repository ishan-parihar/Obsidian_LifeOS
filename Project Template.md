---
name: "[Project Name]"
status: planning
priority: medium
area: "[Area of Responsibility]"
startDate: 2025-10-13
deadline: null
completedDate: null
tags: [project, inbox]
---

# [Project Name]

## 🎯 Project Overview
**Desired Outcome**: What does success look like?
**Why This Matters**: Purpose and motivation
**Area of Responsibility**: Which life area does this support?

## 📋 Project Details
- **Status**: `status`
- **Priority**: `priority` 
- **Start Date**: `startDate`
- **Deadline**: `deadline`
- **Estimated Effort**: 
- **Resources Needed**: 

## ✅ Action Plan

### Next Actions
```dataview
TASK FROM "02 - Tasks"
WHERE project = "[Project Name]" AND status != "Completed"
SORT priority DESC
```

### Completed Actions
```dataview
TASK FROM "02 - Tasks" 
WHERE project = "[Project Name]" AND status = "Completed"
SORT completionDate DESC
```

## 📚 Related Resources
- [ ] 

## 🔄 Progress Notes
### Week of [Date]
**Progress**: 
**Challenges**: 
**Next Steps**: 

## 🎯 Success Criteria
- [ ] 
- [ ] 
- [ ] 

## 📊 Project Metrics
- **% Complete**: 
- **Time Spent**: 
- **Budget Used**: 

> **Processing Tip**: When you create a new project from this template, remember to:
> 1. Replace `[Project Name]` in the filename and frontmatter
> 2. Update the `area` field to match your Areas of Responsibility
> 3. Set appropriate `priority` and `deadline` 
> 4. Remove the `inbox` tag once processed
> 5. Create your first task as the next action