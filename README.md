# Django Currency Api
This api is base on django_restful

# Requirements
- Python 3.6
- Django 2
- Django REST Framework

# Installation

	pip install django
	pip install djangorestframework
	pip install requests
	pip install django-cors-headers
	
# Structure
| Endpoint   | Method  | Desciption  | Arguments  |
| ---------- | ------- | ----------- | ---------- |
| currencies | GET | Returns all the currencies with ZAR as a base | None  |
| currencies | POST | Returns the conversed value of the currency in rands value | currency(string),value(number) |
| currencies | PUT | Updates The values of the currecies in the database | None   |

## URLS Views
- GET  :8000/currencies- Returns all the currencies with ZAR as a base
- POST :8000/currencies --arguments required currency(string)-Name of the currency to be converted, value(float)-Amount of the currency 
- PUT  :8000/currencies Updates The values of the currecies in the database

### Installation
	python manage.py runserver
  
### Usage
  Start the vuew project and make sure it is running in the same host with the api
