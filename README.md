# React & Django Full Stack: web app, backend API, mobile apps

## Description
React single page web app, Django 2 REST API with Python 3, React Native cross platform mobile apps for Android and iOS.
### [Udemy Course Link](https://www.udemy.com/course/react-django-full-stack)

Steps:
1. Create GitHub repository
   - [GitHub](https://docs.github.com/en/get-started/quickstart/create-a-repo)
2. Download and Install Python3
   - [Python3](https://www.python.org/downloads)
3. Create virtual environment:
   - python3 -m venv .venv
4. Activate virtual environment:
   - source .venv/bin/activate
5. Install Django
   - pip install django==2.2
6. Create Project
   - django-admin startproject first .
7. RunServer
   - python3 manage.py runserver
8. Download and Install Pycharm
   - [Pycharm](https://www.jetbrains.com/pycharm/download)
9. Create App
   - django-admin startapp demo
10. Migrations
    - python3 manage.py migrate
11. Create in demo/models.py class `Book`
12. Add first/settings.py section INSTALLED_APPS new app `demo`
13. Apply new class for migrations
    - python3 manage.py makemigrations
    - python3 manage.py migrate
14. Create user and admin
    - python3 manage.py createsuperuser
15. Add first/admin.py class `Book`
16. Field Options
    - [field options](https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-options)
17. Change field options in class `Book` in demo/models.py and migrate
    - python3 manage.py makemigrations
    - python3 manage.py migrate
18. Field Types
    - [field options](https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types)
19. Add *description, price, published, is_published, cover* in class `Book` in demo/models.py and migrate
    - python3 manage.py makemigrations
    - python3 manage.py migrate
20. Create new *urls.py* in `demo` directory and add 'demo.urls' path to *first/urls.py*
21. Create function in *demo/views.py* file and add the function name to `demo/urls.py` file
22. Create Another class in *demo/views.py* file and add the function name to `demo/urls.py` file
23. Add title, id of books to `Another class` in *demo/views.py* and use all(), filter(), get()
24. Templates
    - Add 'templates' in first/settings.py TEMPLATES->DIRS->'templates'
    - Create first_temp.html add some text in h1 and h2
    - add 'first_temp.html' in demo/views.py
    - Change url in demo/urls.py 
    - Change code in demo/views.py
25. DjangoRestFramework
    - pip install djangorestframework
    - add in INSTALLED_APPS (setting.py) `rest_framework`
    - add file serializers.py
    - change views.py file
    - change urls.py file
26. Token
    - add in INSTALLED_APPS (setting.py) `rest_framework.authtoken`
    - add in first/urls.py `path('auth/', obtain_auth_token)`
27. Permissions
    - add in settings.py `REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
    }`
    - add in views.py `authentication_classes`
    - add in views.py `permission_classes`
28. One to one
    - add in models.py `BookNumber`
    - add in admin.py `BookNumber`
    - add in serializers.py `BookNumberSerializer`
29. One to Many
    - add in models.py `Character`
    - add in admin.py `Character`
    - - add in serializers.py `CharacterSerializer`