<<<<<<< HEAD
python manage.py makemigrations --noinput 
python manage.py migrate --noinput
python manage.py collectstatic --noinput 

gunicorn lere.wsgi:application --bind 0.0.0.0:$PORTuPI
=======
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput 
gunicorn lere.wsgi:application --bind 0.0.0.0:$PORT
>>>>>>> 7b8dcbb67fb106159a28ec7d47538139ed678784
