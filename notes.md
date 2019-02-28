# Setting up
```
$django-admin.py startproject [project name]
```
- Creates scaffolding for project
```
	>>> django-admin.py startproject addressbook
	>>>	manage.py	        # Is a pointer back to django-admin.py *WITH* an environment variable set, 
				        #pointing to this project as the one to read settings from and operate on when needed.
		./addressbook	
			__init__.py	# This is a an empty file
			settings.py	# This is where you'll configure the project. Sensible defaults, bu no database chosen when you start
			urls.py		# contains the URL ---> VIEW mappings
			wsgi.py		# This is a WSGI (Web Server Gateway Interface) for your application. Used by dev servers, and possibly other containers
```
## 1. Creating the "App"
```
$ python ./manage.py startapp [application name]
```
- Creates a new application in the project. 
- **SINCE Django 1.4** : Apps are placed alongside _project_ packages. Advantageous in terms of deployment
```
	>>> python ./manage.py startapp contacts
	>>>	./addressbook
		./contacts
			__init__.py
			models.py	# Will contain the Django ORM models for this app
			tests.py	# Will contain the View code
			views.py	# Will contain the unit and integration tests that are written

```

# Using Models

## 1. Configuring the Database
Django has support for { MySQL, PostgreSQL, SQLite3, Oracle } 
- When using MySQL (for example) you'd need mysql-python to support your requirements.txt file

- When choosing a database, you need to edit the DATABASES definition in `addressbook/settings.py`.
```
		DATABASES = {
		    'default': {
		        'ENGINE': 'django.db.backends.sqlite3',  # 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		        'NAME': 'address.db',
		        'USER': '',                      # Not used with sqlite3.
		        'PASSWORD': '',                  # Not used with sqlite3.
		        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
		        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
		    }
		}
```
## 2. Creating a model
A model in Django closely resembles a database table. A place to encapsulate business logic. 
ALL models subclass the base Model, each subclass has field conditions.
```
	>>> contacts/models.py
		from django.db import models
		# A list of fields can be found: https://docs.djangoproject.com/en/1.8/ref/models/fields/
		class Contact(models.Model):
			first_name = models.CharField(
				max_length=255,
			)

			last_name = models.CharField(
				max_length=255,
			)
		
			email = models.EmailField()

			def __str__(self):
				return ''.join([
					self.first_name,
					self.last_name
				])
```	

- Once created, the app needs to be installed in INSTALLED_APPS settings
```
		INSTALLED_APPS = (
		    'django.contrib.auth',
		    'django.contrib.contenttypes',
		    'django.contrib.sessions',
		    'django.contrib.sites',
		    'django.contrib.messages',
		    'django.contrib.staticfiles',
		    # Uncomment the next line to enable the admin:
		    # 'django.contrib.admin',
		    # Uncomment the next line to enable admin documentation:
		    # 'django.contrib.admindocs',
		    'contacts',
		)

	>>> python manage.py migrate
```

# Writing Views
## 1. View Basics
Django view take an **HTTP Request** and return to the user a **HTTP Response**
Any Python object can be a view, it must take in a request parameter
```python
from django.http import HttpResponse

def hello_world(request):
	return HttpResponse("Hello World")
```
This is the simpliest form of a view.
The ListView is a subclass which has additional behaviors, we can create a view in the `views.py` file as follows:
```python
from django.views.generic import ListView

from contacts.models import Contact


class ListContactView(ListView):

    model = Contact
```

## 2. Defining URLs
A URL is how Django delgates a request to the python code. Django makes use of `urlpatterns` in the `urls.py` file, located in the **project**

An example URL mapping for the Contact ListView would look like this:
```python
from django.conf.urls import patterns, include, url

import contacts.views


urlpatterns = patterns('',
    url(r'^$', contacts.views.ListContactView.as_view(),
        name='contacts-list',),
)
```
### Some important notes
- The URL function is not _strictly_ required. Used mostly for clarity
- The first parameter is a `Regular Expression`
- The second parameter is a view callable, can also be a module name string
	- If we're using a class based view (which we are) this **must** be a real object
- Giving the URL pattern an name allows for reverse lookup!

