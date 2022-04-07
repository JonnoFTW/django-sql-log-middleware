import json
import re
import time

from django.conf import settings
from django.http import HttpRequest, HttpResponse

try:
    from django.utils.deprecation import MiddlewareMixin as Parent
except ImportError:
    Parent = object


class SqlLogMiddleware(Parent):
    """Output the sql used in the view.
    """

    def process_response(self, request: HttpRequest, response: HttpResponse):
        """Log all the sql queries for the Django orm.
        """
        from django.db import connection
        should_run = getattr(settings, 'SQLLOG_MIDDLEWARE', True)
        if str(should_run).lower() == "false":
            return response
        path_re = getattr(settings, 'SQLLOG_PATH_RE', r".*")
        output_path = getattr(settings, "SQLLOG_LOG", "django_queries.jsonl")
        runnable = getattr(settings, 'DEBUG', False) or getattr(settings, 'TESTING', False)
        if should_run and runnable and re.search(path_re, request.path):
            queries = connection.queries
            if len(queries) > 0:
                self.log_queries(request, queries, output_path)
        return response

    def log_queries(self, request: HttpRequest, queries, output_path):
        """Write queries to jsonl all the queries.

        Each JSON is an object per request with:
        {
            path: '/path',
            time: 1649301150,
            queries: [
                {sql: "select * from users", time: 1.1234},
                {sql: "select * from things", time: 4.1234},
            ]
        }

        """

        data = {
            "path": request.get_full_path(),
            "time": int(time.time()),
            "queries": [
                q for q in queries
            ]
        }
        with open(output_path, 'a') as out_file:
            out_file.write(json.dumps(data) + "\n")
