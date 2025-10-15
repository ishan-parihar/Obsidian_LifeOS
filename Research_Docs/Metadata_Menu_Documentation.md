# Metadata Menu Plugin: Comprehensive Technical Documentation for AI Agent Implementation

## Executive Overview

Metadata Menu is a data quality management plugin for Obsidian that enables structured metadata management through typed fields, contextual classifications (fileClasses), and automated data validation. The plugin operates on both frontmatter properties (YAML) and inline fields (Dataview syntax: `fieldName::value`) to provide database-like functionality within a knowledge management system.[mdelobelle.github+2](https://mdelobelle.github.io/metadatamenu/)​

## Core Architecture

## System Components

**Metadata Scope Management**: The plugin operates in two modes configured via global settings :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/settings/)​

- Frontmatter-only mode: Manages YAML properties exclusively (optimal performance)
    
- Frontmatter + Inline mode: Manages both YAML and Dataview inline fields (slower with large files)
    

**Field Definition Hierarchy**: Field settings follow a priority cascade system :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/general/)​

1. FileClass field definitions (highest priority)
    
2. Global preset field settings (plugin settings)
    
3. Default behavior (no constraints)
    

**Control Interfaces**: Fields can be manipulated through multiple access points :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/general/)​

- Editor autocompletion with suggested values
    
- Context menus (file explorer, tab headers, link right-click)
    
- Dataview table integration with fieldModifiers
    
- Metadata Menu button (appears adjacent to notes in various contexts)
    
- FileClass table views with inline editing
    
- Metadata Menu code blocks
    

## Field Type System (22 Types)

## Basic Data Types

**Input Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/fields/)​

text

`Type: Input Accepts: Any string value Constraints: None Options: {template: "string with {{placeholder}}"} Use Case: Freeform text entry, templated patterns`

**Boolean Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/fields/)​

text

`Type: Boolean Accepts: true | false | null Constraints: Three-state logic Options: None Use Case: Binary states, toggles, flags`

**Number Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/general/)​

text

`Type: Number Accepts: Numeric values (integer or float) Constraints: Numeric validation Options: None Use Case: Quantities, measurements, calculations`

## Selection Types

**Select Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/fields/)​

text

`Type: Select Accepts: Single value from predefined list Constraints: Must match options Options: {   valuesList: {"0": "option1", "1": "option2"},  sourceType: "ValuesList" | "ValuesFromPath" | "ValuesFromDVQuery",  valuesListNotePath: "path/to/note.md",  valuesFromDVQuery: "dv.pages('\"folder\"')" } Use Case: Status fields, categories, controlled vocabularies`

**Multi Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/general/)​

text

`Type: Multi Accepts: Array of values from predefined list Constraints: All values must match options Options: Same as Select field Use Case: Tags, multiple categories, multi-selection`

**Cycle Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/fields/)​

text

`Type: Cycle Accepts: Values that cycle through predefined list Constraints: Sequential progression through options Options: Same as Select field Use Case: Workflow states, progressive status tracking`

## File Link Types

**File Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/general/)​

text

`Type: File Accepts: [[wikilink]] to vault file Constraints: Must be valid file in vault Options: {   dvQueryString: "dv.pages('\"folder\"').where(p => condition)",  customListViewHeader: "string",  filters: [array of filter conditions] } Use Case: Single file references, relationships`

**MultiFile Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/fields/)​

text

`Type: MultiFile Accepts: Array of [[wikilinks]] Constraints: All must be valid files Options: Same as File field Use Case: Multiple file relationships, collections`

**Media Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/general/)​

text

`Type: Media Accepts: [[wikilink]] to media file (image, audio, video) Constraints: Must be media file type Options: Same as File field Use Case: Image galleries, audio references`

**MultiMedia Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/fields/)​

text

`Type: MultiMedia Accepts: Array of [[wikilinks]] to media files Constraints: All must be media file types Options: Same as File field Use Case: Multiple media attachments`

## Temporal Types

**Date Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/general/)​

text

`Type: Date Accepts: Date in specified format Constraints: Valid date Options: {   dateFormat: "YYYY-MM-DD" | "DD/MM/YYYY" | custom,  defaultInsertAsLink: "true" | "false" } Use Case: Deadlines, creation dates, timestamps`

**DateTime Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/fields/)​

text

`Type: DateTime Accepts: Date with time component Constraints: Valid datetime Options: Same as Date field plus time format Use Case: Precise timestamps, scheduling`

**Time Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/general/)​

text

`Type: Time Accepts: Time value Constraints: Valid time format Options: Time format specifications Use Case: Time tracking, duration fields`

## Computed Types

**Lookup Field**[reddit+2](https://www.reddit.com/r/ObsidianMD/comments/xmnhwa/metadatamenu_02_lookup_fields/)​

text

`Type: Lookup Accepts: Dataview query result Constraints: Must be valid Dataview expression Options: {   queryTemplate: "dataview inline query",  outputType: "inline" | "bulletList" } Behavior: Automatically refreshed, persists calculated value Use Case: Dynamic aggregations, relationship queries, computed references Example: Retrieve all tasks from linked project notes`

**Formula Field**[reddit+2](https://www.reddit.com/r/ObsidianMD/comments/1d1kj4e/metadata_menu_formula_to_show_relative_date_today/)​

text

`Type: Formula Accepts: JavaScript expression result Constraints: Valid JS syntax, access to note fields via this.fieldName Options: {   formula: "JavaScript expression" } Use Case: Calculations, conditional logic, data transformations Example: this.endDate - this.startDate`

## Canvas Integration Types

**Canvas Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/fields/)​

text

`Type: Canvas Accepts: Links extracted from canvas file Constraints: Must reference canvas nodes Options: Canvas-specific configuration Use Case: Visual relationship mapping`

**Canvas Group Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/general/)​

text

`Type: Canvas Group Accepts: Group identifiers from canvas Constraints: Must be valid canvas groups Options: Group selection criteria Use Case: Kanban boards, visual categorization`

**Canvas Group Link Field**[mdelobelle.github+1](https://mdelobelle.github.io/metadatamenu/fields/)​

text

`Type: Canvas Group Link Accepts: Links within canvas groups Constraints: Must be within specified groups Options: Group and link filtering Use Case: Grouped relationship tracking`

## Structured Data Types

**JSON Field**[reddit+2](https://www.reddit.com/r/ObsidianMD/comments/17wz7pt/metadata_menu_060_public_beta_is_out/)​

text

`Type: JSON Accepts: Valid JSON object Constraints: Must parse as JSON Options: JSON editor configuration Scope: Frontmatter only Use Case: Complex data structures, API responses`

**YAML Field**[reddit+2](https://www.reddit.com/r/ObsidianMD/comments/17wz7pt/metadata_menu_060_public_beta_is_out/)​

text

`Type: YAML Accepts: Valid YAML object Constraints: Must parse as YAML Options: YAML editor configuration Scope: Frontmatter only Use Case: Hierarchical configuration data`

**Object Field**[reddit+2](https://www.reddit.com/r/ObsidianMD/comments/17wz7pt/metadata_menu_060_public_beta_is_out/)​

text

`Type: Object Accepts: Collection of nested fields Constraints: Defined field structure Options: {   fields: [    {name: "fieldName", type: "FieldType", options: {...}},    ...  ] } Scope: Frontmatter only Use Case: Nested property structures, complex entities Example: Address object with street, city, zip fields`

**Object List Field**[obsidian+3](https://forum.obsidian.md/t/getting-a-list-from-metadata-menu-object-list-in-dataview-js-table/83600)​

text

`Type: Object List Accepts: Array of Object field collections Constraints: Each item follows Object field structure Options: Same as Object field Scope: Frontmatter only Use Case: Repeating structured data, multiple related entries Example: List of tasks with title, status, priority fields Accessing: In Dataview use dv.p.objectListField[index].nestedField`

## FileClass System

## Concept and Purpose

FileClasses provide context-aware field definitions that apply to specific note categories. They function as "schemas" or "templates" that define which fields are available and how they behave for different note types.[chaseadams+2](https://chaseadams.io/posts/metadata-menu)​

## FileClass Architecture

**FileClass File Structure** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/fileclasses/)​

text

`--- # FileClass Settings (frontmatter) extends: parentFileClassName excludes: [fieldName1, fieldName2] mapWithTag: true tagNames: [tag1, tag2] filesPaths: ["folder/path", "another/folder"] bookmarkGroups: ["group1", "group2"] buttonIcon: lucideIconName maxRecordsPerPage: 50 fields:   - name: fieldName    type: FieldType    id: uniqueId    path: fieldPath    options:      option1: value1      option2: value2 --- # Body (not used by plugin, available for documentation)`

## FileClass Mapping Strategies

**Priority Order** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/fileclasses/)​

1. Explicit `fileClass: className` in note frontmatter (highest)
    
2. Tag matching (if `mapWithTag: true`)
    
3. Path matching (if note in `filesPaths`)
    
4. Bookmark group matching (if bookmarked in `bookmarkGroups`)
    
5. FileClass query matching (from plugin settings)
    
6. Global FileClass (catch-all default)
    
7. Preset field settings (lowest)
    

**Implementation Patterns**:

_Basic Mapping_ :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/fileclasses/)​

text

`--- fileClass: projectNote ---`

_Multiple FileClasses_ :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/fileclasses/)​

text

`--- fileClass:   - projectNote  - clientWork ---`

_Tag-Based Mapping_ :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/fileclasses/)​

text

`# In FileClass file --- mapWithTag: true --- # In target note #projectNote`

_Path-Based Mapping_ :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/fileclasses/)​

text

`# In FileClass file --- filesPaths: ["Projects/Active", "Work/Current"] --- # All notes in these folders automatically mapped`

## FileClass Inheritance

**Extends Mechanism** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/fileclasses/)​

text

`# Parent: course.md --- fields:   - name: teacher    type: Input  - name: grade    type: Select    options:      valuesList:        "0": "A"        "1": "B"        "2": "C" --- # Child: mathematics.md --- extends: course fields:   - name: chapter    type: Select    options:      valuesList:        "0": "Algebra"        "1": "Geometry" --- # Inherits teacher and grade fields, adds chapter field`

**Field Override** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/fileclasses/)​  
Child FileClasses can redefine inherited fields to customize behavior:

text

`--- extends: course fields:   - name: grade  # Overrides parent grade field    type: Select    options:      valuesList:        "0": "Pass"        "1": "Fail" ---`

**Exclusion Pattern** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/fileclasses/)​

text

`--- extends: course excludes: [grade]  # Inherits all fields except grade ---`

## FileClass Views

**Table View** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/fileclasses/)​

- Displays all notes mapped to FileClass
    
- Inline field editing capabilities
    
- Filtration system with multiple strategies
    
- Sortable columns
    
- Customizable column visibility and order
    

**Filter Types** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/fileclasses/)​

- Text filter: Type value, supports comma-separated multiple values
    
- Regex filter: Use `/pattern/` syntax (escape backslashes: `\\`)
    
- Dropdown filters:
    
    - Empty values: Field exists but no value
        
    - Not empty values: Field exists with value
        
    - Not found: Field doesn't exist in note
        
    - Existing: Field exists regardless of value
        
    - Type-specific values (Select options, File lists, Boolean states)
        
- Custom JavaScript filter functions returning boolean
    

**Saved Views** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/fileclasses/)​

- Save filter + sort combinations
    
- Mark favorite view as default
    
- Per-FileClass view persistence
    

## Configuration System

## Global Settings

**Scope Configuration** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/settings/)​

text

`Setting: Scope Options: "Frontmatter only" | "Frontmatter and inline fields" Impact: Performance vs. functionality trade-off Requires: Plugin reload on change`

**Context Menu Display** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/settings/)​

text

`Setting: Display field options in context menu On: All fields shown directly (large menus) Off: Fields accessed via "Field Options" modal (compact)`

**Field Exclusions** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/settings/)​

text

`Setting: Globally ignored fields Format: Comma-separated field names Effect: Excluded from all context menus Example: "id, internal_id, system_field"`

**File Exclusions** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/settings/)​

text

`Setting: Exclusions Options: Path patterns, extensions, regex name patterns Use Case: Exclude templates, system files, archives`

**Date Picker Configuration** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/settings/)​

text

`Setting: First day of week Options: Monday | Sunday Applies to: All Date and DateTime field pickers`

## Preset Field Settings

**Global Field Definition** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/settings/)​

text

`Location: Plugin Settings > Preset Field Settings Process: 1. Click "+" to add field 2. Enter field name 3. Select field type 4. Configure type-specific options Effect: Field available across entire vault`

## FileClass Settings

**FileClass Folder Configuration** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/settings/)​

text

`Setting: Class Files Path Format: "path/to/classes/" (include trailing slash) Purpose: Centralized FileClass definition storage`

**FileClass Alias** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/settings/)​

text

`Setting: fileClass field alias Purpose: Use existing categorization field (e.g., "type", "category") Effect: Dual-purpose field (categorization + field management)`

**Global FileClass** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/settings/)​

text

`Setting: Global fileClass Purpose: Default FileClass for all notes without explicit mapping Priority: Lowest in mapping hierarchy`

**Query-Based FileClass** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/settings/)​

text

`Setting: fileClass queries Format: Dataview query syntax Effect: Automatic FileClass assignment based on query match Priority: Last matching query wins (top to bottom)`

## Button Visibility Settings

**Metadata Menu Button Toggles** :[dannyhatcher](https://dannyhatcher.com/metadata-menu/)​

- Reading mode
    
- Live preview mode
    
- Tab headers
    
- File explorer
    
- Backlinks panel
    
- Search panel
    
- Starred/Bookmarks panel
    
- Properties section
    

**Custom Button Icons** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/fileclasses/)​

text

`Setting: buttonIcon (per FileClass) Source: lucide.dev icon names Tool: Use Commander plugin to browse icon names`

## Implementation Workflows

## Field Creation Workflow

**Global Field Creation**:

text

`1. Settings > Metadata Menu > Preset Field Settings 2. Click "+" button 3. Define:    - Field name (must be unique)   - Field type (from 22 options)   - Type-specific options 4. Save configuration 5. Field available in all notes`

**FileClass Field Creation**:

text

`1. Create FileClass note in configured folder 2. Click Metadata Menu button on FileClass note 3. Navigate to "Fileclass Fields" tab 4. Add field with "list plus" button 5. Configure field definition 6. Field available only to mapped notes`

**Inline Field Creation** :[dannyhatcher](https://dannyhatcher.com/metadata-menu/)​

text

`Context Menu > Add field at cursor Context Menu > Add field at section Context Menu > Add field in frontmatter`

## Note-to-FileClass Mapping Workflow

**Explicit Mapping**:

text

`--- fileClass: taskManagement ---`

**Tag-Based Automatic Mapping**:

text

`FileClass Configuration: --- mapWithTag: true --- Target Note: #taskManagement`

**Path-Based Automatic Mapping**:

text

`FileClass Configuration: --- filesPaths: ["Tasks", "Projects/Active"] --- Effect: All notes in specified paths automatically mapped`

## Data Entry Workflows

**Via Autocompletion**:

text

`1. Type field name in editor 2. Trigger autocompletion (Ctrl+Space) 3. Select from suggested values 4. Value inserted with validation`

**Via Context Menu**:

text

`1. Right-click note/link/tab 2. Select field from context menu 3. Choose value from modal/picker 4. Value written to note`

**Via Dataview Table**:

text

`const {fieldModifier: f} = this.app.plugins.plugins["metadata-menu"].api; dv.table(   ["Name", "Status", "Priority"],  dv.pages('"Projects"')    .map(p => [      p.file.link,      f(dv, p, "status"),      f(dv, p, "priority")    ]) );`

**Via FileClass Table View**:

text

`1. Open FileClass note 2. Click Metadata Menu button 3. Navigate to "Table view" tab 4. Edit fields directly in table cells 5. Apply filters and sorts 6. Save view for future use`

## Advanced Implementation Patterns

## Lookup Field Implementation

**Basic Lookup** :[reddit](https://www.reddit.com/r/ObsidianMD/comments/xmnhwa/metadatamenu_02_lookup_fields/)​

text

`fieldName:   type: Lookup  options:    queryTemplate: "[[currentNote]].relatedField"`

**Dataview Query Lookup**:

text

`relatedTasks:   type: Lookup  options:    queryTemplate: "dv.pages().where(p => p.project == dv.current().file.name)"    outputType: "bulletList"`

**Aggregation Lookup**:

text

`totalHours:   type: Lookup  options:    queryTemplate: "dv.pages().where(p => p.project == dv.current().file.name).sum(p => p.hours)"`

## Formula Field Implementation

**Date Calculation** :[reddit](https://www.reddit.com/r/ObsidianMD/comments/1d1kj4e/metadata_menu_formula_to_show_relative_date_today/)​

javascript

`// Days until deadline Math.ceil((new Date(this.deadline) - new Date()) / (1000 * 60 * 60 * 24))`

**Conditional Logic**:

javascript

`// Priority based on status and deadline this.status === "urgent" || (this.deadline && new Date(this.deadline) < new Date(Date.now() + 7*24*60*60*1000)) ? "High" : "Normal"`

**Field Aggregation**:

javascript

`// Total score from multiple fields (this.score1 || 0) + (this.score2 || 0) + (this.score3 || 0)`

## Object and ObjectList Implementation

**Object Field Structure** :[reddit](https://www.reddit.com/r/ObsidianMD/comments/17wz7pt/metadata_menu_060_public_beta_is_out/)​

text

`address:   type: Object  options:    fields:      - name: street        type: Input      - name: city        type: Select        options:          valuesList:            "0": "New York"            "1": "London"      - name: zipCode        type: Number`

**ObjectList Field Structure** :[obsidian](https://forum.obsidian.md/t/getting-a-list-from-metadata-menu-object-list-in-dataview-js-table/83600)​

text

`tasks:   type: ObjectList  options:    fields:      - name: title        type: Input      - name: status        type: Select        options:          valuesList:            "0": "Todo"            "1": "In Progress"            "2": "Done"      - name: priority        type: Number`

**Accessing ObjectList in Dataview** :[obsidian](https://forum.obsidian.md/t/getting-a-list-from-metadata-menu-object-list-in-dataview-js-table/83600)​

javascript

`// Access specific item and field page.tasks[0].title // Iterate over ObjectList page.tasks.forEach(task => {   console.log(task.title, task.status); }); // In DataviewJS table dv.table(   ["Task", "Status"],   dv.current().tasks.map(t => [t.title, t.status]) );`

## Template Integration Pattern

**Input Field with Template** :[curiouslychase+1](https://www.curiouslychase.com/posts/metadata-menu)​

text

`image:   type: Input  options:    template: "/img/notes/{{image}}.png"`

**Usage**:

text

`User enters: "diagram-01" System writes: "/img/notes/diagram-01.png"`

## Nested FileClass Architecture

**Parent-Child Hierarchy**:

text

`BaseNote (fileClass)   ├── fields: common fields  │  ├── ProjectNote (extends BaseNote)  │   ├── inherits: common fields  │   └── adds: project-specific fields  │  └── TaskNote (extends BaseNote)      ├── inherits: common fields      └── adds: task-specific fields`

**Implementation**:

text

`# BaseNote.md --- fields:   - name: created    type: Date  - name: modified    type: Date  - name: tags    type: Multi --- # ProjectNote.md --- extends: BaseNote fields:   - name: status    type: Select  - name: deadline    type: Date  - name: team    type: MultiFile --- # TaskNote.md --- extends: BaseNote fields:   - name: priority    type: Select  - name: assignee    type: File  - name: project    type: File ---`

## API Integration for AI Agents

## JavaScript API Access

**API Object**:

javascript

`const metadataMenuAPI = app.plugins.plugins["metadata-menu"].api;`

**Field Modifier Function** :[reddit](https://www.reddit.com/r/ObsidianMD/comments/xmnhwa/metadatamenu_02_lookup_fields/)​

javascript

`const {fieldModifier: f} = metadataMenuAPI; // Usage in DataviewJS dv.table(   ["File", "Status"],   dv.pages('"folder"').map(p => [     p.file.link,     f(dv, p, "status")  // Renders editable field   ]) );`

## Programmatic Field Modification

**Command Palette Integration** :[reddit](https://www.reddit.com/r/ObsidianMD/comments/17wz7pt/metadata_menu_060_public_beta_is_out/)​

text

`Commands available: - Add field at cursor - Add field at section - Add field in frontmatter - Manage Class fields - Add Class to file - Add new Class - Update Field - Open Class modal`

**Keyboard Navigation** :[reddit](https://www.reddit.com/r/ObsidianMD/comments/17wz7pt/metadata_menu_060_public_beta_is_out/)​

- Full keyboard operability for field management
    
- Hotkey support for commands
    
- Modal navigation in nested fields
    

## Data Structures

## Field Definition Schema

typescript

`interface FieldDefinition {   name: string;   type: FieldType;   id: string;   path: string;   options: FieldOptions; } type FieldType =    | "Input" | "Boolean" | "Number"   | "Select" | "Multi" | "Cycle"   | "File" | "MultiFile" | "Media" | "MultiMedia"   | "Date" | "DateTime" | "Time"   | "Lookup" | "Formula"   | "Canvas" | "CanvasGroup" | "CanvasGroupLink"   | "JSON" | "YAML" | "Object" | "ObjectList"; interface FieldOptions {   // Type-specific options   template?: string;  // Input   dateFormat?: string;  // Date/DateTime   defaultInsertAsLink?: boolean;  // Date   valuesList?: Record<string, string>;  // Select/Multi/Cycle   sourceType?: "ValuesList" | "ValuesFromPath" | "ValuesFromDVQuery";   dvQueryString?: string;  // File/MultiFile   queryTemplate?: string;  // Lookup   formula?: string;  // Formula   fields?: FieldDefinition[];  // Object/ObjectList }`

## FileClass Schema

typescript

`interface FileClassDefinition {   extends?: string;   excludes?: string[];   mapWithTag?: boolean;   tagNames?: string | string[];   filesPaths?: string | string[];   bookmarkGroups?: string | string[];   buttonIcon?: string;   maxRecordsPerPage?: number;   version?: string;   fields: FieldDefinition[]; }`

## Frontmatter Structure

text

`--- # FileClass assignment fileClass: className # or multiple fileClass: [class1, class2] # Field values fieldName: value selectField: selectedOption multiField: [option1, option2] dateField: 2025-10-15 fileField: "[[LinkedNote]]" multiFileField: ["[[Note1]]", "[[Note2]]"] booleanField: true numberField: 42 # Nested Object objectField:   subField1: value1  subField2: value2 # ObjectList objectListField:   - item1Field1: value1    item1Field2: value2  - item2Field1: value3    item2Field2: value4 ---`

## Performance Optimization

## Scope Selection Strategy

**Frontmatter-Only Mode** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/settings/)​

- Optimal for: Vaults with standardized frontmatter
    
- Performance: Fastest
    
- Limitation: No inline field management
    

**Frontmatter + Inline Mode** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/settings/)​

- Optimal for: Dataview-heavy workflows
    
- Performance: Slower with large files
    
- Capability: Full inline field support
    

## Exclusion Strategies

**File Exclusions** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/settings/)​

text

`Exclude patterns: - Template folders: "Templates/" - System files: "_system/" - Archives: "Archive/" - File extensions: ".excalidraw" - Name patterns: /^_.*/ (files starting with _)`

**Field Exclusions** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/settings/)​

text

`Globally ignored fields: - System fields: "id, uid, internal_id" - Auto-generated: "created_by_system, modified_by_system"`

## Index Management

**Internal Index** :[reddit](https://www.reddit.com/r/ObsidianMD/comments/xmnhwa/metadatamenu_02_lookup_fields/)​

- Synchronous operation after v0.2.0
    
- No async/await required in DataviewJS
    
- Automatic index updates on field changes
    

## Error Handling and Validation

## Field Validation Rules

**Type Constraints**:

- Boolean: Accepts only true/false/null
    
- Number: Validates numeric format
    
- Date/DateTime/Time: Validates temporal format
    
- Select/Multi: Validates against option list
    
- File/MultiFile: Validates file existence
    
- JSON: Validates JSON parse
    
- YAML: Validates YAML parse
    

**Constraint Violations**:

- Invalid values rejected
    
- Error feedback in UI
    
- Rollback to previous valid state
    

## FileClass Mapping Conflicts

**Multiple FileClass Scenario** :[mdelobelle.github](https://mdelobelle.github.io/metadatamenu/fileclasses/)​  
When note matches multiple FileClasses:

- All FileClasses apply
    
- Field name conflicts resolved by priority order
    
- Later FileClasses override earlier ones
    
- Explicit frontmatter FileClass highest priority
    

## Life Management System Implementation Guide

## Recommended Architecture

**Core FileClass Structure**:

text

`life-management/ ├── fileClasses/ │   ├── Base.md (common fields for all) │   ├── Goal.md (extends Base) │   ├── Project.md (extends Base) │   ├── Task.md (extends Base) │   ├── Habit.md (extends Base) │   ├── Journal.md (extends Base) │   ├── Note.md (extends Base) │   └── Review.md (extends Base)`

**Base FileClass Definition**:

text

`--- fields:   - name: created    type: DateTime  - name: modified    type: DateTime  - name: status    type: Select    options:      valuesList:        "0": "Active"        "1": "Archived"        "2": "Deleted"  - name: tags    type: Multi    options:      sourceType: "ValuesFromDVQuery"      valuesFromDVQuery: "dv.pages().flatMap(p => p.file.tags).distinct()"  - name: related    type: MultiFile    options:      dvQueryString: "dv.pages()" ---`

**Goal FileClass**:

text

`--- extends: Base mapWithTag: true tagNames: goal filesPaths: ["Goals"] fields:   - name: category    type: Select    options:      valuesList:        "0": "Health"        "1": "Career"        "2": "Finance"        "3": "Relationships"        "4": "Personal Growth"  - name: targetDate    type: Date  - name: progress    type: Number  - name: projects    type: MultiFile    options:      dvQueryString: "dv.pages().where(p => p.fileClass == 'Project')"  - name: milestones    type: ObjectList    options:      fields:        - name: milestone          type: Input        - name: deadline          type: Date        - name: completed          type: Boolean ---`

**Task FileClass**:

text

`--- extends: Base mapWithTag: true tagNames: task fields:   - name: priority    type: Select    options:      valuesList:        "0": "Critical"        "1": "High"        "2": "Medium"        "3": "Low"  - name: project    type: File    options:      dvQueryString: "dv.pages().where(p => p.fileClass == 'Project')"  - name: due    type: DateTime  - name: estimate    type: Number  - name: actual    type: Number  - name: completion    type: Formula    options:      formula: "this.actual && this.estimate ? Math.round((this.actual / this.estimate) * 100) : 0"  - name: daysUntilDue    type: Formula    options:      formula: "this.due ? Math.ceil((new Date(this.due) - new Date()) / (1000*60*60*24)) : null" ---`

**Habit FileClass**:

text

`--- extends: Base mapWithTag: true tagNames: habit fields:   - name: frequency    type: Select    options:      valuesList:        "0": "Daily"        "1": "Weekly"        "2": "Monthly"  - name: streak    type: Number  - name: lastCompleted    type: Date  - name: log    type: ObjectList    options:      fields:        - name: date          type: Date        - name: completed          type: Boolean        - name: notes          type: Input ---`

**Journal FileClass**:

text

`--- extends: Base mapWithTag: true tagNames: journal filesPaths: ["Journal"] fields:   - name: mood    type: Select    options:      valuesList:        "0": "Excellent"        "1": "Good"        "2": "Neutral"        "3": "Poor"        "4": "Terrible"  - name: energy    type: Number  - name: gratitude    type: Multi    options:      sourceType: "ValuesList"  - name: tasksCompleted    type: Lookup    options:      queryTemplate: "dv.pages().where(p => p.fileClass == 'Task' && p.status == 'Done' && p.modified.toString().includes(dv.current().file.name)).length"  - name: highlights    type: ObjectList    options:      fields:        - name: event          type: Input        - name: category          type: Select          options:            valuesList:              "0": "Win"              "1": "Learning"              "2": "Challenge" ---`

## Dashboard Implementation

**DataviewJS Dashboard**:

javascript

`const {fieldModifier: f} = this.app.plugins.plugins["metadata-menu"].api; // Active Goals dv.header(2, "Active Goals"); dv.table(   ["Goal", "Category", "Progress", "Target"],   dv.pages('"Goals"')     .where(p => p.status == "Active")     .map(p => [       p.file.link,       f(dv, p, "category"),       f(dv, p, "progress") + "%",       f(dv, p, "targetDate")     ]) ); // Critical Tasks dv.header(2, "Critical Tasks"); dv.table(   ["Task", "Project", "Due", "Days Until"],   dv.pages()     .where(p => p.fileClass == "Task" && p.priority == "Critical" && p.status != "Done")     .sort(p => p.due)     .map(p => [       p.file.link,       f(dv, p, "project"),       f(dv, p, "due"),       f(dv, p, "daysUntilDue")     ]) ); // Habit Tracking dv.header(2, "Habits"); dv.table(   ["Habit", "Frequency", "Streak", "Last"],   dv.pages()     .where(p => p.fileClass == "Habit")     .map(p => [       p.file.link,       f(dv, p, "frequency"),       f(dv, p, "streak"),       f(dv, p, "lastCompleted")     ]) );`

## Automation Patterns

**Template with Metadata Menu**:

text

`--- fileClass: Task created: <% tp.date.now("YYYY-MM-DD HH:mm") %> status: Active priority: <% tp.system.suggester(["Critical", "High", "Medium", "Low"], ["Critical", "High", "Medium", "Low"]) %> --- # <% tp.file.title %> ## Description ## Acceptance Criteria - [ ]  ## Notes`

**Lookup-Based Progress Tracking**:

text

`# In Project note completionRate:   type: Lookup  options:    queryTemplate: |      const tasks = dv.pages().where(p =>        p.fileClass == "Task" &&        p.project &&        p.project.path == dv.current().file.path      );      const total = tasks.length;      const done = tasks.where(t => t.status == "Done").length;      return total > 0 ? Math.round((done / total) * 100) : 0;`

## Troubleshooting Guide

## Common Issues

**Fields Not Appearing**:

1. Verify FileClass mapping (check priority order)
    
2. Confirm field definition in FileClass or settings
    
3. Check global exclusions list
    
4. Reload plugin after scope changes
    

**Lookup Fields Not Updating** :[github](https://github.com/mdelobelle/metadatamenu/issues/656)​

1. Verify Dataview plugin active
    
2. Check query syntax validity
    
3. Confirm field inheritance hierarchy
    
4. Test query in Dataview block first
    

**FileClass Not Applying**:

1. Verify FileClass file in configured folder
    
2. Check fileClass value matches filename (without .md)
    
3. Confirm no exclusion rules blocking
    
4. Check mapping priority conflicts
    

**Performance Issues**:

1. Switch to frontmatter-only mode
    
2. Add exclusion patterns for large folders
    
3. Limit ObjectList depth
    
4. Optimize Lookup queries
    

This comprehensive documentation provides the technical foundation for an AI agent to understand, modify, update, and refactor an Obsidian vault using the Metadata Menu plugin.