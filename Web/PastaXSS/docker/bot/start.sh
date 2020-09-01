#!/bin/bash
(cd app; gunicorn --user www-data --bind 0.0.0.0:8010 --workers 5 wsgi:app) &
nginx -g "daemon off;"
