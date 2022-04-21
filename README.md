# automated-testing-repository

# Run locally

## Web
### Development with default SQLite database
1) Install requirements from web/requirements.txt
2) Create .env file from .env_example in web directory with your smtp parameters (for sending activation email)
3) In command line from directory web:
```shell
# Migrate all models to db
python manage.py makemigrations
python manage.py migrate

# Create admin user for admin panel
python manage.py create superuser 

# Run server
python manage.py runserver   
```
4) Server started at localhost with 8000 port and all the api endpoints are ready to connection.