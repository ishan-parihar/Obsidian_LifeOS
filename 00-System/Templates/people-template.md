---
title: 
people_first_name: ""
people_custom_name: ""
people_city: ""
people_relationship_status: ""

# Developmental Psychology Tracking
people_developmental_altitude: ""
people_primary_center_intelligence: ""
people_explanatory_style: ""
people_stability_profile: ""
people_primary_conflict_style: ""
people_dominant_power_strategy: ""

# Motivational & Shadow Psychology
people_aspirational_drive: ""
people_core_shadow: ""
people_temporal_focus: ""

# Influence & Networking
people_influence_toolkit: []
people_networking_profile: ""
people_desired_trajectory: ""
people_value_exchange_balance: ""

# Strategic Context Fields
people_in_days_connection_frequency: 30
people_reconnect_by: ""
people_last_connected_date: ""
people_origin_context: ""
people_key_personal_intel: ""
people_strategic_context: ""
people_professional_domain_influence: ""
people_engagement_blueprint: ""
people_summary: ""

# Relations
people_community: []
people_projects: []
people_stories: []

# Computed Fields
people_current_status: ""
people_active_range: ""

entity_type: "person"
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
    array.sort(row => row.value("date"))
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
