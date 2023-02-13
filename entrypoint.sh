git pull 
python manage.py makemigrations guia 
python manage.py migrate 
gunicorn guiasuldabahia.wsgi:application --bind 0.0.0.0:8000
