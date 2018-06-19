# flango_ms
Creating microservices using frameworks Django and Flask

## Flask + Django + MicroServices = flango_ms

- This is a bioler plate to create microservices using django and flask

- I have used awesomeness of Django's ORM to deal with the database and simplicity of Flask to create a service

### Steps to make it up and running

- Create virtualenv with python3: `virtualenv env_flango -p python3`
- Clone repo
- `cd flango_ms`
- Start virtual environment: `source ../env_flango/bin/activate`
- Install the requirements: `pip install -r requirements.txt`
- Do migrations:
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- Start Django server: `python manage.py runserver`
- Start service1: `python service1.py`

### Play with the service

- Goto url http://127.0.0.1:5000/ which is serivce1
  You should see 0 as there are no hits.
  now hit utl http://127.0.0.1:5000/hit/something
  You should see _Hit created successfully_
- Check the count it should have incremented
- Do these steps several times
- Now check the django server: http://127.0.0.1:8000/admin/app_poc/hit/
- You should see a list of hits you have created.

#### Event if the Django server is shut, service created in flask will be able to access the models from the Django. ####
