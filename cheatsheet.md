\| [HOME](README.md) \|
# CHEATSHEET
*This page lists some of the frequent commands used to create this project.*

# Command Line
### Copying database
- `copy db back_db`
### Changing Directory - two levels up
`cd..\..\`

# Python
### Create Virtual Environment
- Create a virtual environment in the current directory: `python -m venv ENV`
- Activate the environment in Windows: `ENV\Scripts\activate`
- Install the dependencies: `pip install -r requirements.txt`

### General
- See list of installed packages: `pip list`

# Django
### Creating a Django Project
- $ `django-admin startproject` mysite

### Creating a Django App
- $ `python mange.py startapp` myapp
	- This will create a folder

### Dataset template
-  d1=Decision(title="Purchase Microsoft Office", decisions="Our Office will purchase two licenses", decisionDate="2016-01-02", backgroundInfo="Two licenses are sufficient to keep the office running", rationale="There are only two people in the office",subject="purchonase",decisionMaker=e)

### To create a test dataset 
- mkdir hist\fixtures
- python manage.py dumpdata hist > hist/fixtures/test_data.json

### Querying models
- `python manage.py shell`
```python
from hist.models import *
h1 = Decision ()
h1.title = "blah"
h1.save ()
from employee.models import *
e1 = Employee.objects.get(pk=1)
```

### Django management commands
*Source: [https://github.com/joshuago78/labcat](https://github.com/joshuago78/labcat)*
- `python manage.py shell` starts the Python interpreter that is Django aware.
- `python manage.py dbshell` starts the shell for SQLite3 (or whatever RDBMS you configure)
- `python manage.py runserver` runs your application on port 8000 (point your browser at http://127.0.0.1:8000)
	- Ctrl + C exits out the runserver
- `python manage.py test catalog` runs the test suite in the catalog/tests.py file
- `python manage.py makemigrations` checks for changes to your models and makes a migration file
- `python manage.py migrate` converts migration files to SQL and implements the changes in the database

# Git
### Git commands
- `git clone https://github.com/joshuago78/labcat.git`
- `git pull`
- `git branch`
- `git checkout master`
- `git merge master`
- `git commit`
- `git push original`
- `git ini`
	- Initialize empty git repository
- `git checkout -b project-models/1`
	- Switches to a new branch ‘project-models/1’

# SQLite 3
## FAQs
1. I keep getting AttributeError about fields that I renamed.
	- I resolved this by deleting the db.sqlite 3 file in side the om folder
	- I also removed the .py files inside hist > migration but leaving __init__.py intact.
	- I then run python manage.py makemigrations and python manage.py migrate.




  
