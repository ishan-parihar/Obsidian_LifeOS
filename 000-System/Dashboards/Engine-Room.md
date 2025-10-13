```dataview
dv.header(1, "The Engine Room - Resource Management");

// People Dashboard
dv.header(2, "People to Connect With");
dv.table(
  ["Name", "Relationship", "Last Contact", "Reconnect By"],
  dv.pages('"People"')
    .where(p => p.reconnect_by && p.reconnect_by <= date(today) + dur(7 days))
    .sort(p => p.reconnect_by, 'asc')
    .map(p => [p.file.link, p.relationship_status, p.last_connected_date, p.reconnect_by])
);

// Knowledge Areas
dv.header(2, "Knowledge Categories");
dv.list(
  dv.pages('"MOCs"')
    .file.name
    .map(name => link("MOCs/" + name))
);

// Recent Notes
dv.header(2, "Recent Notes");
dv.list(
  dv.pages('"Notes"')
    .sort(p => p.file.mtime, 'desc')
    .limit(10)
    .file.name
    .map(name => link("Notes/" + name))
);
```