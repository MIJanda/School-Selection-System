# School-Selection-System
A system to manage the selection criteria of schools


### Project Setup

Follow these steps to have a local running copy of the app.

##### Clone The Repo

`git clone https://github.com/MIJanda/School-Selection-System.git`

If `master` is not up to date, `git checkout develop`. However, note that code on develop could be having some minor issues to sort.

##### Install PostgreSQL

Here's a great resource to check out:

[How To Install and Use PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

Create the two databases `school_selection_db` (for development) and `school_selection_testing_db` (for unit testing).

##### Create a Virtual Environment

App was developed with `Python 3.6`.

Make sure you have `pip` installed on your machine.

Install the dependencies.

`pip install -r requirements.txt`

Create a `.env` file (which defines the environment variables used) at the root of the app.

Add the following details, customizing as needed.

```
export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_RUN_PORT=5000
```

Activate the virtual environment.

`. venv/bin/activate`

Run the application.

`flask run`

##### Testing and Coverage

This app uses `nose` to run tests.

`nosetests --with-coverage --cover-package=routes`
