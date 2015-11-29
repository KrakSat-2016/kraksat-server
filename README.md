# kraksat-server

## Requirements
* Python 3.5

## Before running anything
```
export DJANGO_SETTINGS_MODULE=kraksat_server.settings.local
```
For running server on production, copy
`kraksat_server/settings/production.py.example` to `production.py`, modify
as needed and then use:
```
export DJANGO_SETTINGS_MODULE=kraksat_server.settings.production
```

## Installing
```
pip install -r requirements.txt
python manage.py migrate
```

## Running
```
python manage.py runserver
```

## Unit Testing
```
python manage.py test
```
