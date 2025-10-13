---
dashboard_type: workbench
created: 2025-10-14
---
# The Workbench

> **Today's Command Center** - Real-time operational intelligence

## 🔥 Today's Focus

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  priority as "Priority",
  status as "Status"
FROM "15-Projects"
WHERE status = "Active" AND contains(string(this), "#sprint/current")
SORT priority DESC
LIMIT 10
```

## ⚡ Systemic Issues

```dataview
TABLE WITHOUT ID
  file.link as "Issue",
  impact as "Impact",
  status as "Status"
FROM "03-Systemic-Journal"
WHERE status = "Triage" OR status = "Escalated"
SORT impact DESC
LIMIT 5
```

## 👥 People Reconnections

```dataview
TABLE WITHOUT ID
  file.link as "Person",
  reconnect_by as "Reconnect By",
  networking_profile as "Profile"
FROM "17-People"
WHERE reconnect_by <= date(today) + dur(7 days)
SORT reconnect_by ASC
LIMIT 5
```

## 📊 Today's Metrics

- **Active Projects**: 
- **Current Sprint Tasks**: 
- **Systemic Dissonances**: 
- **People to Connect**: 

## 🎯 Strategic Alignment

```dataview
LIST
FROM "13-Annual-Goals"
WHERE status = "Active"
```

## 🔗 Quick Actions

- [ ] Create new Subjective log
- [ ] Log Systemic issue
- [ ] Add Activity entry
- [ ] Review Today's synthesis

---

*Last updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
