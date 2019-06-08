from django.test import TestCase
from hist.models import *
from datetime import date
from hist.forms import * # import all forms

class ModelsReprTestCase(TestCase):
    
    # decorator
    @classmethod
    def setUpTestData(cls):
        cls.employee1 = Employee.objects.create(lname='Beck', fname='Tony')
        cls.decision1 = Decision.objects.create(title='Decision Test', decisionDesc='This is a test of the decision description field.')
        cls.employee2 = Employee.objects.create(lname='Love', fname='Annie')
        cls.decision1.decisionMaker.add(cls.employee1)
        cls.decision1.decisionMaker.add(cls.employee2)
        cls.decision1.DateLastUpdate = date.today()
    
    def testEmployeeRepr(self):
        self.assertEqual(repr(self.employee1), '<Employee 1: Tony Beck>')

    def testDecisionRepr(self):
        self.assertEqual(repr(self.decision1), '<Decision 1: Decision Test - This is a test of the decision description field.>')

# testing chinese characters
   # def testEmployeeRepr(self):
   #     self.assertEqual(repr(self.employee2), '<Employee 2: 测验 黄>')
   #     print (repr(self.employee2))

    def test_decision_employee(self):
        self.assertEqual(str(self.decision1.decisionMaker.all()), 
            '<QuerySet [<Employee 1: Tony Beck>, <Employee 2: Annie Love>]>')

    def test_DateLastUpdate(self):
        self.assertEqual(self.decision1.DateLastUpdate, date.today())

class ContactFormTest(TestCase):
    def test_form(self):
        form = fm_contact()
        self.assertTrue(form.fields['subject'].label == None or form.fields['subject'].label == 'subject')