# kraksat-server

## Configuration

### Requirements
* Python 3.5

### Before running anything
```
export DJANGO_SETTINGS_MODULE=kraksat_server.settings.local
```
For running the server on production, copy
`kraksat_server/settings/production.py.example` to `production.py`, modify
as needed and then use:
```
export DJANGO_SETTINGS_MODULE=kraksat_server.settings.production
```

### Installing
```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

### Running
```
python manage.py runserver
```

### Unit Testing
```
python manage.py test
```

## Usage

### Authentication

We use token-based authentication as described in
[Django REST Framework docs](http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication).
Basically, an `Authorization` HTTP header is needed for every "non-safe" or
"write" requests (i.e. all but `GET`, `OPTIONS` and `HEAD`), like so:
```
Authorization: Token 28619272344753805f6f6724c8c6f0d7ea5aeb42
```
A token for a particular user can be obtained using `/token-auth/` API endpoint:
```
$ curl -X POST http://127.0.0.1:8000/token-auth/ -d "username=test&password=test"
{"token":"28619272344753805f6f6724c8c6f0d7ea5aeb42"}
```
