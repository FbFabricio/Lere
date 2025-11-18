python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput 
gunicorn lere.wsgi:application --bind 0.0.0.0:$PORT
