from django.db import models
# get page location
from django.urls import reverse

# Create your models here.
class Decision (models.Model):
    STATUS = (
        ('1', 'In-progress'),
        ('2', 'Completed'),
        ('3', 'Archived')
        )
    title = models.CharField(max_length=256, blank=True)
    decisionDesc = models.TextField(blank=True)
    decisionDate = models.DateField(auto_now_add=True)
    backgroundInfo = models.TextField(blank=True)
    rationale = models.TextField(blank = True)
    subject = models.CharField(max_length=256, blank=True)
    impact = models.TextField(blank = True)
    lessonLrnd = models.TextField(blank=True)
    decisionStatus = models.CharField(max_length=1, choices=STATUS, default='1')

    # define one-to-many relationship
    # decisionMaker = models.ForeignKey('Employee', on_delete=models.CASCADE, blank=True, null=True)
    # Changed to many-to-many relationship.  A decision can be made by multiple employees. An employee can make multiple dcisions.
    # Added related_name to disambiguate accessor name
    decisionMaker = models.ManyToManyField('Employee', related_name="decisionMaker" )
    enteredby = models.ManyToManyField('Employee', related_name="enteredby")
    
    # override default print command
    def __repr__(self):
        return '<Decision {}: {} - {}>'.format(self.id,self.title, self.decisionDesc)

    def __str__(self):
        return repr(self)

    def get_absolute_url(self):
        return reverse('hist-detail', kwargs={'pk':self.pk})

class Employee(models.Model):
    fname = models.CharField(max_length=256)
    lname = models.CharField(max_length=256)
    position = models.CharField(max_length=256)

    def __repr__(self):
        return '<Employee {}: {} {}>'.format(self.id,self.fname,self.lname)

    def __str__(self):
        return repr(self)

    def get_absolute_url(self):
        return reverse('employee-detail', kwargs={'pk':self.pk})