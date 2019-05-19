# Adopted from class lecture 2 lecture notes

import csv

from django.core.management.base import BaseCommand, CommandError
from hist.models import Decision, Employee

file_decisions_CSV = '../data/decisions_data.csv' # go to root?
file_employees_CSV = '../data/employee_data.csv'

class Command(BaseCommand):

    help = "Imports a CSV of decision data"

    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs='?', type=str, default=file_employees_CSV)

    def handle(self, *args, **options):
        with open(options['csv_path'], 'r') as data_file:
            reader = csv.DictReader(data_file)
            for row in reader:
                try:
                    employee = self.get_or_create_employee(row)
                    # decision = self.get_or_create_decision(employee, row)
                except Exception as e:
                    raise

    def get_or_create_employee(self, row):
        employee, created = Employee.objects.get_or_create(
            fname=row['fname'],
            lname=row['lname'],
            position=row['position'])
        return employee

    def get_or_create_decision(self, employee, row):
        decision, created = Decision.objects.get_or_create(
            enteredby=employee,
            decisionTitle=row['title'],
            decisionDate=row['decisionDate'],
            decisionDescription=row['decisionDesc'],
            decisionBackground=row['backgroundInfo'],
            decisionRationale=row['rationale'],
            decisionSubject=row['subject'],
            decisionImpact=row['impact'],
            decisonLessonLearned=row['lessonLrnd'],
            decisionStatus=row['decisionStatus'],
            decisionMaker=row['decisionMaker']
            )
        return decision


