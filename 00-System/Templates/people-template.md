---
title: 
first_name: ""
custom_name: ""
city: ""
relationship_status: ""

# Developmental Psychology Tracking
developmental_altitude: ""
primary_center_intelligence: ""
explanatory_style: ""
stability_profile: ""
primary_conflict_style: ""
dominant_power_strategy: ""

# Motivational & Shadow Psychology
aspirational_drive: ""
core_shadow: ""
temporal_focus: ""

# Influence & Networking
influence_toolkit: []
networking_profile: ""
desired_trajectory: ""
value_exchange_balance: ""

# Strategic Context Fields
in_days_connection_frequency: 30
reconnect_by: ""
last_connected_date: ""
origin_context: ""
key_personal_intel: ""
strategic_context: ""
professional_domain_influence: ""
engagement_blueprint: ""
summary: ""

# Relations
community: []
projects: []
stories: []

# Computed Fields
current_status: ""
active_range: ""

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

```datacorejsx
const COLUMNS = [
  { id: "Interaction", value: row => row.$link },
  { id: "Date", value: row => row.value("date") },
  { id: "Tone", value: row => row.value("emotional_tone") }
];

return function View() {
  const interactions = dc.useQuery(`@page and "Logs/Relational" and people = "<% tp.file.title %>"`);
  const sortedInteractions = dc.useArray(interactions, array => 
    array.sort(row => row.value("date")).reverse()
  ).slice(0, 5);
  
  return <dc.VanillaTable columns={COLUMNS} rows={sortedInteractions} />;
}
```

### Shared Projects

```datacorejsx
return function View() {
  const projects = dc.useQuery(`@page and "Projects" and people = "<% tp.file.title %>" and status = "Active"`);
  
  return (
    <ul>
      {projects.map(project => (
        <li key={project.$path}>{project.$link}</li>
      ))}
    </ul>
  );
}
```

## 🎯 Growth Opportunities

**What I can learn from them**: 
**How I can contribute to their growth**: 
**Potential collaborations**: 

---

*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
