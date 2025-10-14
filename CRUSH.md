# LifeOS Obsidian System Commands

## Template Creation Commands
- Create new daily note: Use Templater with daily-note.md template
- Create new subjective journal: Use Templater with subjective-journal.md template  
- Create new relational journal: Use Templater with relational-journal.md template
- Create new systemic journal: Use Templater with systemic-journal.md template
- Create new activity log: Use Templater with activity-log.md template
- Create new diet log: Use Templater with diet-log.md template
- Create new task: Use Templater with task-template.md template
- Create new person: Use Templater with people-template.md template

## Dataview Queries for Dashboard Views
- Daily atomic logs rollup: Query from respective log folders with date filtering
- Weekly aggregation: Query Days with week containing period
- Monthly financial summary: Query Financial Log with month relations
- Task sprint status: Filter by sprint_status property
- People reconnection reminders: Filter by reconnect_by date

## YAML Property Structure
All templates follow the universal YAML structure with:
- Core properties (title, date, type, id, created)
- Hierarchy properties (hierarchy_level, parent_entities, child_entities, sibling_entities)
- Strategic alignment properties (strategic_alignment, related_time_periods)
- Database-specific properties matching Notion LifeOS schema
- Computed fields for Dataview aggregation

## Dashboard Structure
- Engine-Room.md: Systemic issues and operational intelligence
- Forge.md: Project and task management  
- Observatory.md: Strategic planning and review cycles
- Workbench.md: Daily command center and quick actions

## Data Flow Architecture
Atomic Logs → Days (15 AI Synthesis) → Weeks → Months → Quarters → Years
Strategic Cascade: Values → Vision → Annual Goals → Quarterly Goals → Projects → Tasks → Days