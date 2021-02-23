python manage.py makemigrations
python manage.py migrate 
gunicorn restapi.wsgi --bind 0.0.0.0:8000