#!/usr/bin/env sh
set -e

echo "Waiting for DB..."
python - <<'PY'
import os, time, psycopg2
host=os.getenv("POSTGRES_HOST","db")
port=int(os.getenv("POSTGRES_PORT","5432"))
db=os.getenv("POSTGRES_DB")
user=os.getenv("POSTGRES_USER")
pw=os.getenv("POSTGRES_PASSWORD")
for i in range(60):
    try:
        psycopg2.connect(host=host, port=port, dbname=db, user=user, password=pw).close()
        print("DB is up")
        break
    except Exception as e:
        time.sleep(1)
else:
    raise SystemExit("DB not ready")
PY

echo "Apply migrations..."
python manage.py migrate --noinput

echo "Collect static..."
python manage.py collectstatic --noinput || true

echo "Start gunicorn..."
exec gunicorn main.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 60
