# Life Management Overview

This system is built on proven productivity methodologies including Getting Things Done (GTD), Eisenhower Matrix, and Personal Knowledge Management principles. It's designed to help you:

- **Clarify** your vision and priorities
- **Capture** everything that demands your attention  
- **Organize** information into actionable categories
- **Execute** with focus and confidence
- **Review** regularly to maintain system integrity

## 🏗️ System Architecture

### Core Components

1. **Areas of Responsibility** - Your key life domains (Health, Career, Family, etc.)
2. **Projects** - Multi-step outcomes requiring planning
3. **Tasks** - Single actionable items
4. **Resources** - Reference materials and knowledge base
5. **Archive** - Completed and historical items

### Information Flow

```
Inbox → Processing → Organization → Execution → Review → Archive
```

## 📁 File Structure

All files are organized with clear naming conventions:

- **Prefix Numbers**: `00-`, `01-`, `02-` etc. for main categories
- **Project Files**: `Project - [Name].md`
- **Task Files**: `Task - [Description].md` 
- **Templates**: Use consistent frontmatter for dataview compatibility

## 🏷️ Tagging System

### Status Tags
- `#status/todo` - Not started
- `#status/in-progress` - Currently working on
- `#status/waiting` - Blocked or waiting on others
- `#status/review` - Needs review before completion
- `#status/done` - Completed

### Priority Tags
- `#priority/urgent` - Must do today
- `#priority/high` - Important this week
- `#priority/medium` - Should do this month
- `#priority/low` - Nice to have

### Context Tags
- `#context/home` - Can only be done at home
- `#context/work` - Work-related
- `#context/errand` - Requires going out
- `#context/call` - Requires phone/video call
- `#context/computer` - Requires computer access

## 🔧 Dataview Integration

This system leverages Obsidian's Dataview plugin to create dynamic views. Key frontmatter fields include:

```yaml
---
status: todo
priority: high  
project: Project Name
area: Area of Responsibility
dueDate: 2025-12-31
created: 2025-10-13
tags: [inbox, review]
---
```

## 🔄 Maintenance Schedule

### Daily (5-10 minutes)
- Process inbox items
- Review today's tasks
- Update task statuses

### Weekly (30-60 minutes)  
- Complete full weekly review
- Plan upcoming week
- Review all active projects
- Clean up completed items
- Assess system effectiveness

### Monthly (1-2 hours)
- Review areas of responsibility
- Set monthly goals
- Archive old projects and tasks
- Update system templates and processes

## 🚀 Getting Started

1. **Install Required Plugins**:
   - Dataview (for dynamic views)
   - Templater (for templates)
   - Tasks (optional, for advanced task management)

2. **Set Up Your Areas**:
   - Review and customize the Areas of Responsibility template
   - Create files for each of your key life domains

3. **Capture Everything**:
   - Use the Projects Inbox and Tasks Inbox to capture all ideas
   - Process items within 24-48 hours

4. **Start Small**:
   - Focus on one area or project initially
   - Gradually expand to full system adoption

5. **Customize**:
   - Adapt templates and processes to your workflow
   - Add your own tags and categories as needed

> **Remember**: The goal is to create a system that works for you, not against you. Start simple and evolve as you learn what works best for your unique situation.