# flango_ms
Creating microservices using frameworks Django and Flask

## Flask + Django + MicroServices = flango_ms

- This is a bioler plate to create microservices using django and flask

- I have used awesomeness of Django's ORM to deal with the database and simplicity of Flask to create a service

### Steps to make it up and running

- Create virtualenv with python3: `virtualenv env_flango -p python3`
- Clone repo
- `cd flango_ms`
- Start virtual environment: `source env_flango/bin/activate`
- Install the requirements: `pip install -r requirements.txt`
- Do migrations:
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- Start Django server: `python manage.py runserver`
- Start service1: `python service1.py`
