python manage.py makemigrations guia &&
python manage.py migrate &&
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell &&



gunicorn guiasuldabahia.wsgi:application --bind 0.0.0.0:8000
