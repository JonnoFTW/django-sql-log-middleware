# Django SQL Log Middleware

A middleware to write Django SQL queries and stats to a jsonl file. Makes analysis easier when you have log files
that are hundreds of megabytes.

Inspired by the [django-sqlprint-middleware](https://github.com/thebjorn/django-sqlprint-middleware) project

## Installation

```
pip install django-sql-log-middleware
```

Add it to the middleware section of settings.py:

```py
MIDDLEWARE = [
    ...
    'django_sql_log_middleware.SqlLogMiddleware',
]
```

## Output

Output will be written to the path specified in `SQLLOG_LOGFILE` in the below format. Each line is a JSON object
covering a single request. Time is the current unix time. Query time is measured in seconds.

```json
{
        "path": "/path/to/api?abc=1234",
        "time": 1649301150,
        "queries": [
            {"sql": "select * from users", "time": 1.1234},
            {"sql": "select * from things", "time": 4.1234},
        ]
}
```

## Settings

Specify the following settings in your settings.py file:

* **DEBUG** This middleware will only run when DEBUG is set.
* **SQLLOG_MIDDLEWARE** set this variable to `False` disable the middleware without removal. Defaults to `True`
* **SQLLOG_PATH_RE** a regex pattern to only log SQL queries in hte matched path(s). Defaults to `.*`
* **SQLLOG_LOG** the file to write out the logs to. Defaults to `django_queries.jsonl`
