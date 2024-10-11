from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee_list'),
    path('<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('add/', views.EmployeeCreateView.as_view(), name='employee_add'),
    path('add/file/', views.upload_file, name='employee_upload'),
    path('update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='employee_delete'),

]
