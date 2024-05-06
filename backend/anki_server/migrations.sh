#!/bin/bash

rm -rf cards/migrations
rm -rf userapp/migrations
rm -rf decks/migrations
rm -rf notes/migrations
rm -rf images/migrations

python manage.py makemigrations

python manage.py makemigrations cards
python manage.py makemigrations userapp
python manage.py makemigrations decks
python manage.py makemigrations notes
python manage.py makemigrations images

python manage.py migrate