from django.db import models

# Create your models here.
class Decision (models.Model):
    title = models.CharField(max_length=256, blank=True)
    decisions = models.TextField(blank=True)
    decisionDate = models.DateField(auto_now_add=True)
    backgroundInfo = models.TextField(blank=True)
    rationale = models.TextField(blank = True)
    subject = models.CharField(max_length=256, blank=True)
    # define one-to-many relationship
    decisionMaker = models.ForeignKey('Employee', on_delete=models.CASCADE, blank=True, null=True)
    
    # override default print command
    def __repr__(self):
    	return '<Decision {}: {}>'.format(self.id,self.title)


class Employee(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)

    # override default print command
    def __repr__(self):
    	return '<Employee {}: {} {}>'.format(self.id, self.first_name, self.last_name)


