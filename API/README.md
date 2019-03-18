# PETS API

## Set up development environment
Clone application
```
git clone https://CorecodeCmd@bitbucket.org/CorecodeCmd/pets-api-flask.git
```

Change directory to application folder
```
cd pets-api-flask
```

Set up virtualenv environment
```
pip install pipenv
pipenv shell
```

Install application requirements
```
pipenv install
```

Start application
```
python manage.py runserver
```

Use *https://localhost:5000/* as root endpoint in postman to start testing the application

Application endpoints

|Endpoint  |Description |
|----------|------------|
|GET: /pets/|List all pets|
|GET: /pets/{pet_id}/|Get an individual pet|
|POST: /pets/|Add a pet|
|PUT: /pets/{pet_id}/|Update an individual pet|
|DELETE: /pets/{pet_id}/|DELETE a pet|

When doing POST or PUT the sample request body is below
```json
{
    "name": "Jerry",
    "type": "Dog",
    "sex": "M",
    "age": 2
}
```

Run application tests
```
pytest -v
```