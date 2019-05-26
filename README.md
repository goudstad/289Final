[![Build Status](https://travis-ci.com/goudstad/289Final.svg?branch=master)](https://travis-ci.com/goudstad/289Final)
[![Coverage Status](https://coveralls.io/repos/github/goudstad/289Final/badge.svg?branch=master)](https://coveralls.io/github/goudstad/289Final?branch=master)

\| [CHEATSHEETS](cheatsheet.md) \| [RESOURCES](resources.md) \| [KNOWN ISSUES](knownIssues.md) \|
# 289Final
*Welcome to 289Final.  This GitHub repository is a final class project created by Raymond Huang for IS 289 course: Web Development during Spring quarter 2019. This prototype database uses Python, Django, and SQLite 3 to track business decisions in order to enhance organizatonal memory.  

This web application project contains the followings:
- Two models: Decision and Employee.
- Two relationships: Decisions to employees (many-to-many) on fields decisionMaker and enteredby
  - Multiple decisions can be made by multiple employees within an organization.
  - Multiple decisions can be entered by multiple employees within an organization.
- Ten views and 9 templates
- Bootstrap to enhance look and feel.
- Five sample data for the Decision model, and 10 sample data for the Employee model.
  - Fixtures
  - Custom Import Script (attempted)
- Navigations through menus.
- Creation of new data can be done either via custom forms or through Django admin.
```
    admin/
    hist/ [name='hist-list']
    hist/add [name='hist-add']
    hist/<int:pk> [name='hist-detail']
    hist/<int:pk>/edit [name='hist-update']
    hist/<int:pk>/delete [name='hist-delete']
    employee/ [name='employee-list']
    employee/add [name='employee-add']
    employee/<int:pk> [name='employee-detail']
    employee/<int:pk>/edit [name='employee-update']
    employee/<int:pk>/delete [name='employee-delete']
 ```

-Raymond Huang*

