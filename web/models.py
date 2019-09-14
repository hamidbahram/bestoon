from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model): #kharj
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
       #__unicode__
    def __str__(self):
        return "{}-{}".format(self.date, self.amount)

class Income(models.Model): #vorodi
    text = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.date, self.amount)