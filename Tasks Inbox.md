# Tasks Inbox

This is your capture point for all individual tasks, to-dos, and action items. Process these regularly to keep your system current and prevent overwhelm.

## 📥 Capture New Tasks

Add tasks as you think of them, receive them, or identify them from projects. Use the format below for quick capture:

### Quick Capture Format
- **Task**: What needs to be done?
- **Context**: Where/when can this be done? (home, work, errand, call, computer)
- **Priority**: How important is this? (urgent, high, medium, low)
- **Project**: Which project does this support? (if any)
- **Due Date**: When does this need to be completed?

## 🔄 Processing Guidelines

When processing inbox tasks, decide:

1. **Delete**: Is this still relevant/necessary?
2. **Delegate**: Can someone else do this?
3. **Defer**: When will you do this? Set due date and context
4. **Do**: Can you complete it in <2 minutes? Do it now!
5. **Document**: Does this belong in a project or area file?

## 📋 Current Inbox Items

### New Tasks
- [ ] 

### Follow-ups Needed
- [ ] 

### Quick Actions (<2 minutes)
- [ ] 

## 📊 Unprocessed Tasks Dashboard

```dataview
LIST
FROM #inbox AND #task
SORT file.ctime DESC
```

## 🎯 Today's Focus

```dataview
TASK FROM "02 - Tasks"
WHERE dueDate = date(today) AND status != "Completed"
SORT priority DESC
```

> **Pro Tip**: Review your Tasks Inbox at least once daily to keep your system current and prevent task accumulation!