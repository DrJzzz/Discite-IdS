# Build django 

Move to directory `anki_server`

## Requirments

For install all the packages that need the project 
```bash
pip install -r requirements.txt
```


## Create database

To setup all the tables in our app
```bash
python manage.py makemigrations snippets

python manage.py makemigrations

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