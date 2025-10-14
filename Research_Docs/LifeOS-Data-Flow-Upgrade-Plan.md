# LifeOS Data Flow Upgrade Plan

**Date**: 2025-10-14  
**Priority**: CRITICAL  
**Status**: Comprehensive Architecture Redesign Required

---

## 🎯 **Executive Summary**

The current LifeOS system has **fundamental data flow limitations** that prevent true hierarchical rollups. The system operates as isolated databases rather than an integrated hierarchy. This plan outlines a complete architectural transformation to enable bidirectional data flow across all levels.

### **Critical Issues Identified:**
1. **Missing Templates**: No monthly, yearly, or task templates exist
2. **Broken Queries**: Templates reference incorrect folder paths  
3. **Unidirectional Flow**: Data only flows upward, no downward visibility
4. **Inconsistent YAML**: Field structures don't support hierarchical linking
5. **No Cross-Hierarchy Queries**: Cannot see tasks from annual goals

---

## 📊 **Current State Analysis**

### **Existing Data Flow Limitations**

#### **Review Cycle Hierarchy (BROKEN)**
```
Days (06) → Weeks (07) → Months (08) → Quarters (09) → Years (10)
    ❌           ❌           ❌           ❌           ❌
```

**Problems:**
- Weekly template queries `"Reviews/Days"` (should be `"06-Days"`)
- No month/year templates exist
- No bidirectional linking fields
- Cannot navigate from Years → Days

#### **Strategic Execution Hierarchy (BROKEN)**
```
Annual Goals (13) → Quarterly Goals (14) → Projects (15) → Tasks (16)
       ❌                ❌              ❌           ❌
```

**Problems:**
- Annual goals template queries `"Strategy/QuarterlyGoals"` (should be `"14-Quarterly-Goals"`)
- No task template exists
- Projects template queries `"Projects"` (should be `"15-Projects"`)
- No downward visibility from goals to tasks

#### **Atomic Data Rollup (PARTIALLY FIXED)**
```
Subjective (01) → Days (06) ✅ FIXED
Relational (02) → Days (06) ✅ FIXED  
Systemic (03)  → Days (06) ✅ FIXED
Activity (04)  → Days (06) ✅ FIXED
Diet (05)      → Days (06) ✅ FIXED
```

---

## 🏗️ **Proposed Architecture Transformation**

### **1. Universal YAML Field Standardization**

#### **Hierarchical Linking Fields**
Every database needs standardized fields for bidirectional navigation:

```yaml
# Universal fields for all databases
hierarchy_level: "atomic|review|strategic|resource"
parent_entities: []           # Links to parent levels
child_entities: []            # Links to child levels  
sibling_entities: []          # Links to same level
related_time_periods: []      # Time-based relationships
strategic_alignment: []       # Goal/vision connections
```

#### **Time-Based Hierarchy Fields**
```yaml
# For time-based databases (Days, Weeks, Months, etc.)
time_period_start: "YYYY-MM-DD"
time_period_end: "YYYY-MM-DD"
containing_period: ""        # Parent time period
contained_periods: []        # Child time periods
parallel_periods: []         # Same level time periods
```

#### **Strategic Execution Fields**
```yaml
# For goal/project/task databases
strategic_hierarchy: {
  vision: [],
  annual_goals: [],
  quarterly_goals: [], 
  projects: [],
  tasks: []
}
execution_status: {
  progress: 0,
  health: "",
  next_milestone: "",
  blockers: []
}
```

### **2. Missing Template Creation**

#### **Required New Templates:**
- `monthly-review.md` - Month synthesis and rollup
- `annual-review.md` - Year synthesis and strategic review
- `task-template.md` - Individual task management
- `quarterly-review.md` - Quarter strategic assessment
- `vision-template.md` - Long-term vision framework  
- `values-template.md` - Core values definition

### **3. Complete Query Overhaul**

#### **Hierarchical Query Patterns**

**Upward Rollup Queries (Child → Parent):**
```dataview
# From Months → Quarter
TABLE WITHOUT ID
  file.link as "Month",
  month_progress as "Progress",
  key_insights as "Insights"
FROM "08-Months"
WHERE containing_period = this.file.name
SORT time_period_start DESC
```

**Downward Visibility Queries (Parent → Child):**
```dataview
# From Annual Goal → Tasks
TABLE WITHOUT ID
  file.link as "Task",
  status as "Status",
  priority as "Priority",
  due_date as "Due"
FROM "16-Tasks"
WHERE contains(strategic_hierarchy.annual_goals, "<% tp.file.title %>")
SORT priority DESC, due_date ASC
```

**Cross-Level Navigation Queries:**
```dataview
# From any level → Related atomic data
TABLE WITHOUT ID
  file.link as "Entry",
  type as "Type",
  emotional_tone as "Tone"
FROM "01-Subjective-Journal", "02-Relational-Journal", "03-Systemic-Journal"
WHERE date >= this.time_period_start AND date <= this.time_period_end
SORT date DESC, type ASC
```

---

## 🔧 **Implementation Roadmap**

### **Phase 1: Foundation Repair (Week 1)**

#### **1.1 Fix Existing Template Queries**
- [ ] Correct all folder path references in existing templates
- [ ] Fix weekly-review.md: `"Reviews/Days"` → `"06-Days"`
- [ ] Fix annual-goal.md: `"Strategy/QuarterlyGoals"` → `"14-Quarterly-Goals"`
- [ ] Fix quarterly-goal.md: `"Strategy/FailureScenarios"` → `"24-Failure-Scenarios"`
- [ ] Fix project-template.md: `"Projects"` → `"15-Projects"`

#### **1.2 Create Missing Templates**
- [ ] Create `monthly-review.md` template
- [ ] Create `annual-review.md` template  
- [ ] Create `task-template.md` template
- [ ] Create `quarterly-review.md` template
- [ ] Create `vision-template.md` template
- [ ] Create `values-template.md` template

### **Phase 2: YAML Transformation (Week 2)**

#### **2.1 Upgrade All Template YAML Structures**
- [ ] Add universal hierarchy fields to all templates
- [ ] Add time-based fields to review cycle templates
- [ ] Add strategic execution fields to goal/project/task templates
- [ ] Standardize field naming conventions across all templates

#### **2.2 Implement Bidirectional Linking**
- [ ] Add parent/child relationship fields
- [ ] Add strategic alignment fields
- [ ] Add time period relationship fields
- [ ] Create automated link generation in templates

### **Phase 3: Advanced Query Implementation (Week 3)**

#### **3.1 Hierarchical Query Library**
- [ ] Create standardized query patterns for each hierarchy level
- [ ] Implement upward rollup queries
- [ ] Implement downward visibility queries
- [ ] Implement cross-level navigation queries

#### **3.2 Dashboard Integration**
- [ ] Update Workbench dashboard with hierarchical queries
- [ ] Update Observatory dashboard with multi-level views
- [ ] Create new strategic hierarchy dashboard
- [ ] Create time navigation dashboard

### **Phase 4: Testing & Validation (Week 4)**

#### **4.1 End-to-End Testing**
- [ ] Test atomic → daily rollup (already working)
- [ ] Test daily → weekly → monthly → quarterly → annual rollup
- [ ] Test annual → quarterly → project → task visibility
- [ ] Test cross-hierarchy navigation (years → days)
- [ ] Test strategic drill-down (vision → tasks)
- [ ] Validate all dashboard queries

#### **4.2 Performance Optimization**
- [ ] Optimize Dataview query performance
- [ ] Implement query caching strategies
- [ ] Test with large datasets
- [ ] Validate memory usage

---

## 📋 **Detailed Template Specifications**

### **Missing Template Requirements**

#### **1. Monthly Review Template**
```yaml
---
month_number: <% tp.date.now("MM") %>
month_name: <% tp.date.now("MMMM") %>
year: <% tp.date.now("YYYY") %>
time_period_start: <% tp.date.now("YYYY-MM-01") %>
time_period_end: <% tp.date.now("YYYY-MM-31") %>
containing_period: [[<% tp.date.now("YYYY-[Q]Q") %>]]
contained_periods: [] # Auto-populated with weeks
parallel_periods: [] # Other months in same year
hierarchy_level: "review"
parent_entities: []
child_entities: []
strategic_alignment: []
month_progress: 0
key_insights: ""
emergent_themes: []
health_metrics: {}
---
```

#### **2. Task Template**
```yaml
---
title: 
description: 
priority: "High|Medium|Low"
status: "Backlog|Ready|In Progress|Blocked|Done"
due_date: 
estimated_hours: 
actual_hours: 
assigned_to: 
strategic_hierarchy: {
  vision: [],
  annual_goals: [],
  quarterly_goals: [],
  projects: [],
  tasks: [] # Dependencies
}
execution_status: {
  progress: 0,
  health: "",
  next_milestone: "",
  blockers: []
}
hierarchy_level: "strategic"
parent_entities: [] # Project
child_entities: [] # Subtasks
sibling_entities: [] # Other tasks in project
context: {
  energy_required: "",
  time_of_day: "",
  location: "",
  tools_needed: []
}
---
```

### **Query Pattern Library**

#### **Time Hierarchy Navigation**
```dataview
# Navigate from any time period to contained days
TABLE WITHOUT ID
  file.link as "Day",
  day_synthesis as "Synthesis",
  energy_level as "Energy"
FROM "06-Days"
WHERE date >= this.time_period_start AND date <= this.time_period_end
SORT date DESC

# Navigate from any time period to atomic data
TABLE WITHOUT ID
  file.link as "Entry",
  type as "Type",
  primary_emotion as "Emotion"
FROM "01-Subjective-Journal" OR "02-Relational-Journal" OR "03-Systemic-Journal"
WHERE date >= this.time_period_start AND date <= this.time_period_end
SORT date DESC, type ASC
```

#### **Strategic Hierarchy Navigation**
```dataview
# From Vision → All execution items
TABLE WITHOUT ID
  file.link as "Item",
  type as "Type",
  status as "Status",
  progress as "Progress"
FROM "13-Annual-Goals" OR "14-Quarterly-Goals" OR "15-Projects" OR "16-Tasks"
WHERE contains(strategic_hierarchy.vision, "<% tp.file.title %>")
SORT type ASC, progress DESC

# From Annual Goal → Complete execution tree
TABLE WITHOUT ID
  file.link as "Item",
  type as "Type",
  status as "Status",
  due_date as "Due"
FROM "14-Quarterly-Goals" OR "15-Projects" OR "16-Tasks"
WHERE contains(strategic_hierarchy.annual_goals, "<% tp.file.title %>")
SORT type ASC, due_date ASC
```

---

## 🎯 **Priority Implementation Matrix**

### **CRITICAL (Must Fix First)**
1. **Fix existing template queries** - System currently broken
2. **Create task template** - Strategic execution hierarchy incomplete
3. **Create monthly/yearly templates** - Review cycle broken
4. **Standardize YAML fields** - No hierarchical linking possible

### **HIGH (Enables Core Functionality)**
1. **Bidirectional linking implementation**
2. **Hierarchical query library**
3. **Dashboard updates**
4. **Time navigation system**

### **MEDIUM (Enhanced Capabilities)**
1. **Performance optimization**
2. **Advanced cross-hierarchy queries**
3. **Automated link generation**
4. **Query caching**

---

## 📈 **Expected Outcomes**

### **Before Upgrade (Current State)**
- ❌ Cannot navigate from Years to Days
- ❌ Cannot see Tasks from Annual Goals
- ❌ Broken queries in existing templates
- ❌ Missing 6 critical templates
- ❌ Unidirectional data flow only
- ❌ No hierarchical relationship tracking

### **After Upgrade (Target State)**
- ✅ Complete bidirectional hierarchy navigation
- ✅ See any level from any other level
- ✅ All queries working and optimized
- ✅ Complete template library (24 total)
- ✅ Automatic relationship tracking
- ✅ Cross-hierarchy data synthesis
- ✅ Performance-optimized queries

### **Use Cases Enabled**
1. **Strategic Review**: From Vision → All execution items
2. **Time Travel**: From Year → Any specific day's atomic data
3. **Progress Tracking**: From Task → Impact on Annual Goals
4. **Pattern Analysis**: Across any time period and data type
5. **Resource Planning**: View all commitments across hierarchies

---

## 🚨 **Immediate Action Required**

The current system is **partially functional** and needs immediate attention:

### **Today's Critical Fixes:**
1. Fix weekly-review.md template queries
2. Fix annual-goal.md template queries  
3. Fix quarterly-goal.md template queries
4. Fix project-template.md queries
5. Create basic task template

### **This Week's Priorities:**
1. Create monthly and yearly review templates
2. Implement standardized YAML fields
3. Test basic hierarchical navigation
4. Update dashboard queries

---

## 📝 **Next Steps**

1. **Review this plan** with system requirements
2. **Approve implementation roadmap**
3. **Begin Phase 1: Foundation Repair**
4. **Test each phase** before proceeding
5. **Document all changes** for future reference

---

**This upgrade plan transforms LifeOS from a collection of isolated databases into a truly integrated hierarchical life management system.**

**Estimated Timeline**: 4 weeks
**Priority**: CRITICAL
**Impact**: Complete system transformation

