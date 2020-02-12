# EDITS

## ERRORS

- encountered an error while migrating...

```
  File "/Users/aldo/sei/labs/Auto-swap/.env/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
psycopg2.errors.StringDataRightTruncation: value too long for type character varying(100)
```

### solution

- dropped the database
- edited the seed file, used a shorter img_url for Car.
- did makemigrations and migrated again.
