from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    score1 = models.FloatField(default=-1.)
    score2 = models.FloatField(default=-1.)
    date = models.DateTimeField(auto_now=True)
    team = models.CharField(max_length=100)
