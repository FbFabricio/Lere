python3 manage.py migraate --noinput
python3 manage.py collectstatic --noinput 
gunicorn lere.wsgi:application --bind 0.0.0.0:$PORT