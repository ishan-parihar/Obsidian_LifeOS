# Getting Started Guide

Welcome to your Life Management System! This guide will walk you through setting up and using your new system step by step.

## 🚀 Quick Start (First 30 Minutes)

### Step 1: Install Required Plugins
1. Open Obsidian Settings → Community Plugins
2. Install these essential plugins:
   - **Dataview** (for dynamic views and dashboards)
   - **Templater** (for templates - optional but recommended)
3. Enable the plugins in Settings → Core Plugins:
   - **Daily Notes** (for daily task tracking)
   - **Backlinks** (to see connections between notes)

### Step 2: Review Your Dashboard
- Open [[Life Management Dashboard]]
- This is your central command center
- All key information is displayed here dynamically

### Step 3: Set Up Your Areas
1. Review [[Areas of Responsibility]]
2. Customize the areas to match your life:
   - Keep 5-10 total areas maximum
   - Create individual files for each area you want to track
   - Update the frontmatter with your priorities

### Step 4: Process Your Inboxes
1. Check [[Projects Inbox]] - add any current projects
2. Check [[Tasks Inbox]] - add any pending tasks  
3. Process these items using the guidelines in each file

## 📋 Week 1: Foundation Building

### Day 1-2: Areas Setup
- [ ] Review and finalize your Areas of Responsibility
- [ ] Create files for your top 3-5 priority areas
- [ ] Set realistic standards for each area

### Day 3-4: Project Capture  
- [ ] Brain dump all current projects into [[Projects Inbox]]
- [ ] Process each project using the [[Project Template]]
- [ ] Link projects to appropriate Areas of Responsibility

### Day 5-7: Task Management
- [ ] Capture all pending tasks in [[Tasks Inbox]]
- [ ] Process tasks using the [[Task Template]]
- [ ] Link tasks to projects and areas
- [ ] Set priorities and due dates

## 🔧 System Configuration

### Dataview Setup
Your system uses Dataview queries extensively. To ensure everything works:

1. **Enable Dataview**: Settings → Community Plugins → Dataview → Enable
2. **Auto-refresh**: In Dataview settings, enable "Auto-refresh everything"
3. **Inline Queries**: Enable "Inline queries" for task lists

### File Naming Conventions
- **Projects**: `Project - [Name].md`
- **Tasks**: `Task - [Description].md`
- **Areas**: `[Area Name].md` (no prefix for easy linking)
- **Templates**: Include "Template" in the name
- **Archive**: Include "Archive" in the name

### Frontmatter Standards
Always include these fields in your files:

**For Projects:**
```yaml
---
name: "Project Name"
status: planning|in-progress|waiting|review|completed
priority: high|medium|low
area: "Area Name"
startDate: YYYY-MM-DD
deadline: YYYY-MM-DD
tags: [project]
---
```

**For Tasks:**
```yaml
---
name: "Task Description"
status: todo|in-progress|waiting|review|done
priority: urgent|high|medium|low
context: home|work|errand|call|computer
project: "Project Name"
area: "Area Name"  
dueDate: YYYY-MM-DD
tags: [task]
---
```

## 🔄 Daily Workflow

### Morning (5 minutes)
1. Open [[Life Management Dashboard]]
2. Review today's tasks (due today)
3. Check for urgent items
4. Plan your day's focus

### Throughout the Day
1. **Capture**: Add new tasks to [[Tasks Inbox]]
2. **Complete**: Mark tasks as done in their individual files
3. **Update**: Adjust priorities and due dates as needed

### Evening (5 minutes)
1. Review completed tasks
2. Add any new items to inboxes
3. Prepare for tomorrow

## 📅 Weekly Workflow

### Weekly Review (30-60 minutes)
Use the [[Weekly Review Template]] every week:

1. **Process Inboxes**: Clear Projects and Tasks Inbox
2. **Review Projects**: Update all active project statuses
3. **Plan Next Week**: Set priorities and key focus areas  
4. **Review Areas**: Check 1-2 Areas of Responsibility
5. **System Health**: Assess what's working and what needs adjustment

## 🛠️ Troubleshooting

### Dataview Queries Not Working
- Ensure Dataview plugin is installed and enabled
- Check that frontmatter fields match exactly (case-sensitive)
- Verify file paths in queries match your actual folder structure

### Templates Not Loading
- If using Templater plugin: Check template folder settings
- Manual method: Copy/paste from template files directly

### Overwhelmed by Setup
- Start with just 3 areas and 3 projects
- Focus on capturing current commitments first
- Expand the system gradually as you get comfortable

## 🎯 Success Tips

### Start Small
- Don't try to set up everything perfectly on day one
- Begin with your most important areas and projects
- Add complexity only as needed

### Be Consistent  
- Daily and weekly reviews are crucial
- Even 5 minutes daily is better than 1 hour weekly
- Consistency beats perfection

### Customize Freely
- This is your system - adapt it to your needs
- Add your own tags, categories, and workflows
- Remove anything that doesn't serve you

### Review and Evolve
- Your system should grow with you
- Regularly ask: "Is this still working for me?"
- Don't be afraid to change templates and processes

## 📚 Next Steps

Once you're comfortable with the basics:

1. **Explore Advanced Features**:
   - Custom Dataview queries for your specific needs
   - Daily notes integration for time tracking
   - Calendar plugin for visual scheduling

2. **Expand Your Areas**:
   - Add more specific areas as needed
   - Create sub-areas for complex domains

3. **Build Your Knowledge Base**:
   - Use the Resources folder for reference materials
   - Link related concepts and ideas
   - Create your own best practices documentation

## 🤝 Support and Community

Remember, you're not alone in this journey! Consider:
- Joining Obsidian Discord communities
- Following productivity and PKM (Personal Knowledge Management) content
- Sharing your system with accountability partners

> **Final Thought**: The goal isn't a perfect system—it's a system that helps you live a more intentional, productive, and fulfilling life. Start where you are, use what you have, and build as you go!