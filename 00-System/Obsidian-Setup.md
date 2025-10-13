# LifeOS Obsidian Setup Guide

## 📋 Required Plugins

### Core Plugins (Enable First)
1. **Daily Notes** - For daily review creation
2. **Templates** - Template system
3. **File Explorer** - Navigation
4. **Search** - Content discovery
5. **Quick Switcher** - Fast navigation
6. **Graph View** - Visual connections
7. **Backlinks** - Link management
8. **Outgoing Links** - Link discovery
9. **Tags Pane** - Tag management

### Community Plugins (Install via Community Plugins)
1. **Dataview** - Core query engine (CRITICAL)
   - Enable inline queries
   - Enable JavaScript queries
2. **Templater** - Advanced templating (CRITICAL)
   - Template folder: `00-System/Templates`
   - Enable system commands
3. **Tasks** - Task management (CRITICAL)
   - Enable global task collection
4. **Calendar** - Date navigation
5. **Periodic Notes** - Weekly/Monthly/Quarterly notes
6. **Buttons** - Interactive elements
7. **Meta Bind** - Dynamic frontmatter inputs
8. **Tag Wrangler** - Tag management
9. **Folder Note** - Folder-level overviews
10. **QuickAdd** - Quick capture workflows
11. **Kanban** - Project boards
12. **Advanced Tables** - Better table management
13. **Hover Editor** - Enhanced note viewing

## ⚙️ Configuration

### Dataview Settings
- Enable inline queries
- Enable inline JS queries
- Set query timeout to 30 seconds

### Templater Settings
- Template folder: `00-System/Templates`
- Enable system command execution
- Enable user script functions
- Auto-run templates on new file creation

### Tasks Settings
- Enable global task collection
- Set done date on completion
- Enable task scheduling

### Periodic Notes Settings
- Daily notes: Format `YYYY-MM-DD`, folder `Reviews/Days`
- Weekly notes: Format `YYYY-[W]WW`, folder `Reviews/Weeks`
- Monthly notes: Format `YYYY-MM`, folder `Reviews/Months`
- Quarterly notes: Format `YYYY-[Q]Q`, folder `Reviews/Quarters`
- Yearly notes: Format `YYYY`, folder `Reviews/Years`

### Calendar Settings
- Configure to show Periodic Notes
- Link to weekly review notes

## 🗂️ Folder Structure Verification

Your vault should have this structure:

```
vault/
├── 00-System/
│   ├── Templates/          # All database templates
│   ├── Scripts/           # Future automation scripts
│   ├── Dashboards/        # Workbench, Observatory, Forge
│   └── Obsidian-Setup.md  # This file
├── Logs/
│   ├── Subjective/        # Emotional/psychological logs
│   ├── Relational/        # Relationship interactions
│   ├── Systemic/          # Operational issues
│   ├── Activity/          # Time tracking
│   └── Diet/              # Nutrition tracking
├── Reviews/
│   ├── Days/              # Daily synthesis notes
│   ├── Weeks/             # Weekly review notes
│   ├── Months/            # Monthly strategic reviews
│   ├── Quarters/          # Quarterly strategic reviews
│   └── Years/             # Annual reviews
├── Strategy/
│   ├── Values/            # Core principles
│   ├── Vision/            # Long-term aspirations
│   ├── AnnualGoals/       # Yearly objectives
│   ├── QuarterlyGoals/    # 90-day OKRs
│   └── FailureScenarios/  # Risk management
├── Projects/              # Active project folders
├── People/                # Relationship profiles
├── Notes/                 # General knowledge
├── MOCs/                  # Maps of Content
└── Resources/
    ├── Documents/         # Important files
    └── Attachments/       # Media and attachments
```

## 🚀 Quick Start Workflow

### 1. Daily Setup
1. Open Daily Notes (creates today's note)
2. Use Templater
