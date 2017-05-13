from django.db import models

from newsongy.models import Person


class Pray(models.Model):

    pray_dt = models.DateField()

    class Meta:
        db_table = 'pray'


class Attendance(models.Model):

    person = models.ForeignKey(Person)
    pray = models.ForeignKey(Pray)
    joined_morning = models.BooleanField(default=False)
    joined_afternoon = models.BooleanField(default=False)

    class Meta:
        db_table = 'attendance'


