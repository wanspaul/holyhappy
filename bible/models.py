from django.db import models

from newsongy.models import Person


class Bible(models.Model):

    person = models.ForeignKey(Person)
    title = models.CharField(max_length=50)
    read = models.BooleanField(default=False)
    day = models.CharField(max_length=10)
    memo = models.TextField()

    class Meta:
        db_table = 'bible'

