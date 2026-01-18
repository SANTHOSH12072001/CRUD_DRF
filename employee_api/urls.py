from django.urls import path
from .views import *

urlpatterns=[
    path("employees/", EmployeeApi.as_view()),
    path("employees/<int:id>/", EmployeeApi.as_view())
]