# LifeOS Obsidian Migration Blueprint

## Executive Architecture Summary

Your LifeOS operates on a **dual-hierarchy convergence model**: temporal review cycles (bottom-up synthesis) intersecting with strategic operational systems (top-down execution), creating a dynamic junction point that reveals "what matters most right now."

---

## I. SYSTEM ARCHITECTURE

### A. Primary Systems Hierarchy

```
1. THE WORKBENCH (Dashboard Layer)
   ↓
2. THE OBSERVATORY (Strategic Layer)
   ↓
3. THE FORGE (Execution Layer)
   ↓
4. THE ENGINE ROOM (Resource Layer)
```

### B. Data Flow Architecture

```
ATOMIC CAPTURE → SYNTHESIS → STRATEGY → EXECUTION

[Logs] → [Days] → [Weeks] → [Months] → [Quarters] → [Years]
   ↕         ↕        ↕          ↕           ↕           ↕
[Tasks] ← [Projects] ← [Q-Goals] ← [Annual Goals] ← [Vision] ← [Values]
```

**Critical Flow Pattern:**

- **Upward Flow (Synthesis)**: Atomic logs roll up into temporal reviews
- **Downward Flow (Execution)**: Strategic intent cascades into tactical actions
- **Convergence Point**: Each review cycle correlates with operational systems to identify priority actions

---

## II. DATABASE SCHEMAS

### A. ATOMIC LOGS LAYER

### 1. Subjective Journal

**Purpose**: Internal emotional/psychological states

```yaml
Schema:
  - title: text (entry content)
  - date: datetime
  - primary_emotion: select
    options: [Motivated, Confident, Satisfied, Grateful, Excited, 
              Focused, Connected, Stressed, Anxious, Frustrated, 
              Disappointed, Insecure, Lonely, Reflective, Uncertain]
  - secondary_emotion: select (same options)
  - days: relation → Days
  - id: auto-increment

Obsidian Implementation:
  - Folder: /Logs/Subjective/
  - Template: [subjective-journal-template.md](http://subjective-journal-template.md)
  - Frontmatter:
      date: {{date}}:{{time}}
      primary_emotion: 
      secondary_emotion:
      days: "[[YYYY-MM-DD]]"
```

### 2. Relational Journal

**Purpose**: Interpersonal interactions tracking

```yaml
Schema:
  - title: text (interaction summary)
  - date: datetime
  - people: relation → People
  - emotional_tone: select
    options: [Loving, Collaborative, Friendly, Neutral, 
              Negotiating, Antagonistic, Negative]
  - power_balance: select
    options: [Equal, Unequal-I-have-more, Unequal-They-have-more]
  - days: relation → Days
  - id: auto-increment

Obsidian Implementation:
  - Folder: /Logs/Relational/
  - Template: [relational-journal-template.md](http://relational-journal-template.md)
  - Frontmatter:
      date: {{date}}:{{time}}
      people: ["[[Person Name]]"]
      emotional_tone:
      power_balance:
      days: "[[YYYY-MM-DD]]"
```

### 3. Systemic Journal

**Purpose**: Operational issues/incidents tracking

```yaml
Schema:
  - title: text (issue description)
  - date: datetime
  - status: status
    groups:
      to_do: [AI-Generated, Triage]
      in_progress: [Escalated]
      complete: [Resolved, Archived]
  - impact: select
    options: [P1-Critical, P2-High, P3-Medium, P4-Low, P5-Note]
  - system_domain: select
    options: [Psychological, Physiological, Operational, 
              Relational, Financial]
  - tasks: relation → Tasks
  - failure_scenarios: relation → Failure Scenarios
  - projects: relation → Projects
  - ai_generated_report: long-text
  - created_time: datetime (auto)
  - id: auto-increment

Obsidian Implementation:
  - Folder: /Logs/Systemic/
  - Template: [systemic-journal-template.md](http://systemic-journal-template.md)
  - Frontmatter:
      date: {{date}}:{{time}}
      status: Triage
      impact:
      system_domain:
      tasks: []
      failure_scenarios: []
      projects: []
      id: 
```

### 4. Activity Log

**Purpose**: Time and activity tracking

```yaml
Schema:
  - title: text (activity name)
  - date: datetime
  - duration: number
  - activity_type: relation → Activity Types
  - days: relation → Days

Obsidian Implementation:
  - Use TimeTracker or ActivityWatch plugin
  - Export to /Logs/Activity/[YYYY-MM-DD-activity.md](http://YYYY-MM-DD-activity.md)
```

### 5. Diet Log

**Purpose**: Nutritional tracking

```yaml
Schema:
  - title: text (meal/food)
  - date: datetime
  - meal_type: select [Breakfast, Lunch, Dinner, Snack]
  - days: relation → Days

Obsidian Implementation:
  - Folder: /Logs/Diet/
  - Daily note section or separate entries
```

---

### B. REVIEW CYCLES LAYER

### 1. Days Database

**Purpose**: Daily synthesis hub - the atomic unit of review

```yaml
Schema:
  - title: text (format: "YYYY-MM-DD" or day name)
  - date: date (computed from title)
  - day_number: number (1-365/366)
  - day_name: formula (Monday, Tuesday, etc.)
  - year: number
  
  # Relations to logs (rollup sources)
  - subjective_journal: relation → Subjective Journal
  - relational_journal: relation → Relational Journal
  - activity_logs: relation → Activity Log
  - diet_log: relation → Diet Log
  
  # Synthesis perspectives (15+ AI-generated reports)
  - day_synthesis: long-text (general)
  - the_witness: long-text (awareness/observation)
  - the_logos_inquisitor: long-text (rational analysis)
  - the_alpha_scanner: long-text (opportunities)
  - the_structural_integrator: long-text (systems thinking)
  - the_ascension_architect: long-text (growth/development)
  - the_mythopoetic_weaver: long-text (narrative/meaning)
  - the_somatic_arbiter: long-text (body wisdom)
  - the_state_hacker: long-text (consciousness states)
  - the_capital_strategist: long-text (financial)
  - the_hearth_tender: long-text (home/family)
  - the_network_weaver: long-text (relationships)
  - the_stillness_warden: long-text (peace/calm)
  - the_aesthetic_calibrator: long-text (beauty/design)
  - the_legacy_tender: long-text (long-term impact)
  - the_systemic_navigator: long-text (operational)
  
  # Oracle/Phoenix/Sovereign syntheses (meta-perspectives)
  - day_oracle_synthesis: long-text (wisdom)
  - day_phoenix_synthesis: long-text (transformation)
  - day_sovereign_synthesis: long-text (power/agency)
  
  # Review prompts
  - night_wind_down: long-text (evening reflection)
  
  # Rollup relations
  - weeks: relation → Weeks
  - months: relation → Months

Obsidian Implementation:
  - Folder: /Reviews/Days/
  - File naming: [YYYY-MM-DD.md](http://YYYY-MM-DD.md)
  - Use Daily Notes core plugin
  - Dataview queries to aggregate logs:
  
```

TABLE WITHOUT ID

[file.link](http://file.link) as "Entry",

primary_emotion as "Emotion"

FROM "Logs/Subjective"

WHERE contains(days, [this.file.name](http://this.file.name))

```

- Templater script for synthesis generation:
  • Call LLM API with day's logs as context
  • Generate 15 perspective reports
  • Insert into daily note sections
```

### 2. Weeks Database

**Purpose**: Weekly planning and review cycle

```yaml
Schema:
  - title: text (format: "YY-WNN" e.g., "25-W41")
  - week_number: number (1-52)
  - year: number
  - week_start_date: date
  - week_end_date: date
  
  # Synthesis
  - week_synthesis: long-text
  - key_insights: long-text
  - wins: long-text
  - challenges: long-text
  - lessons_learned: long-text
  
  # Relations
  - days: relation → Days (rollup: 7 days)
  - tasks: relation → Tasks
  - projects: relation → Projects
  - months: relation → Months
  - quarters: relation → Quarters
  
  # Status
  - status: select [Planning, Active, Complete]

Obsidian Implementation:
  - Folder: /Reviews/Weeks/
  - File naming: [YYYY-Wnn.md](http://YYYY-Wnn.md)
  - Template: [week-review-template.md](http://week-review-template.md)
  - Dataview aggregation:
  
```

TABLE WITHOUT ID

day_synthesis as "Daily Synthesis"

FROM "Reviews/Days"

WHERE week = [this.file.name](http://this.file.name)

SORT [file.name](http://file.name) ASC

```

```

### 3. Months Database

**Purpose**: Monthly review cycle

```yaml
Schema:
  - title: text (format: "YY-MNN" e.g., "25-M10")
  - month_number: number (1-12)
  - year: number
  - month_start_date: date
  - month_end_date: date
  
  # Synthesis
  - month_synthesis: long-text
  - monthly_theme: text
  - major_outcomes: long-text
  - metrics_review: long-text
  
  # Relations
  - weeks: relation → Weeks (rollup: 4-5 weeks)
  - days: relation → Days
  - projects: relation → Projects
  - quarters: relation → Quarters
  
  # Status
  - status: select [Planning, Active, Complete]

Obsidian Implementation:
  - Folder: /Reviews/Months/
  - File naming: [YYYY-Mnn.md](http://YYYY-Mnn.md)
```

### 4. Quarters Database

**Purpose**: Quarterly strategic review cycle

```yaml
Schema:
  - title: text (format: "YY-QN" e.g., "25-Q4")
  - quarter_number: number (1-4)
  - year: number
  - quarter_start_date: date
  - quarter_end_date: date
  
  # Synthesis
  - quarter_synthesis: long-text
  - quarterly_theme: text
  - strategic_shifts: long-text
  - okr_review: long-text
  
  # Relations
  - months: relation → Months (rollup: 3 months)
  - weeks: relation → Weeks
  - quarterly_goals: relation → Quarterly Goals
  - years: relation → Years
  
  # Status
  - status: select [Planning, Active, Complete]

Obsidian Implementation:
  - Folder: /Reviews/Quarters/
  - File naming: [YYYY-Qn.md](http://YYYY-Qn.md)
```

### 5. Years Database

**Purpose**: Annual review cycle

```yaml
Schema:
  - title: text (format: "YYYY")
  - year: number
  
  # Synthesis
  - year_synthesis: long-text
  - annual_theme: text
  - year_in_review: long-text
  
  # Relations
  - quarters: relation → Quarters (rollup: 4 quarters)
  - annual_goals: relation → Annual Goals

Obsidian Implementation:
  - Folder: /Reviews/Years/
  - File naming: [YYYY.md](http://YYYY.md)
```

---

### C. OPERATIONAL/STRATEGIC LAYER

### 1. Values & Core Principles

**Purpose**: Foundation layer - immutable truths

```yaml
Schema:
  - title: text (principle name)
  - core_tenet: long-text (philosophical statement)
  - the_commitment: long-text (what you commit to)
  - the_boundary: long-text (what you won't do)
  - shadow_expression: long-text (pathological form)
  - litmus_test: long-text (how to know you're aligned)
  - status: status [Active, Archived]
  
  # Relations
  - life_aspects: relation → Life Aspects
  - vision: relation → Vision
  
  # Rollups
  - annual_goals: rollup (via Vision)

Obsidian Implementation:
  - Folder: /Strategy/Values/
  - One note per principle
  - Frontmatter-based
```

### 2. Life Aspects

**Purpose**: Domain categorization

```yaml
Schema:
  - title: text (aspect name: Financial, Social, Intelligence, etc.)
  - vision: relation → Vision
  - values: relation → Values & Core Principles

Obsidian Implementation:
  - Folder: /Strategy/LifeAspects/
  - MOC (Map of Content) structure
```

### 3. Vision

**Purpose**: Long-term aspirational states by domain

```yaml
Schema:
  - title: text (vision statement title)
  - vision_statement: long-text (detailed description)
  - guiding_question: text
  - strategic_pillars: multi-select
  - priority: select [⭐⭐⭐⭐⭐, ⭐⭐⭐⭐, ⭐⭐⭐, ⭐⭐, ⭐]
  - status: status [Planning, On-Hold, In-Progress, Actualized]
  
  # Dates
  - review_date: date (with reminder)
  - last_review_date: date
  
  # Relations
  - life_aspects: relation → Life Aspects
  - values: relation → Values & Core Principles
  - annual_goals: relation → Annual Goals
  
  # Rollups
  - quarterly_goals: rollup (via Annual Goals)

Obsidian Implementation:
  - Folder: /Strategy/Vision/
  - Dataview table on Life Aspects MOCs
```

### 4. Annual Goals

**Purpose**: Yearly objectives (The Epic)

```yaml
Schema:
  - title: text (annual theme/goal name)
  - goal_archetype: select
    options: [Build, Achieve, Become, Eliminate]
  - strategic_intent: long-text (why this matters)
  - strategic_approach: long-text (how to achieve it)
  - the_epic: long-text (inspirational narrative)
  - target_value: text (measurable outcome)
  - success_condition: text (definition of done)
  - key_risks: long-text
  - status: status [Draft, Active, Achieved, Not-Achieved, Archived]
  
  # Relations
  - vision: relation → Vision
  - years: relation → Years
  - quarterly_goals: relation → Quarterly Goals
  - primary_metric: relation → Key Metrics
  
  # Computed
  - current_annual_goal: formula (is this year?)
  - goal_progress: formula (percentage)
  - planned_range: formula (date range)

Obsidian Implementation:
  - Folder: /Strategy/AnnualGoals/
  - Frontmatter + long-form content
  - Dataview progress tracking:
  
```

TABLE

goal_archetype,

status,

goal_progress

FROM "Strategy/AnnualGoals"

WHERE status = "Active"

```

```

### 5. Quarterly Goals

**Purpose**: 90-day OKR-style objectives

```yaml
Schema:
  - title: text (quarterly objective)
  - key_result_1: text
  - key_result_2: text
  - key_result_3: text
  - key_learning: long-text
  - status: status
    groups:
      to_do: [Planning]
      in_progress: [On-Hold, At-Risk, Off-Track, On-Track]
      complete: [Done]
  
  # Relations
  - annual_goals: relation → Annual Goals
  - quarters: relation → Quarters
  - projects: relation → Projects
  - failure_scenarios: relation → Failure Scenarios
  
  # Computed
  - current_quarter_goal: formula
  - goal_progress: formula
  - health: formula (red/yellow/green)

Obsidian Implementation:
  - Folder: /Strategy/QuarterlyGoals/
  - Link from quarterly review notes
```

### 6. Projects

**Purpose**: Multi-task initiatives with constraints

```yaml
Schema:
  - title: text (project name)
  - project_summary: long-text
  - priority: select [⭐⭐⭐⭐⭐ to ⭐]
  - status: status
    groups:
      to_do: [Cancelled, Someday-Maybe, On-Hold]
      in_progress: [Delegated, Active]
      complete: [Done]
  
  # Dates
  - project_start: date
  - deadline: date
  - review_date: date (with reminder)
  
  # Constraints
  - hard_constraints_antigoals: long-text
  - kpis: long-text
  - kpi_bar: number (progress %)
  
  # Relations
  - quarterly_goals: relation → Quarterly Goals
  - tasks: relation → Tasks
  - people: relation → People
  - notes: relation → Notes Management
  - documents: relation → Documents
  - competencies: relation → Competency Arsenal
  - systemic_journal: relation → Systemic Journal
  
  # Computed
  - health: formula
  - project_progress: formula

Obsidian Implementation:
  - Folder: /Projects/
  - Sub-folders for tertiary systems:
      /Projects/Intelligence-Integration/
      /Projects/Architecture/
      /Projects/Content-Creation/
      /Projects/ConsciRise/
  - Each project = folder with [index.md](http://index.md) + task notes
  - Tasks plugin or custom task management
```

### 7. Tasks

**Purpose**: Atomic actionable items

```yaml
Schema:
  - title: text (task description)
  - description: long-text
  - status: status
    groups:
      to_do: [Waiting, Paused, Delegated, Up-Next]
      in_progress: [Active, Focus]
      complete: [Done, Cancelled, Archived]
  - priority: select [⭐⭐⭐⭐⭐ to ⭐]
  - action_date: date (with reminder 9am)
  - assignee: person
  
  # Relations
  - projects: relation → Projects (limit: 1)
  - weeks: relation → Weeks
  - systemic_journal: relation → Systemic Journal
  
  # Rollups
  - project_status: rollup (from Projects)
  
  # Computed
  - sprint_status: formula (Current/Next1-4/Backlog)
  - monitor: formula (alert status)

Obsidian Implementation:
  - Use Tasks plugin or Dataview task queries
  - Inline tasks in project notes or daily notes:
  
```

- [ ]  Task name #project/[[ProjectName]] #priority/⭐⭐⭐⭐ 📅 2025-10-15

```

- Sprint view via Dataview:

```

TASK

WHERE contains(text, "#sprint/current")

GROUP BY project

```

```

### 8. Failure Scenarios

**Purpose**: Proactive risk management (Anti-Goals)

```yaml
Schema:
  - title: text (scenario description)
  - the_antigoal: long-text (what you're avoiding)
  - type: select
    options: [Internal-Psychological, Internal-Behavioral,
              External-Systemic, External-Relational]
  - impact: select [🔴 High, 🟡 Medium, 🟢 Low]
  - likelihood: select [🔴 High, 🟡 Medium, 🟢 Low]
  - status: status
    groups:
      to_do: [AI-Generated, Identified]
      in_progress: [Active-Monitoring, Materializing, Containing]
      complete: [Contained, Archived]
  
  # Assessment
  - early_warning_signs: long-text
  - proactive_protocol: long-text (prevention)
  - reactive_protocol: long-text (mitigation)
  - post_mortem_debrief: long-text (lessons)
  - last_assessed: date
  
  # Relations
  - quarterly_goals: relation → Quarterly Goals
  - systemic_journal: relation → Systemic Journal
  
  # Computed
  - threat_level: formula (Impact × Likelihood)
  - current_quarter: formula
  - suggestions: formula (action prompts)

Obsidian Implementation:
  - Folder: /Strategy/FailureScenarios/
  - Risk matrix view via Dataview
```

---

### D. RESOURCE LAYER (Engine Room)

### 9. People Database

**Purpose**: Sophisticated relational intelligence system

```yaml
Schema:
  - title: text (person's name)
  - custom_name: text (override)
  - relationship_status: select
    options: [Family-Member, Mentor, Close-Friend, 
              Close-Acquaintance, Coworker, Acquaintance]
  - city: select [Noida, Delhi, etc.]
  
  # Intelligence profiles
  - developmental_altitude: select
    options: [LVL3-Red-Egocentric, LVL4-Amber-Conformist,
              LVL5-Orange-Rational, LVL6-Green-Pluralistic,
              LVL7-Turquoise-Integral]
  - primary_center_intelligence: select
    options: [Cognitive, Affective, Somatic]
  - explanatory_style: select
    options: [The-Pragmatist, The-Hero, The-Martyr, The-Victim]
  - stability_profile: select
    options: [The-Anchor, The-Weaver, The-Rock, The-Warrior]
  - primary_conflict_style: select
    options: [Competing, Accommodating, Avoiding, 
              Collaborating, Compromising]
  - dominant_power_strategy: select
    options: [Directing, Collaborating, Inspiring, 
              Mastering, Gatekeeping]
  - temporal_focus: select
    options: [Operational, Tactical, Strategic, Legacy]
  - aspirational_drive: select
    options: [Security-Stability, Connection-Belonging,
              Status-Recognition, Mastery-Impact, Growth-Understanding]
  - core_shadow: select
    options: [Fear-of-Insignificance, Fear-of-Rejection,
              Fear-of-Chaos, Fear-of-Powerlessness]
  
  # Influence & engagement
  - influence_toolkit: multi-select
    options: [Strategic-Persuasion, Inspirational-Charismatic,
              Collaborative, Coercive, Elicits-Pity, Creates-Desire]
  
  # Networking
  - networking_profile: select
    options: [Key-Ally, Active-Collaborator, Mentor-Advisor,
              Protégé-Mentee, Peer-Sounding-Board, Inactive, Archive]
  - desired_trajectory: select
    options: [Deepen, Maintain, Activate, Graceful-Exit, Inactive]
  - value_exchange_balance: select
    options: [I-am-in-Credit, Balanced, I-am-in-Debt]
  
  # Connection management
  - in_days_connection_frequency: number
  - last_connected_date: formula
  - reconnect_by: formula (computed from frequency)
  
  # Context
  - origin_context: long-text
  - key_personal_intel: long-text
  - professional_domain: long-text
  - strategic_context: long-text
  - engagement_blueprint: long-text
  - summary: long-text
  
  # Relations
  - projects: relation → Projects
  - community: relation → Community
  - stories: relation → Relational Journal

Obsidian Implementation:
  - Folder: /People/
  - One note per person with extensive frontmatter
  - Dataview contact dashboard:
  
```

TABLE

relationship_status,

reconnect_by,

networking_profile

FROM "People"

WHERE reconnect_by <= date(today) + dur(7 days)

SORT reconnect_by ASC

```

```

### 10. Notes Management

**Purpose**: Knowledge capture system

```yaml
Schema:
  - title: text (note title)
  - status: status [New-Note, Live, Priority-Highlight, Archived]
  - created_time: datetime (auto)
  - last_edited_time: datetime (auto)
  
  # Relations
  - knowledge_categories: relation → Knowledge Categories
  - projects: relation → Projects
  
  # Rollup
  - project_status: rollup (from Projects)

Obsidian Implementation:
  - Standard Obsidian notes in /Notes/
  - Tag-based categories: #category/topic
  - Dataview MOCs organized by category/project
```

### 11. Knowledge Categories

**Purpose**: Topic taxonomy

```yaml
Schema:
  - title: text (category name)
  - notes: relation → Notes Management

Obsidian Implementation:
  - Tag system: #category/finance, #category/psychology
  - MOC notes in /MOCs/
```

---

## III. OBSIDIAN IMPLEMENTATION STRATEGY

### A. Folder Structure

```
vault/
├── 000-System/
│   ├── Templates/
│   │   ├── [daily-note.md](http://daily-note.md)
│   │   ├── [weekly-review.md](http://weekly-review.md)
│   │   ├── [project-template.md](http://project-template.md)
│   │   ├── [subjective-log.md](http://subjective-log.md)
│   │   ├── [relational-log.md](http://relational-log.md)
│   │   └── [systemic-log.md](http://systemic-log.md)
│   ├── Scripts/
│   │   ├── synthesis-generator.js
│   │   ├── rollup-calculator.js
│   │   └── sprint-manager.js
│   └── Dashboards/
│       ├── [Workbench.md](http://Workbench.md)
│       ├── [Observatory.md](http://Observatory.md)
│       ├── [Forge.md](http://Forge.md)
│       └── [Engine-Room.md](http://Engine-Room.md)
├── Logs/
│   ├── Subjective/
│   ├── Relational/
│   ├── Systemic/
│   ├── Activity/
│   └── Diet/
├── Reviews/
│   ├── Days/ (daily notes location)
│   ├── Weeks/
│   ├── Months/
│   ├── Quarters/
│   └── Years/
├── Strategy/
│   ├── Values/
│   ├── Vision/
│   ├── AnnualGoals/
│   ├── QuarterlyGoals/
│   └── FailureScenarios/
├── Projects/
│   ├── Intelligence-Integration/
│   ├── Architecture/
│   ├── Content-Creation/
│   └── ConsciRise/
├── People/
├── Notes/
├── MOCs/
└── Resources/
    ├── Documents/
    └── Attachments/
```

### B. Required Plugins

1. **Core Plugins:**
    - Daily notes
    - Templates
    - Outgoing links
    - Backlinks
2. **Community Plugins:**
    - **Dataview** - All query logic
    - **Templater** - Advanced templating with scripts
    - **Tasks** - Task management
    - **Calendar** - Temporal navigation
    - **Periodic Notes** - Weekly/monthly/quarterly notes
    - **Buttons** - Interactive elements
    - **Meta Bind** - Dynamic frontmatter inputs
    - **DB Folder** - Database-like views
    - **Kanban** - Sprint/project boards
    - **Tracker** - Habit/metric tracking
    - **Custom JS** (or QuickAdd) - Synthesis generation scripts

### C. Critical Dataview Queries

### 1. Workbench Dashboard

```
// Today's Context
const today = [dv.date](http://dv.date)("today");
const todayNote = [dv.page](http://dv.page)(`Reviews/Days/${today.toFormat("yyyy-MM-dd")}`);

dv.header(1, "The Workbench");
dv.header(2, "Today: " + today.toFormat("EEEE, MMMM d, yyyy"));

// Current Sprint Tasks
dv.header(3, "Current Sprint");
dv.taskList(
  dv.pages('"Projects"')
    .file.tasks
    .where(t => !t.completed && t.text.includes("#sprint/current"))
    .sort(t => t.priority, 'desc')
);

// Active Systemic Issues
dv.header(3, "Active Systemic Dissonances");
dv.table(
  ["Issue", "Impact", "Status"],
  dv.pages('"Logs/Systemic"')
    .where(p => p.status === "Triage" || p.status === "Escalated")
    .sort(p => p.impact, 'desc')
    .limit(5)
    .map(p => [[p.file.link](http://p.file.link), p.impact, p.status])
);

// Upcoming Reconnections
dv.header(3, "People to Reconnect With");
const reconnectSoon = dv.pages('"People"')
  .where(p => p.reconnect_by && p.reconnect_by <= [today.plus](http://today.plus)({days: 7}))
  .sort(p => p.reconnect_by, 'asc')
  .limit(5);
  
dv.table(
  ["Person", "Reconnect By", "Trajectory"],
  [reconnectSoon.map](http://reconnectSoon.map)(p => [[p.file.link](http://p.file.link), p.reconnect_by, p.desired_trajectory])
);
```

### 2. Observatory - Review Aggregation

```
// Weekly Synthesis Rollup
const weekNum = "25-W41"; // parameterize
const week = [dv.page](http://dv.page)(`Reviews/Weeks/${weekNum}`);

dv.header(2, `Week ${weekNum} Review`);

// Aggregate all days in this week
const days = dv.pages('"Reviews/Days"')
  .where(p => p.weeks && p.weeks.includes(weekNum))
  .sort(p => [p.file.name](http://p.file.name), 'asc');

dv.header(3, "Daily Syntheses");
for (let day of days) {
  dv.header(4, [day.file.name](http://day.file.name));
  dv.paragraph([day.day](http://day.day)_synthesis);
}

// Task completion rate
const tasksThisWeek = dv.pages('"Projects"')
  .file.tasks
  .where(t => t.weeks && t.weeks.includes(weekNum));
  
const completed = tasksThisWeek.where(t => t.completed).length;
const total = tasksThisWeek.length;

dv.paragraph(`**Task Completion**: ${completed}/${total} (${Math.round(completed/total*100)}%)`);
```

### 3. Strategic Alignment Check

```
// Show current Annual Goal → Quarterly Goal → Projects → Tasks hierarchy
const currentYear = [dv.date](http://dv.date)("today").year;
const currentQuarter = `${currentYear}-Q${Math.ceil([dv.date](http://dv.date)("today").month / 3)}`;

dv.header(2, "Strategic Alignment");

// Annual Goals
const annualGoals = dv.pages('"Strategy/AnnualGoals"')
  .where(p => p.status === "Active" && p.years.includes(String(currentYear)));

for (let goal of annualGoals) {
  dv.header(3, "🎯 " + goal.title);
  
  // Quarterly Goals under this annual goal
  const qGoals = dv.pages('"Strategy/QuarterlyGoals"')
    .where(p => p.annual_goals && p.annual_goals.includes([goal.file.link](http://goal.file.link)) 
                && p.quarters.includes(currentQuarter));
  
  for (let qGoal of qGoals) {
    dv.header(4, "📊 " + qGoal.title);
    dv.paragraph(`**KR1**: ${qGoal.key_result_1}`);
    dv.paragraph(`**KR2**: ${qGoal.key_result_2}`);
    dv.paragraph(`**KR3**: ${qGoal.key_result_3}`);
    
    // Projects under this quarterly goal
    const projects = dv.pages('"Projects"')
      .where(p => p.quarterly_goals && p.quarterly_goals.includes([qGoal.file.link](http://qGoal.file.link))
                  && p.status === "Active");
    
    if (projects.length > 0) {
      dv.header(5, "Active Projects:");
      dv.list([projects.map](http://projects.map)(p => [p.file.link](http://p.file.link) + " (" + p.status + ")"));
    }
  }
}
```

### D. Templater Scripts for Synthesis Generation

### Daily Synthesis Generator

```jsx
<%*
// Template: [daily-note.md](http://daily-note.md)
// Requires: Templater plugin + API access to LLM

const date = tp.file.title; // YYYY-MM-DD

// Gather all logs for this day
const subjectiveLogs = await dv.pages('"Logs/Subjective"')
  .where(p => p.days.includes(date));
const relationalLogs = await dv.pages('"Logs/Relational"')
  .where(p => p.days.includes(date));
const systemicLogs = await dv.pages('"Logs/Systemic"')
  .where(p => [p.date](http://p.date) === date);

// Compile context for LLM
const context = {
  subjective: [subjectiveLogs.map](http://subjectiveLogs.map)(l => l.file.content).join("\n\n"),
  relational: [relationalLogs.map](http://relationalLogs.map)(l => l.file.content).join("\n\n"),
  systemic: [systemicLogs.map](http://systemicLogs.map)(l => l.file.content).join("\n\n")
};

// Call LLM API for each synthesis perspective
const perspectives = [
  "the_witness", "the_logos_inquisitor", "the_alpha_scanner",
  "the_structural_integrator", "the_ascension_architect", 
  // ... all 15 perspectives
];

const syntheses = {};
for (let perspective of perspectives) {
  const prompt = `You are ${perspective}. Synthesize the following day's logs from your unique perspective:\n\n${JSON.stringify(context)}`;
  
  // API call (pseudo-code)
  syntheses[perspective] = await callLLM(prompt);
}

// Insert into template
-%>
---
date: <% tp.file.title %>
days: <% tp.file.title %>
weeks: [[<% moment(tp.file.title).format('YYYY-[W]WW') %>]]
type: daily-review
---

# <% moment(tp.file.title).format('dddd, MMMM D, YYYY') %>

## Day Synthesis
<%* tR += [syntheses.day](http://syntheses.day)_synthesis || "" %>

## The Witness
<%* tR += syntheses.the_witness || "" %>

## The Logos Inquisitor
<%* tR += syntheses.the_logos_inquisitor || "" %>

<!-- Continue for all 15 perspectives -->

## Logs
### Subjective
<%* 
for (let log of subjectiveLogs) {
  tR += `- ${[log.file.link](http://log.file.link)}: ${log.primary_emotion}\n`;
}
%>

### Relational
<%* 
for (let log of relationalLogs) {
  tR += `- ${[log.file.link](http://log.file.link)}: ${log.people.join(", ")}\n`;
}
%>

### Systemic
<%* 
for (let log of systemicLogs) {
  tR += `- ${[log.file.link](http://log.file.link)} (${log.impact})\n`;
}
%>
```

### E. Button-Based Sprint Management

Using Buttons plugin:

```markdown
# Project: EA Development

## Tasks
- [ ] Backtest Alpha 2 strategy #priority/⭐⭐⭐⭐⭐ #sprint/backlog
- [ ] Refine entry signals #priority/⭐⭐⭐⭐ #sprint/current
- [ ] Document trade logic #priority/⭐⭐⭐ #sprint/next1

```

name Move to Current Sprint

type command

action QuickAdd: Move Task to Current Sprint

```
^button-current

```

name Move to Next Sprint

type command

action QuickAdd: Move Task to Next Sprint

```
^button-next
```

---

## IV. AUTOMATION & WORKFLOW

### A. Daily Workflow

1. **Morning (Ignition)**
    - Open Workbench dashboard
    - Review today's note (auto-created by Daily Notes)
    - Check current sprint tasks
    - Review systemic issues
2. **Throughout Day (Capture)**
    - Quick-capture logs via mobile/desktop
    - Templater hotkeys for log templates
    - Activity tracking via plugin
3. **Evening (Synthesis)**
    - Run synthesis generator script
    - Review 15 perspectives
    - Add night wind-down reflection
    - Link to weekly note

### B. Weekly Workflow

1. **Sunday Evening (Review)**
    - Open Observatory dashboard
    - Create new week note (Periodic Notes)
    - Run weekly aggregation Dataview
    - Synthesize: Wins, Challenges, Lessons
    - Plan next week's sprint
2. **Monday Morning (Planning)**
    - Review quarterly goals alignment
    - Assign tasks to Current Sprint
    - Set weekly focus

### C. Monthly/Quarterly Workflow

Similar pattern with increasing strategic altitude.

### D. n8n Integration (Optional)

Since you currently use n8n for automation:

**n8n Workflow for Obsidian:**

1. Trigger: Daily cron (8 AM)
2. Fetch: Query Obsidian logs via Local REST API plugin
3. Process: Send to LLM for synthesis
4. Write: Post synthesis back to daily note
5. Notify: Send Telegram summary

---

## V. MIGRATION CHECKLIST

### Phase 1: Foundation (Week 1)

- [ ]  Set up folder structure
- [ ]  Install required plugins
- [ ]  Create templates for all databases
- [ ]  Build Workbench dashboard
- [ ]  Build Observatory dashboard

### Phase 2: Data Migration (Week 2-3)

- [ ]  Export Notion data to CSV/JSON
- [ ]  Script conversion to Markdown + frontmatter
- [ ]  Migrate logs (Subjective, Relational, Systemic)
- [ ]  Migrate review cycles (Days, Weeks, etc.)
- [ ]  Migrate strategic data (Goals, Projects, Tasks)

### Phase 3: Automation (Week 4)

- [ ]  Set up Templater scripts for synthesis
- [ ]  Configure Dataview queries
- [ ]  Test rollup logic
- [ ]  Set up n8n workflows (if applicable)
- [ ]  Create button actions for sprint management

### Phase 4: Testing & Refinement (Week 5)

- [ ]  Run full daily/weekly cycle
- [ ]  Verify data integrity
- [ ]  Optimize query performance
- [ ]  Refine dashboard layouts
- [ ]  Document personal workflows

---

## VI. KEY DIFFERENCES: NOTION vs OBSIDIAN

| Aspect | Notion | Obsidian |
| --- | --- | --- |
| **Data Model** | Relational databases | File-based with frontmatter |
| **Relations** | Native multi-select | Dataview queries + links |
| **Rollups** | Automatic | Dataview computed |
| **Formulas** | Built-in | Dataview/JS custom functions |
| **Buttons** | API-based | Plugin-based actions |
| **Syncing** | Cloud-native | Local-first (sync via plugin) |
| **Mobile** | Native app | Community app (limited) |
| **AI Integration** | Built-in | API calls via scripts |

**Advantages of Obsidian:**

- Full data ownership (plain text)
- Faster performance (local)
- Infinite extensibility (plugins/scripts)
- Graph view for emergent insights
- No vendor lock-in

**Challenges:**

- More technical setup required
- Manual query optimization
- Steeper learning curve for Dataview

---

This blueprint provides the complete technical specification to rebuild your LifeOS in Obsidian while preserving its sophisticated systemic intelligence. The key is maintaining the dual-hierarchy convergence: logs → synthesis → reviews flowing upward, while strategy → goals → tasks flows downward, meeting at the junction point that reveals "what matters most right now."