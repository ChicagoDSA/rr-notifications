# rr-notifications
Application for mass texting to specific groups. It uses Twilio to send the messages and Django to manage administration and signup


## Installation for Dev

You'll need a few things on your machine to get started. Currently, this guide assumes you are using a Linux or Mac.

### Prerequisites
Make sure to have the following installed

* Python 3.6.*
* [pipenv](https://docs.pipenv.org/)
	* [Basic Usage Docs](https://docs.pipenv.org/basics/)
* [yarn](https://yarnpkg.com/en/) or npm (for frontend work)

### Django Setup

Django 2.0 is being used. All the required Python packages are managed using pipenv. It's probably worthwhile to learn a bit about pipenv. 



To install what's needed move to the nested rr-notifications directory. There will be a `Pipfile` and `Pipfile.lock`

In the terminal,
  
  ```bash
  pipenv shell
  
  # Make sure you are using Python 3 and it's a virtualenv copy
  # The following commands should point to wherever you 
  # configured your virtualenvs to stored
  
  which python 
  
  # check for python 3
  python --version 
  
  # Should be 3.6.5. If not make sure you have installed and activated the venv correctly
  ```
That will activate a Python virtual environment for the project. 

Next, install the packages specified in `Pipfiile` and `Pipfile.lock`. Always be sure to include those files in future commits if more pip packages are installed.

```bash
pipenv sync
```
Let's fire up a dev server now that the virtualenv has the required packages.

The Pipfile includes a package named [`django-extensions` ](https://github.com/django-extensions/django-extensions). This package has improved versions of some Django's management commands. One of them is an improved version of the regular dev server. Do the following to start that bad boy up.
```
# Move to the Django project root dir
cd rr-notifications

# Run database migrations
python manage.py migrate

# Get the dev server popping
python manage.py runserver_plus

```

Now go to [localhost:8000](http://localhost:8000) and you should hopefully see an ugly green page.


