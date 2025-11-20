python -m pip install --upgrade build 
pip install -r requirements.txt 
python manage.py migrate
python create_superuser.py