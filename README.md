[![Build Status](https://travis-ci.com/goudstad/om.svg?branch=master)](https://travis-ci.com/goudstad/om) [![Coverage Status](https://coveralls.io/repos/github/goudstad/om/badge.svg?branch=master)](https://coveralls.io/github/goudstad/om?branch=master)

# 289Final
This GitHub repository was created for the Web Development class during Spring quarter 2019.

## Project
The concept of this project is to create a prototype that can used to track business decisions organizatonal memory.

### Dataset template
-  d1=Decision(title="Purchase Microsoft Office", decisions="Our Office will purchase two licenses", decisionDate="2016-01-02", backgroundInfo="Two licenses are sufficient to keep the office running", rationale="There are only two people in the office",subject="purchonase",decisionMaker=e)

### To create a test dataset 
- mkdir hist\fixtures
- python manage.py dumpdata hist > hist/fixtures/test_data.json

