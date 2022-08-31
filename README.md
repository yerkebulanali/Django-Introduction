# React & Django Full Stack: web app, backend API, mobile apps

## Description
React single page web app, Django 2 REST API with Python 3, React Native cross platform mobile apps for Android and iOS.
### [Udemy Course Link](https://www.udemy.com/course/react-django-full-stack)

Steps:
1. Create GitHub repository
   - [GitHub](https://docs.github.com/en/get-started/quickstart/create-a-repo)
2. Download and Install Python3
   - [Python3](https://www.python.org/downloads)
2. Create virtual environment:
   - python3 -m venv .venv
3. Activate virtual environment:
   - source .venv/bin/activate
4. Install Django
   - pip install django==2.2
5. Create Project
   - django-admin startproject first .
6. RunServer
   - python3 manage.py runserver
7. Download and Install Pycharm
   - [Pycharm](https://www.jetbrains.com/pycharm/download)
8. Create App
   - django-admin startapp demo
9. Migrations
   - python3 manage.py migrate
10. Create in demo/models.py class `Book`
11. Add first/settings.py section INSTALLED_APPS new app `demo`
12. Apply new class for migrations
    - python3 manage.py makemigrations
    - python3 manage.py migrate