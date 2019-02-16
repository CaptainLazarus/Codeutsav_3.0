from django.db import models
from uuid import uuid4

def generateUUID():
    return str(uuid4())

# Create your models here.
class Startups(models.Model):
    id = models.UUIDField(primary_key=True, default=generateUUID, editable=False)
    name = models.CharField(max_length =100 , unique= True)
    created = models.DateTimeField(auto_now_add=True)
    branch = models.CharField(max_length=100)

class Startupmembers(models.Model):
    name = models.CharField(max_length =100)
    dob = models.DateField()

class Startupprojects(models.Model):
    _id = models.ForeignKey(Startups , on_delete=models.CASCADE,)
    name = models.CharField(max_length =100)
    dob = models.DateTimeField(auto_now_add=True)
    PROGRESS = (
        ('F', 'Finished'),
        ('U', 'Underway'),
        ('N', 'Not yet begun'),
    )
    progress = models.CharField(max_length=1 ,choices=PROGRESS , default = 'N')

class ProgressMilestones(models.Model):
    _id = models.ForeignKey(Startups , on_delete=models.CASCADE,)
    milestone = models.CharField(max_length=300)
    Acheived = models.BooleanField(default=False)

class OfficeSpaces(models.Model):
    address = models.CharField(max_length=300)
    company = models.IntegerField()

class Investors(models.Model):
    id = models.UUIDField(primary_key=True, default=generateUUID, editable=False)
    name = models.CharField(max_length =100)
    dob = models.DateField()

class Invested(models.Model):
    _id = models.ForeignKey(Investors , on_delete=models.CASCADE,)
    startup_invested = models.ForeignKey(Startups , on_delete=models.CASCADE,)


class Mentors(models.Model):
    id = models.UUIDField(primary_key=True, default=generateUUID, editable=False)
    name = models.CharField(max_length =100)
    dob = models.DateField()
