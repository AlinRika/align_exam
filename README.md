# Align exam
### Alina Kuznetsova
### mail: kuznetsovalina@list.ru

This is a small web app.
It uses:

* [Python](https://www.python.org/) as the main programming language
* [FastAPI](https://fastapi.tiangolo.com/) for the backend
* [SQLAlchemy](https://www.sqlalchemy.org/) for the database

Please, create directory ./app/app_logs/ for logging works

## Installing dependencies

To install project dependencies:

```bash
pip install -r requirements.txt
```

## Running the app

To run the app:

```bash
uvicorn app.main:app
```

Then, open your browser to [`http://127.0.0.1:8000`](http://127.0.0.1:8000) to load the app.
Open your browser to [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) to load the Swagger.
