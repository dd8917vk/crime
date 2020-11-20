from django.urls import path
from . import views
app_name="crimes"
urlpatterns = [
    path('', views.ListDepartments.as_view(), name='list_departments'),
    path('add/', views.NewDepartment.as_view(), name='add_department'),
    path('edit/<int:pk>', views.EditDepartment.as_view(), name='edit_department'),
]