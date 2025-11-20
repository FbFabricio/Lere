
python manage.py makemigrations --noinput 
python manage.py migrate --noinput
python manage.py collectstatic --noinput 

gunicorn lere.wsgi:application --bind 0.0.0.0:$PORT


<<<<<<< HEAD
=======

>>>>>>> 662bb352860e10964956edca2cf818a2f13cbc44
