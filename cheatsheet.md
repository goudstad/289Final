\| [HOME](README.md) \|
# CHEATSHEET
### Dataset template
-  d1=Decision(title="Purchase Microsoft Office", decisions="Our Office will purchase two licenses", decisionDate="2016-01-02", backgroundInfo="Two licenses are sufficient to keep the office running", rationale="There are only two people in the office",subject="purchonase",decisionMaker=e)

### To create a test dataset 
- mkdir hist\fixtures
- python manage.py dumpdata hist > hist/fixtures/test_data.json

### Copying database
- copy db back_db

### Django management commands

    - python manage.py shell starts the Python interpreter that is Django aware.
    - python manage.py dbshell starts the shell for SQLite3 (or whatever RDBMS you configure)
    - python manage.py runserver runs your application on port 8000 (point your browser at http://127.0.0.1:8000)
    - python manage.py test catalog runs the test suite in the catalog/tests.py file
    - python manage.py makemigrations checks for changes to your models and makes a migration file
    - python manage.py migrate converts migration files to SQL and implements the changes in the database




  
