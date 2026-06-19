["id", "created_at", "name", "has_test", "alternate_url"]
,
(.items[]
    | select (.name | ascii_downcase | contains ("data scientist"))
    | [.id, .created_at, .name, .has_test, .alternate_url])
| @csv