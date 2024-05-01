# django-auth
This project is about Auth Example for django JWT with django ninja

# Process of macking project
### make virtual env 
- `conda create -n auth`
- things to install is listed in [requirments.txt](requirements.txt)
    - can install by running `conda create --name <env> --file requirements.txt`
    - `pip install django-cors-header` sholud be run additionally

### setting django
``` terminal
$ django-admin startproject backend
$ python manage.py startapp people
```
- fix setting.py, urls.py, models.py
- make api.py
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver 
```

### Testing
- make user in `localhost:{portnum}/admin`
- get access token in `localhost:{portnum}/api/docs`
- auth with this in `localhost:{portnum}/api/docs`'s top right button
- test `add api`

> anyway when we go out from window, auth disappear