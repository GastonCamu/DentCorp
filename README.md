# DentCorp
Empresa ficticia como proyecto final de la tec. analista superior de sistemas (ISDM)

source venv/Scripts/activate

Dependencias a instalar:

virtualenv venv
pip install django
pip install pymysql
pip install django-extensions
pip install crispy-bootstrap5
pip install Pillow

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
