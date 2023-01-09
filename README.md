
# Documentation of Family Budget

This project use "Python" as main programming languages and "Django" as main python-framework.

To start this poject you need python3.9
Install python3.9 from this link https://www.python.org/downloads/release/python-394/


## How to start
Update pip if you need

- pip install -m requirements.txt
- python manage.py loaddata users_data.json
- python manage.py loaddata category_data.json
- python manage.py loaddata сurrency_data.json
- python manage.py runserver

On users_data.json you alredy load super user
login: admin
password: admin


## Create new superuser if you need
- python manage.py createsuperuser

## Admin panel
Start project
- python manage.py runserver

Go to http://127.0.0.1:8000/admin/
By default, Django starts on localhost with 8000 port. Change this value if you use another port.

Use the superuser password and username to login into admin panel