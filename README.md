# dikultur

"Portal" for gathering study resources, events and other stuff at DIKU.

## Requirements

- Python 3
- Django 1.7

See ``requirements.txt`` for other requirements.

## Quick setup

0. Create virtualenv
1. Install requirements: pip install -r requirements.txt
2. Set environment variables (database, smtp etc.) in dikultur/settings/.env - see dikultur/settings/env_sample for required settings
3. Run migrate: ./manage.py migrate
4. Run server: ./manage.py runserver

Of course deploying to production is a bit more complicated (but not much).