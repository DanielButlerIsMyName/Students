from django.test import TestCase
from django.core.validators import EmailValidator
from .models import Canton, Company, Student

class CantonModelTest(TestCase):
    def setUp(self):
        self.canton = Canton.objects.create(name='Test Canton')

    def test_canton_str(self):
        self.assertEqual(str(self.canton), 'Test Canton')

class CompanyModelTest(TestCase):
    def setUp(self):
        self.canton = Canton.objects.create(name='Test Canton')
        self.company = Company.objects.create(name='Test Company', canton=self.canton)

    def test_company_str(self):
        self.assertEqual(str(self.company), 'Test Company')

    def test_company_has_canton(self):
        self.assertEqual(self.company.canton, self.canton)

    def test_company_name_max_length(self):
        max_length = self.company._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)
    
class StudentModelTest(TestCase):
    def setUp(self):
        self.canton = Canton.objects.create(name='Test Canton')
        self.company = Company.objects.create(name='Test Company', canton=self.canton)
        self.student = Student.objects.create(firstName='John', lastName='Doe', email='johndoe@example.com', canton=self.canton, company=self.company)
    
    def test_student_str(self):
        self.assertEqual(str(self.student), 'John Doe')
    
    def test_student_has_canton(self):
        self.assertEqual(self.student.canton, self.canton)
    
    def test_student_has_company(self):
        self.assertEqual(self.student.company, self.company)
    
    def test_student_first_name_max_length(self):
        max_length = self.student._meta.get_field('firstName').max_length
        self.assertEqual(max_length, 100)
    
    def test_student_last_name_max_length(self):
        max_length = self.student._meta.get_field('lastName').max_length
        self.assertEqual(max_length, 100)
    
    def test_student_email_valid(self):
        email_validator = EmailValidator()
        try:
            email_validator(self.student.email)
        except ValidationError:
            self.fail("Email validation failed")