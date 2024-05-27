from django.db import models

# Create your models here.

class Student(models.Model):
  id = models.AutoField(primary_key=True)
  firstName = models.CharField(max_length=100)
  lastName = models.CharField(max_length=100)
  joinDate = models.DateField(auto_now_add=True)
  canton = models.ForeignKey('Canton', on_delete=models.CASCADE)
  company = models.ForeignKey('Company', on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.firstName} {self.lastName}"


class Canton(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class Company(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  canton = models.ForeignKey('Canton', on_delete=models.CASCADE)

  def __str__(self):
    return self.name