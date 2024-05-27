from django.shortcuts import render
from rest_framework import generics
from .models import Student, Canton, Company
from .serializers import StudentSerializer, CantonSerializer, CompanySerializer

class StudentListCreate(generics.ListCreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class CantonListCreate(generics.ListCreateAPIView):
  queryset = Canton.objects.all()
  serializer_class = CantonSerializer


class CompanyListCreate(generics.ListCreateAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer