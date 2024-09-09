# Build Step (initial build dependency)
FROM python:3.11.9-bullseye AS build
RUN pip install pdm
WORKDIR /app-build
COPY . .
RUN pdm build
RUN pdm install
RUN pdm run src/manage.py collectstatic --noinput

# Build for dependency to production
FROM python:3.11.9-bullseye AS build-to-prod
WORKDIR /build-to-prod
COPY --from=build /app-build/dist/*.whl .
RUN pip install *.whl --no-cache-dir --prefer-binary

# Runner Apps
FROM gcr.io/distroless/python3-debian12:latest AS runner
WORKDIR /app-runner
USER nonroot
COPY --from=build-to-prod /usr/local/bin/granian /usr/local/bin/granian
COPY --from=build-to-prod /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build /app-build/src/static /app-runner/src/static
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages
COPY src/manage.py .
EXPOSE 8000
CMD ["/usr/local/bin/granian", "django_modular.wsgi:application", "--host", "0.0.0.0", "--interface", "wsgi"]