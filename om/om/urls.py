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
# remember to add views here as you create them
from hist.views import DecisionList, DecisionDetail, EmployeeList, EmployeeDetail
# using functional view
# from hist.views import decision_details

urlpatterns = [
    path('admin/', admin.site.urls),
    # using functional view
    # path('hist/<int:dec_id>', decision_details),
    path('hist/<int:pk>', DecisionDetail.as_view()),
    path('hist/', DecisionList.as_view()),
    path('employee/<int:pk>', EmployeeDetail.as_view()),
    path('employee/', EmployeeList.as_view())

]
