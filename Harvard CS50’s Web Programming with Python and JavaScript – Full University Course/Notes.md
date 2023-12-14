# Notes for CS50's Web Programming Course

Installing Django: pip3 install Django

Creating a Django Project: django-admin startproject PROJECT_NAME

Running the Django Project: python3 manage.py runserver

Creating an app in our Django Project: python3 manage.py startapp APP_NAME

When creating a new app and rendering an html page, remember to add project name in settings.py
under INSTALLED_APPS. After that also make sure that the location of the html file follows the
following directory style in the app folder: templates/APP_NAME/HTML_FILE.
