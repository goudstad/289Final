from django.test import TestCase
from hist.models import *

class ModelsReprTestCase(TestCase):
	
	# decorator
	@classmethod
	def setUpTestData(cls):
		cls.employee1 = Employee.objects.create(lname='Beck', fname='Tony' )

	def testEmployeeRepr(self):
		self.assertEqual(repr(self.employee1), '<Employee 1: Tony Beck>')

