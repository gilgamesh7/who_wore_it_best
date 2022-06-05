# who_wore_it_best

# Set up for development
1. Install & activate venv (python3 -m venv venv --upgrade-deps)
2. Generate project : ./venv/bin/django-admin startproject vote_rajesh .
3. Generate application : python3 manage.py startapp who_wore_it_best

# Migrate
1. python manage.py makemigrations
2. python manage.py migrate

# Run server
python3 manage.py runserver 127.0.0.1:8001

# Create superuser
