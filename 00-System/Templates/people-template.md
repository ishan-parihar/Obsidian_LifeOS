---
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
last_connected_date:
reconnect_by:
origin_context:
key_personal_intel:
professional_domain_influence:
strategic_context:
engagement_blueprint:
summary:
community: []
projects: []
stories: []
type: person
created: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>
---

# <% tp.file.title %>

## 👤 Basic Info

**Relationship Status**: 
**City**: 
**Custom Name**: 

## 🧠 Intelligence Profile

### Developmental Psychology
**Developmental Altitude**: 
**Primary Center of Intelligence**: 
**Explanatory Style**: 
**Stability Profile**: 
**Primary Conflict Style**: 
**Core Shadow**: 

### Motivational & Strategic
**Aspirational Drive**: 
**Dominant Power Strategy**: 
**Temporal Focus**: 
**Influence Toolkit**: 

## 🤝 Network Management

**Current Profile**: 
**Desired Trajectory**: 
**Value Exchange Balance**: 
**Connection Frequency**: 30 days

**Next Reconnect**: 
**Last Connected**: 

## 📋 Strategic Context

### Origin

**How we met**: 

### Professional Domain

**Expertise & Influence**: 

### Strategic Value

**Strategic Context**: 

### Engagement Blueprint

**How to interact effectively**: 

### Key Intelligence

**Important facts to remember**: 

## 📊 Relationship History

### Recent Interactions

```dataview
TABLE WITHOUT ID
  file.link as "Interaction",
  date as "Date",
  emotional_tone as "Tone"
FROM "Logs/Relational"
WHERE contains(people, "<% tp.file.title %>")
SORT date DESC
LIMIT 5
```

### Shared Projects

```dataview
LIST
FROM "Projects"
WHERE contains(people, "<% tp.file.title %>") AND status = "Active"
```

## 🎯 Growth Opportunities

**What I can learn from them**: 
**How I can contribute to their growth**: 
**Potential collaborations**: 

---

*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
