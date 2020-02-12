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

## ERRORS
_images not appeared in the main page

### solution

In settings, add MEDIA_URL and MEDIA_ROOT
```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
```

In auto folder, import settings and static
```
from django.conf import settings
from django.conf.urls.static import static
```
Then add this at the end of the urlpattern_array
```
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

