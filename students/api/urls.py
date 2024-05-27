from django.urls import path
from . import views

urlpatterns = [
  path('students/', views.StudentListCreate.as_view(), name='student-list-create'),
  path('cantons/', views.CantonListCreate.as_view(), name='canton-list-create'),
  path('companies/', views.CompanyListCreate.as_view(), name='company-list-create'),
]