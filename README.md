# Django REST framework test project

A starter project template to build a RESTful Web API using [Django REST framework](http://www.django-rest-framework.org/).

## Features

- Based on [Django REST framework official tutorial](http://www.django-rest-framework.org/tutorial/quickstart/).
- Integration with [Django REST Swagger](https://django-rest-swagger.readthedocs.io/en/latest/).
- Integration with Postgresql

## How to Use

To use this project, follow these steps:

1. Create your working environment.  See [Set up Python](http://sourabhbajaj.com/mac-setup/Python/README.html).
2. Install dependences using `pip`.  
3. Download this project.
4. Create and activate python virtual environment using `virtualenv venv && source venv/bin/activate`
5. Run `pip install -r requirements.txt` to install packages
6. Create Postgresql database with name `test_crm_db`. Run `docker-compose up -d` if there is no postgres service installed in local
7. Run `python manage.py migrate` to migrate database.
8. Run `python manage.py runserver` to start application.

- API root: [http://localhost:8000/](http://localhost:8000/) 
- Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

## Genarating `requirements.txt`

Run `pip freeze --local > requirements.txt`

## Dependences

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](http://www.django-rest-framework.org/)
- [Django REST Swagger](https://django-rest-swagger.readthedocs.io/)
- [DRF Docs](https://drf-yasg.readthedocs.io/en/stable/readme.html)
