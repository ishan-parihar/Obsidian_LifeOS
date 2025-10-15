# Review Cycles FileClass Definitions

These FileClasses define the temporal hierarchy with 15 Intelligence Synthesis Units at each level.

---
## FileClass-Days.md

```yaml
---
extends: base-entity
mapWithTag: true
tagNames: [daily-review]
filesPaths: ["06-Days"]
maxRecordsPerPage: 31

fields:
  # Core Temporal Fields
  - name: daily_date
    type: Date
    options:
      dateFormat: "YYYY-MM-DD"

  - name: daily_day_name
    type: Formula
    options:
      formula: "const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']; return days[new Date(this.daily_date).getDay()];"

  - name: daily_day_number
    type: Formula
    options:
      formula: "const start = new Date(new Date(this.daily_date).getFullYear(), 0, 0); const diff = new Date(this.daily_date) - start; return Math.floor(diff / (1000 * 60 * 60 * 24));"

  - name: daily_year
    type: Formula
    options:
      formula: "return new Date(this.daily_date).getFullYear();"

  - name: daily_time_period_start
    type: Date
    options:
      dateFormat: "YYYY-MM-DD"

  - name: daily_time_period_end
    type: Date
    options:
      dateFormat: "YYYY-MM-DD"

  # Hierarchical Relations
  - name: daily_weeks
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"07-Weeks\"')"

  - name: daily_months
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"08-Months\"')"

  - name: daily_quarters
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"09-Quarters\"')"

  - name: daily_years
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"10-Years\"')"

  # Evening Reflection
  - name: daily_night_wind_down
    type: Input

  # 15 Intelligence Synthesis Units
  - name: daily_day_synthesis
    type: Input

  - name: daily_the_witness
    type: Input

  - name: daily_the_logos_inquisitor
    type: Input

  - name: daily_the_alpha_scanner
    type: Input

  - name: daily_the_structural_integrator
    type: Input

  - name: daily_the_ascension_architect
    type: Input

  - name: daily_the_mythopoetic_weaver
    type: Input

  - name: daily_the_somatic_arbiter
    type: Input

  - name: daily_the_state_hacker
    type: Input

  - name: daily_the_capital_strategist
    type: Input

  - name: daily_the_hearth_tender
    type: Input

  - name: daily_the_network_weaver
    type: Input

  - name: daily_the_stillness_warden
    type: Input

  - name: daily_the_aesthetic_calibrator
    type: Input

  - name: daily_the_legacy_tender
    type: Input

  - name: daily_the_systemic_navigator
    type: Input

  # Meta-Synthesis
  - name: daily_day_oracle_synthesis
    type: Input

  - name: daily_day_phoenix_synthesis
    type: Input

  - name: daily_day_sovereign_synthesis
    type: Input

  # Status
  - name: daily_status
    type: Formula
    options:
      formula: "const synthCount = [this.daily_the_witness, this.daily_the_logos_inquisitor, this.daily_the_alpha_scanner, this.daily_the_structural_integrator, this.daily_the_ascension_architect, this.daily_the_mythopoetic_weaver, this.daily_the_somatic_arbiter, this.daily_the_state_hacker, this.daily_the_capital_strategist, this.daily_the_hearth_tender, this.daily_the_network_weaver, this.daily_the_stillness_warden, this.daily_the_aesthetic_calibrator, this.daily_the_legacy_tender, this.daily_the_systemic_navigator].filter(x => x && x.length > 0).length; return synthCount >= 10 ? 'Complete' : synthCount >= 5 ? 'In Progress' : 'Not Started';"

  - name: daily_day_report
    type: Formula
    options:
      formula: "return '[[' + this.file.name + ']]';"
---
```

---
## FileClass-Weeks.md

```yaml
---
extends: base-entity
mapWithTag: true
tagNames: [weekly-review]
filesPaths: ["07-Weeks"]
maxRecordsPerPage: 52

fields:
  # Core Temporal Fields
  - name: weekly_week_number
    type: Number

  - name: weekly_year
    type: Number

  - name: weekly_time_period_start
    type: Date
    options:
      dateFormat: "YYYY-MM-DD"

  - name: weekly_time_period_end
    type: Date
    options:
      dateFormat: "YYYY-MM-DD"

  # Hierarchical Relations
  - name: weekly_months
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"08-Months\"')"

  - name: weekly_quarters
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"09-Quarters\"')"

  - name: weekly_years
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"10-Years\"')"

  - name: weekly_days
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"06-Days\"')"

  # Task Tracking
  - name: weekly_tasks
    type: Lookup
    options:
      queryTemplate: "dv.pages('\"16-Tasks\"').where(t => t.weeks?.includes(dv.current().file.link))"

  # Financial Tracking
  - name: weekly_financial_log
    type: Lookup
    options:
      queryTemplate: "dv.pages('\"20-Financial-Log\"').where(f => f.fl_weeks?.includes(dv.current().file.link))"

  # 15 Intelligence Synthesis Units
  - name: weekly_week_synthesis
    type: Input

  - name: weekly_the_witness
    type: Input

  - name: weekly_the_logos_inquisitor
    type: Input

  - name: weekly_the_alpha_scanner
    type: Input

  - name: weekly_the_structural_integrator
    type: Input

  - name: weekly_the_ascension_architect
    type: Input

  - name: weekly_the_mythopoetic_weaver
    type: Input

  - name: weekly_the_somatic_arbiter
    type: Input

  - name: weekly_the_state_hacker
    type: Input

  - name: weekly_the_capital_strategist
    type: Input

  - name: weekly_the_hearth_tender
    type: Input

  - name: weekly_the_network_weaver
    type: Input

  - name: weekly_the_stillness_warden
    type: Input

  - name: weekly_the_aesthetic_calibrator
    type: Input

  - name: weekly_the_legacy_tender
    type: Input

  - name: weekly_the_systemic_navigator
    type: Input

  # Meta-Synthesis
  - name: weekly_week_oracle_synthesis
    type: Input

  - name: weekly_week_phoenix_synthesis
    type: Input

  - name: weekly_week_sovereign_synthesis
    type: Input

  # Reflection
  - name: weekly_key_learnings
    type: Input

  # Financial Aggregation (Formulas)
  - name: weekly_total_income
    type: Formula
    options:
      formula: "return dv.pages('\"20-Financial-Log\"').where(f => f.fl_weeks?.includes(dv.current().file.link) && f.fl_transaction_type === 'Income').sum(f => f.fl_amount || 0);"

  - name: weekly_total_expenses
    type: Formula
    options:
      formula: "return dv.pages('\"20-Financial-Log\"').where(f => f.fl_weeks?.includes(dv.current().file.link) && f.fl_transaction_type === 'Expense').sum(f => Math.abs(f.fl_amount || 0));"

  - name: weekly_net_cashflow
    type: Formula
    options:
      formula: "return (this.weekly_total_income || 0) - (this.weekly_total_expenses || 0);"

  # Status
  - name: weekly_status
    type: Formula
    options:
      formula: "const synthCount = [this.weekly_the_witness, this.weekly_the_logos_inquisitor, this.weekly_the_alpha_scanner, this.weekly_the_structural_integrator, this.weekly_the_ascension_architect, this.weekly_the_mythopoetic_weaver, this.weekly_the_somatic_arbiter, this.weekly_the_state_hacker, this.weekly_the_capital_strategist, this.weekly_the_hearth_tender, this.weekly_the_network_weaver, this.weekly_the_stillness_warden, this.weekly_the_aesthetic_calibrator, this.weekly_the_legacy_tender, this.weekly_the_systemic_navigator].filter(x => x && x.length > 0).length; return synthCount >= 10 ? 'Complete' : synthCount >= 5 ? 'In Progress' : 'Not Started';"
---
```

---
## FileClass-Months.md

```yaml
---
extends: base-entity
mapWithTag: true
tagNames: [monthly-review]
filesPaths: ["08-Months"]
maxRecordsPerPage: 12

fields:
  # Core Temporal Fields
  - name: month_number
    type: Number

  - name: year
    type: Number

  - name: time_period_start
    type: Date
    options:
      dateFormat: "YYYY-MM-DD"

  - name: time_period_end
    type: Date
    options:
      dateFormat: "YYYY-MM-DD"

  # Hierarchical Relations
  - name: quarters
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"09-Quarters\"')"

  - name: years
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"10-Years\"')"

  - name: weeks
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"07-Weeks\"')"

  - name: days
    type: MultiFile
    options:
      dvQueryString: "dv.pages('\"06-Days\"')"

  # Financial Log Relation
  - name: financial_log
    type: Lookup
    options:
      queryTemplate: "dv.pages('\"20-Financial-Log\"').where(f => f.fl_months?.includes(dv.current().file.link))"

  # 15 Intelligence Synthesis Units
  - name: month_synthesis
    type: Input

  - name: the_witness
    type: Input

  - name: the_logos_inquisitor
    type: Input

  - name: the_alpha_scanner
    type: Input

  - name: the_structural_integrator
    type: Input

  - name: the_ascension_architect
    type: Input

  - name: the_mythopoetic_weaver
    type: Input

  - name: the_somatic_arbiter
    type: Input

  - name: the_state_hacker
    type: Input

  - name: the_capital_strategist
    type: Input

  - name: the_hearth_tender
    type: Input

  - name: the_network_weaver
    type: Input

  - name: the_stillness_warden
    type: Input

  - name: the_aesthetic_calibrator
    type: Input

  - name: the_legacy_tender
    type: Input

  - name: the_systemic_navigator
    type: Input

  # Meta-Synthesis
  - name: month_oracle_synthesis
    type: Input

  - name: month_phoenix_synthesis
    type: Input

  - name: month_sovereign_synthesis
    type: Input

  # Financial Intelligence (Unique to Months)
  - name: accounts_snapshot
    type: Input

  - name: capital_allocation_insight
    type: Input

  - name: cashflow_narrative
    type: Input

  - name: significant_events
    type: Input

  - name: net_worth_change
    type: Number

  - name: ending_net_worth
    type: Number

  # Reflection
  - name: key_learnings
    type: Input

  # Financial Aggregation
  - name: total_income
    type: Formula
    options:
      formula: "return dv.pages('\"20-Financial-Log\"').where(f => f.fl_months?.includes(dv.current().file.link) && f.fl_transaction_type === 'Income').sum(f => f.fl_amount || 0);"

  - name: total_expenses
    type: Formula
    options:
      formula: "return dv.pages('\"20-Financial-Log\"').where(f => f.fl_months?.includes(dv.current().file.link) && f.fl_transaction_type === 'Expense').sum(f => Math.abs(f.fl_amount || 0));"

  - name: net_cashflow
    type: Formula
    options:
      formula: "return (this.total_income || 0) - (this.total_expenses || 0);"
---
```

---
## FileClass-Quarters.md

```yaml
---
extends: base-entity
mapWithTag: true
tagNames: [quarterly-review]
filesPaths: ["09-Quarters"]
maxRecordsPerPage: 4

fields:
  # Core Temporal Fields
  - name: quarter_number
    type: Number

  - name: year
    type: Number

  - name: time_period_start
    type: Date
    options:
      dateFormat: "YYYY-MM-DD"

  - name: time_period_end
    type: Date
    options