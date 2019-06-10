[![Build Status](https://travis-ci.com/goudstad/289Final.svg?branch=master)](https://travis-ci.com/goudstad/289Final)
[![Coverage Status](https://coveralls.io/repos/github/goudstad/289Final/badge.svg?branch=master)](https://coveralls.io/github/goudstad/289Final?branch=master)

\| [README](README.md) \| [CHEATSHEET](cheatsheet.md) \| [RESOURCES](resources.md) \| [KNOWN ISSUES](knownIssues.md) \|
***
# 289Final
*Welcome to 289Final.  This GitHub repository is a final class project created for IS 289 course: Web Development during Spring quarter 2019. This prototype database uses Python, Django, and SQLite 3 to track business decisions in order to enhance organizatonal memory.*  

This web application project contains the followings:
- Two models: 
    1. Decision
    2. Employee
- Two relationships: 
Decisions to employees (many-to-many) on fields `decisionMaker` and `enteredby`
    1. Multiple decisions can be made by multiple employees within an organization.
    2. Multiple decisions can be entered by multiple employees within an organization.
- 11 views and 11 templates
- One form
    1. Contact Form
- Bootstrap to enhance look and feel.
- 5 sample data for the Decision model, and 10 sample data for the Employee model.
  - Fixtures
  - Custom Import Script (attempted)
- Navigations through menus.
- Creation of new data can be done either via custom forms or through Django admin.
```
    path('admin/', admin.site.urls),
    path('', index, name='index'), # home page
    path('hist/', DecisionList.as_view(), name='hist-list'),
    path('hist/add', DecisionCreate.as_view(), name='hist-add'),
    path('hist/<int:pk>', DecisionDetail.as_view(), name='hist-detail'),
    path('hist/<int:pk>/edit', DecisionUpdate.as_view(), name='hist-update'),
    path('hist/<int:pk>/delete', DecisionDelete.as_view(), name='hist-delete'),    
    path('employee/', EmployeeList.as_view(), name='employee-list'),
    path('employee/add', EmployeeCreate.as_view(), name='employee-add'),
    path('employee/<int:pk>', EmployeeDetail.as_view(), name='employee-detail'),    
    path('employee/<int:pk>/edit', EmployeeUpdate.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete', EmployeeDelete.as_view(), name='employee-delete'),
    path('contact', ContactView.as_view(), name='contact-view')
 ```
- Added Travis CI and Coveralls

-Raymond Huang*

