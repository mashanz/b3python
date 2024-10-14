#!/bin/sh
GRANIAN_WORKERS=$(nproc --all) uv run granian django_modular.wsgi:application --host 0.0.0.0 --interface wsgi