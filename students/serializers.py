from rest_framework import serializers
from .models import Student, Canton, Company

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = '__all__'


class CantonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Canton
    fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = '__all__'