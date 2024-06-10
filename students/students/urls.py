from django.urls import path
from . import views

urlpatterns = [
  path('students/', views.StudentListCreate.as_view(), name='student-list-create'),
  path('students/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view(), name='student-retrieve-update-destroy'),
  path('cantons/', views.CantonListCreate.as_view(), name='canton-list-create'),
  path('cantons/<int:pk>/', views.CantonRetrieveUpdateDestroy.as_view(), name='canton-retrieve-update-destroy'),
  path('companies/', views.CompanyListCreate.as_view(), name='company-list-create'),
  path('companies/<int:pk>/', views.CompanyRetrieveUpdateDestroy.as_view(), name='company-retrieve-update-destroy'),
]