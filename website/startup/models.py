from django.db import models

class Team(models.Model):
    I = "I"
    M = "M"
    Name =  models.CharField(max_length=100)
    Biodata = models.CharField(max_length = 100)
    Contact = models.CharField(max_length = 10,unique=True)
    Social = models.CharField(max_length = 100)
    Type_Choices = (
        (I , 'Investor'),
        (M , 'Mentor'),
    )
    Type = models.CharField(
        max_length=2,
        choices=Type_Choices,
        default=I
    ),
# Create your models here.