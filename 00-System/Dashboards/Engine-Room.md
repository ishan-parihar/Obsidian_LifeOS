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
FROM "Notes"
WHERE status = "Live" OR status = "Priority-Highlight"
SORT file.mtime DESC
LIMIT 10
```

### Knowledge Categories

```dataview
LIST
FROM "MOCs"
SORT file.name ASC
```

## 📄 Document Repository

### Recent Documents

```dataview
TABLE WITHOUT ID
  file.link as "Document",
  category as "Category",
  status as "Status"
FROM "Resources/Documents"
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
FROM "Resources/Financial-Accounts"
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
FROM "Financial Log"
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
FROM "People"
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

### Competency Arsenal

```dataview
LIST
FROM "Resources/Competency-Arsenal"
SORT file.name ASC
```

### Systemic Patterns

```dataview
TABLE WITHOUT ID
  system_domain as "Domain",
  count(rows) as "Issues",
  choice(count(rows) > 5, "⚠️", "✅") as "Health"
FROM "Logs/Systemic"
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

---

*Last updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>*
