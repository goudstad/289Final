# Adopted from class lecture 2 lecture notes

import csv

from django.core.management.base import BaseCommand, CommandError
from hist.models import Decision, Employee

file_decisions_CSV = '../data/decisions_data2.csv' # go to root?
file_employees_CSV = '../data/employee_data2.csv'

class Command(BaseCommand):

    help = "Imports a CSV of decision data"

    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs='?', type=str, default=file_decisions_CSV)

    def handle(self, *args, **options):
        with open(options['csv_path'], 'r', encoding='UTF8') as data_file:
            reader = csv.DictReader(data_file)
            for row in reader:
                try:
                    #employee = self.get_or_create_employee(row)
                    decision = self.get_or_create_decision(row)
                except Exception as e:
                    raise

    def get_or_create_employee(self, row):
        print(row)
        employee, created = Employee.objects.get_or_create(
            fname=row['fname'],
            lname=row['lname'],
            position=row['position'])
        return employee
# import data
# left hand side are the fields in the database; the right side are the fields in the spreadsheet.
    def get_or_create_decision(self, row):
        decision, created = Decision.objects.get_or_create(
            enteredby.add(row['enteredby']),
            title=row['title'],
            decisionDate=row['decisionDate'],
            decisionDesc=row['decisionDesc'],
            backgroundInfo=row['backgroundInfo'],
            rationale=row['rationale'],
            subject=row['subject'],
            impact=row['impact'],
            lessonLrnd=row['lessonLrnd'],
            decisionStatus=row['decisionStatus'],
            decisionMaker=row['decisionMaker']
            )
        return decision


