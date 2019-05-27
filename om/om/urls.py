"""om URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
# remember to add views here as you create them
from hist.views import DecisionList, DecisionDetail, DecisionCreate, DecisionUpdate, DecisionDelete, EmployeeList, EmployeeDetail, EmployeeCreate, EmployeeUpdate, EmployeeDelete, index, ContactView
# using functional view
# from hist.views import decision_details

urlpatterns = [
    path('admin/', admin.site.urls),
    # using functional view
    # path('hist/<int:dec_id>', decision_details),
    path('',index,name='index'), # home page
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
    path('contact', ContactView.as_view(), name='contact-view'),
]
