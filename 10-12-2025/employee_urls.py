from django.urls import path
from.import views

urlpatterns = [
    path('employees/',views.get_employees),
    path('employees/update/<int:id>/', views.update_employee),
    path('employees/delete/<int:id>/', views.delete_employee),
]
