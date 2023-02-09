git pull &&
python manage.py makemigrations guia &&
python manage.py migrate &&
python manage.py collectstatic &&



gunicorn guiasuldabahia.wsgi:application --bind 0.0.0.0:8000
