from django.db import models

# Create your models here.
class Decision (models.Model):
    title = models.CharField(max_length=256, blank=True)
    decisions = models.TextField(blank=True)
    decisionDate = models.DateField(auto_now_add=True)
    backgroundInfo = models.TextField(blank=True)
    rationale = models.TextField(blank = True)
    subject = models.CharField(max_length=256, blank=True)
    decisionMaker = models.ForeignKey('Employee', on_delete=models.CASCADE, blank=True, null=True)

class Employee(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)


