---
title:
custom_name:
relationship_status:
city:
developmental_altitude:
primary_center_intelligence:
explanatory_style:
stability_profile:
primary_conflict_style:
dominant_power_strategy:
temporal_focus:
aspirational_drive:
core_shadow:
influence_toolkit: []
networking_profile:
desired_trajectory:
value_exchange_balance:
in_days_connection_frequency: 30
origin_context:
key_personal_intel:
professional_domain:
strategic_context:
engagement_blueprint:
summary:
---

# {{title}}

## Relationship Status
{{relationship_status}}

## Connection Management
- Last Connected:
- Reconnect By: [[<% tp.date.now('YYYY-MM-DD') %>]]
- Frequency: Every {{in_days_connection_frequency}} days

## Profile
- Developmental Altitude: {{developmental_altitude}}
- Primary Intelligence: {{primary_center_intelligence}}
- Explanatory Style: {{explanatory_style}}
- Stability Profile: {{stability_profile}}

## Context
{{summary}}

## Strategic Context
{{strategic_context}}

## Engagement Blueprint
{{engagement_blueprint}}

## Projects Involvement
```dataview
LIST
FROM "Projects"
WHERE contains(projects, this.file.link)
```

## Interaction History
```dataview
LIST
FROM "Logs/Relational"
WHERE contains(people, this.file.link)
SORT date DESC
```