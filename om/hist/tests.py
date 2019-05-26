from django.test import TestCase
from hist.models import *
from datetime import date

class ModelsReprTestCase(TestCase):
    
    # decorator
    @classmethod
    def setUpTestData(cls):
        cls.employee1 = Employee.objects.create(lname='Beck', fname='Tony')
        cls.decision1 = Decision.objects.create(title='Decision Test', decisionDesc='This is a test of the decision description field.')
        cls.employee2 = Employee.objects.create(lname='黄', fname='测验')
    
    def testEmployeeRepr(self):
        self.assertEqual(repr(self.employee1), '<Employee 1: Tony Beck>')

    def testDecisionRepr(self):
        self.assertEqual(repr(self.decision1), '<Decision 1: Decision Test - This is a test of the decision description field.>')

# testing chinese characters
    def testEmployeeRepr(self):
        self.assertEqual(repr(self.employee2), '<Employee 2: 测验 黄>')
        print (repr(self.employee2))
