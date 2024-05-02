# Build django

Move to directory `anki_server`

## Requirements

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## Create database

Define the file `./anki_server/anki_server/.env` with the following structure:

```bash
SECRET_KEY='secret_key'
DB_NAME=db_name
DB_USER=db_user
DB_PASS=db_pass
DB_HOST=127.0.0.1
DB_PORT=5432
```

Use the PostgresSQL command line interface to run (based on the data contained
in `./anki_server/anki_server/.env` for `DB_USER`, `DB_PASS` and `DB_NAME`):

```bash
CREATE USER DB_USER WITH PASSWORD DB_PASS;
```

```bash
CREATE DATABASE DB_NAME OWNER DB_USER;
```

To setup all the tables in our app:

```bash
python manage.py makemigrations <appname>

python manage.py migrate
```

## Run server

```bash
python manage.py runserver
```

# Endpoints

URL `http://127.0.0.1:8000`
## User

### Register

POST `/rest-auth/registration/`

Parameter obligatory `name, email, phone_number, birth_date, password1, password2`
Return a token
```json
{
  "name": "string",
  "email": "johndoe@example.com",
  "phone_number": "0000000000",
  "birth_date": "YYYY-MM-DD",
  "max_reviews" : 0,
  "password1": "example",
  "password2": "example"

}
```
### Login
POST `/rest-auth/login/`

Return a token

```json
{
  "email": "test@test.com",
  "password": "example"
}
```

### User data
GET `/rest-auth/user/`

Return all data user in json

### Logout

POST `/rest-auth/logout/`

### Change Password

POST `/rest-auth/password/change/`

```json
{
  "new_password1": ".lo,kimju",
  "new_password2": ".lo,kimju"
}
```

### References
The algorithm for scheduling card review is obtained using the implementation of [Open Spaced Repetition](https://github.com/open-spaced-repetition/py-fsrs/tree/main).