@@ -1,56 +0,0 @@
# webapp

## Description
Perform CRU Operation on user using POST, PUT, GET http requests
## Tech Stack
- Python
- Django Framework
- PostgreSQL

## Features
- Django Rest Framework
- Rest API's
- Basic Authentication 
- Serializer's

## How to run the project
- Clone this repo and go inside repo in you local machine
- Create a virtual env using following command (windows)
    - `pip install virtualenvwrapper-win`
    - `virtualenv yourprojectenv`
    - `yourprojectenv\Scripts\activate`
- Install requirement.txt using following command -
    - `pip install -r requirement.txt`
    - You need to be inside project repo before running above command
- Run the server 
  - `python manage.py runserver`
- Install pgadmin for your device and set username and password also create a database for your webapp
- Change you database connectivity inside settings.py in your django app
    - Go to DATABASE variable
    - Change the following things :-
      - NAME which is your Database Name
      - USER which is `postgres` by default
      - PASSWORD which is your user password, default it is your pgadmin application password
- Run project using
    `python manage.py runserver`
- Go to `localhost:8000` to check your django application is running or not
- Once your project is running successfully you need to perform migration before using API's
- Steps to perform migration:-
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- If you want to access Django Admin panel you will need to create super user for the same.
    - `python manage.py createsuperuser`
    - Enter username and password you want to set up
    - Go check user is created successfully runserver and go to `localhost:8000/admin` and enter your creds

## External Lib 
  - bcrypt (For password hashing)
  - black linter (For code formatting)
  - psycopg2 (For postgreSQL connectivity)
  - django-rest-framework (For Rest API's)

## Unit Test
  - In order to run unit test use the following command
  - This project has two test cases 
    - For Post request testing 
    - For Get request testing for invalid user
  - `python manage.py test`
  