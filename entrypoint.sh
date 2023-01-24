git pull
python manage.py makemigrations guia
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn guiasuldabahia.wsgi:application --bind 0.0.0.0:8000
