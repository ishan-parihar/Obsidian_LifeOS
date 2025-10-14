---
dashboard_type: engine-room
created: 2025-10-14
---

# The Engine Room

> **Resource Management Hub** - Knowledge, documents, and system resources

## 📚 Knowledge Management

### Recent Notes

```dataview
TABLE WITHOUT ID
  file.link as "Note",
  status as "Status",
  file.mtime as "Modified"
FROM "21-Notes"
WHERE status = "Live" OR status = "Priority-Highlight"
SORT file.mtime DESC
LIMIT 10
```

## 📄 Document Repository

### Recent Documents

```dataview
TABLE WITHOUT ID
  file.link as "Document",
  category as "Category",
  status as "Status"
FROM "22-Documents"
SORT file.mtime DESC
LIMIT 10
```

### Document Categories

```dataview
TABLE WITHOUT ID
  category as "Category",
  count(rows) as "Count"
FROM "Resources/Documents"
GROUP BY category
SORT count(rows) DESC
```

## 🏦 Financial Resources

### Account Overview

```dataview
TABLE WITHOUT ID
  file.link as "Account",
  type as "Type",
  current_balance as "Balance",
  status as "Status"
FROM "19-Financial-Accounts"
WHERE status = "Active"
SORT current_balance DESC
```

### Recent Financial Activity

```dataview
TABLE WITHOUT ID
  file.link as "Transaction",
  amount as "Amount",
  category as "Category",
  date as "Date"
FROM "20-Financial-Log"
SORT date DESC
LIMIT 10
```

## 👥 People Network

### Relationship Overview

```dataview
TABLE WITHOUT ID
  networking_profile as "Profile",
  count(rows) as "Count",
  choice(count(rows) > 2, "🔥", "📝") as "Activity"
FROM "17-People"
GROUP BY networking_profile
SORT count(rows) DESC
```

### Upcoming Reconnections

```dataview
TABLE WITHOUT ID
  file.link as "Person",
  reconnect_by as "Reconnect By",
  days_until_reconnect as "Days Until"
FROM "People"
WHERE reconnect_by >= date(today) AND reconnect_by <= date(today) + dur(30 days)
SORT reconnect_by ASC
LIMIT 10
```

## 🏗️ Project Resources

### Systemic Patterns

```dataview
TABLE WITHOUT ID
  system_domain as "Domain",
  count(rows) as "Issues",
  choice(count(rows) > 5, "⚠️", "✅") as "Health"
FROM "03-Systemic-Journal"
GROUP BY system_domain
SORT count(rows) DESC
```

## 📊 System Metrics

### Database Health

- **Active Projects**: 
- **People Profiles**: 
- **Documents**: 
- **Financial Accounts**: 
- **Knowledge Notes**: 

### Storage Overview

- **Total Notes**: 
- **Total Size**: 
- **Last Backup**: 

## 🔗 Quick Actions

- [ ] Create new note
- [ ] Upload document
- [ ] Add financial account
- [ ] Create person profile
- [ ] Backup vault

## 🌐 Hierarchical Navigation

### Cross-Hierarchy: Atomic Data by Time Period
```dataview
TABLE WITHOUT ID
  file.link as "Entry",
  type as "Type",
  primary_emotion as "Emotion"
FROM "01-Subjective-Journal" OR "02-Relational-Journal" OR "03-Systemic-Journal"
WHERE date >= date(today) - dur(7 days)
SORT date DESC, type ASC
LIMIT 15
```

---

*Last updated: 2025-10-14*
