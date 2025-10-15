# Atomic Logs FileClass Definitions

Place these in your FileClass folder. Each defines the field schema for atomic log entries.

---
## FileClass-SubjectiveJournal.md

```yaml
---
extends: base-entity
mapWithTag: true
tagNames: [subjective-journal]
filesPaths: ["01-Subjective-Journal"]

fields:
  - name: sj_date
    type: DateTime
    options:
      dateFormat: "YYYY-MM-DDTHH:mm"

  - name: sj_primary_emotion
    type: Select
    options:
      valuesList:
        "0": "Motivated"
        "1": "Confident"
        "2": "Satisfied"
        "3": "Grateful"
        "4": "Excited"
        "5": "Focused"
        "6": "Connected"
        "7": "Stressed"
        "8": "Anxious"
        "9": "Frustrated"
        "10": "Disappointed"
        "11": "Insecure"
        "12": "Lonely"
        "13": "Reflective"
        "14": "Uncertain"

  - name: sj_secondary_emotion
    type: Select
    options:
      valuesList:
        "0": "Motivated"
        "1": "Confident"
        "2": "Satisfied"
        "3": "Grateful"
        "4": "Excited"
        "5": "Focused"
        "6": "Connected"
        "7": "Stressed"
        "8": "Anxious"
        "9": "Frustrated"
        "10": "Disappointed"
        "11": "Insecure"
        "12": "Lonely"
        "13": "Reflective"
        "14": "Uncertain"

  - name: sj_days
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"06-Days\"')"

  - name: sj_total_context
    type: Lookup
    options:
      queryTemplate: "dv.current().file.link"

  - name: sj_id
    type: Number
---
```

---
## FileClass-RelationalJournal.md

```yaml
---
extends: base-entity
mapWithTag: true
tagNames: [relational-journal]
filesPaths: ["02-Relational-Journal"]

fields:
  - name: rj_date
    type: DateTime
    options:
      dateFormat: "YYYY-MM-DDTHH:mm"

  - name: rj_people
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"17-People\"')"

  - name: rj_emotional_tone
    type: Select
    options:
      valuesList:
        "0": "Loving"
        "1": "Collaborative"
        "2": "Friendly"
        "3": "Neutral"
        "4": "Negotiating"
        "5": "Antagonistic"
        "6": "Negative"

  - name: rj_power_balance
    type: Select
    options:
      valuesList:
        "0": "Equal"
        "1": "Unequal - I have more"
        "2": "Unequal - They have more"

  - name: rj_days
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"06-Days\"')"

  - name: rj_relationship_status
    type: Lookup
    options:
      queryTemplate: "dv.pages('\"17-People\"').where(p => dv.current().rj_people?.includes(p.file.link)).relationship_status"

  - name: rj_total_context
    type: Lookup
    options:
      queryTemplate: "dv.current().file.link"

  - name: rj_id
    type: Number
---
```

---
## FileClass-SystemicJournal.md

```yaml
---
extends: base-entity
mapWithTag: true
tagNames: [systemic-journal]
filesPaths: ["03-Systemic-Journal"]

fields:
  - name: sysj_date
    type: DateTime
    options:
      dateFormat: "YYYY-MM-DDTHH:mm"

  - name: sysj_status
    type: Select
    options:
      valuesList:
        "0": "AI Generated"
        "1": "Triage"
        "2": "Escalated"
        "3": "Resolved"
        "4": "Archived"

  - name: sysj_impact
    type: Select
    options:
      valuesList:
        "0": "P1: Critical"
        "1": "P2: High"
        "2": "P3: Medium"
        "3": "P4: Low"
        "4": "P5: Note"

  - name: sysj_system_domain
    type: Select
    options:
      valuesList:
        "0": "Psychological"
        "1": "Physiological"
        "2": "Operational"
        "3": "Relational"
        "4": "Financial"

  - name: sysj_ai_generated_report
    type: Input

  - name: sysj_tasks
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"16-Tasks\"')"

  - name: sysj_failure_scenarios
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"24-Failure-Scenarios\"')"

  - name: sysj_projects
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"15-Projects\"')"

  - name: sysj_systemic_report
    type: Formula
    options:
      formula: "this.sysj_impact + ' - ' + this.sysj_system_domain + ' - ' + this.sysj_status"

  - name: sysj_created_time
    type: DateTime
    options:
      dateFormat: "YYYY-MM-DDTHH:mm:ss"

  - name: sysj_id
    type: Number
---
```

---
## FileClass-ActivityLog.md

```yaml
---
extends: base-entity
mapWithTag: true
tagNames: [activity-log]
filesPaths: ["04-Activity-Log"]

fields:
  - name: al_date
    type: DateTime
    options:
      dateFormat: "YYYY-MM-DDTHH:mm"

  - name: al_habit_quality
    type: Select
    options:
      valuesList:
        "0": "0.1"
        "1": "0.2"
        "2": "0.3"
        "3": "0.4"
        "4": "0.5"
        "5": "0.6"
        "6": "0.7"
        "7": "0.8"
        "8": "0.9"
        "9": "1.0"

  - name: al_days
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"06-Days\"')"

  - name: al_activity_type
    type: Select
    options:
      valuesList:
        "0": "Work - Editing"
        "1": "Work - Social Media"
        "2": "Work - Strategy"
        "3": "Work - Admin"
        "4": "Exercise"
        "5": "Reading"
        "6": "Social"
        "7": "Rest"
        "8": "Learning"
        "9": "Creative"
        "10": "Maintenance"

  - name: al_activity_notes
    type: Input

  - name: al_duration
    type: Formula
    options:
      formula: "const start = new Date(this.al_date); const end = new Date(this.al_date_end || this.al_date); return ((end - start) / (1000 * 60 * 60)).toFixed(2) + ' hours';"

  - name: al_date_end
    type: DateTime
    options:
      dateFormat: "YYYY-MM-DDTHH:mm"

  - name: al_habit
    type: Input

  - name: al_id
    type: Number
---
```

---
## FileClass-DietLog.md

```yaml
---
extends: base-entity
mapWithTag: true
tagNames: [diet-log]
filesPaths: ["05-Diet-Log"]

fields:
  - name: dl_date
    type: DateTime
    options:
      dateFormat: "YYYY-MM-DDTHH:mm"

  - name: dl_meal_type
    type: Select
    options:
      valuesList:
        "0": "Breakfast"
        "1": "Lunch"
        "2": "Dinner"
        "3": "Snack"
        "4": "Brunch"

  - name: dl_days
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"06-Days\"')"

  - name: dl_total_context
    type: Lookup
    options:
      queryTemplate: "dv.current().file.link"

  - name: dl_id
    type: Number
---
```

---

# Implementation Notes

## Metadata Menu Setup

1. **FileClass Folder**: Create these as separate `.md` files in your configured FileClass folder (e.g., `00-System/FileClasses/`)

2. **Mapping Strategy**: Each uses `mapWithTag: true` and `filesPaths` for automatic FileClass assignment

3. **Field Naming**: Prefixes match your template structure:
   - `sj_` = Subjective Journal
   - `rj_` = Relational Journal
   - `sysj_` = Systemic Journal
   - `al_` = Activity Log
   - `dl_` = Diet Log

## Formula Fields

- **al_duration**: Calculates time difference between start/end dates
- **sysj_systemic_report**: Concatenates key fields for quick reference
- **Lookup fields**: Use Dataview queries to pull related data

## Relation Fields

All `MultiFile` fields use Dataview query strings to:
- Filter by folder path
- Enable autocomplete with valid targets
- Maintain bidirectional relationships

## Next Steps

1. Create these FileClass files in your vault
2. Reload Metadata Menu plugin
3. Test field assignment by creating a new log entry
4. Verify autocomplete and relation functionality