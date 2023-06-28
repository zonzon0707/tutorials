from django.urls import path
from . import views 

urlpatterns = [
    path('employees/', views.employees, name='employees'),
    path('employees/details/<int:id>', views.details, name='details'),
    ]