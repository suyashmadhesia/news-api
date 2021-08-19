web: gunicorn apnamau.wsgi:application --preload --workers 1
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput
