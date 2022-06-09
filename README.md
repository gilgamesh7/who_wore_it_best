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
python3 manage.py createsuperuser

# If moving to Heroku (Doesnt work properly yet)
- https://realpython.com/django-hosting-on-heroku/#bootstrap-a-django-project
- https://whoworeitbest-spark.herokuapp.com
- heroku login
- heroku create whoworeitbest-spark
- heroku git:remote --app  whoworeitbest-spark  

- echo python-3.9.6 > runtime.txt
- git add runtime.txt
- git commit -m "Request a specific Python version"  

- git push heroku HEAD:master

# Links
- Vote : http://whoworeitbest.azurewebsites.net/who_wore_it_best/vote
- Get Results : http://whoworeitbest.azurewebsites.net/who_wore_it_best/getvotes
- Admin : http://whoworeitbest.azurewebsites.net/admin/who_wore_it_best/peoplevote/