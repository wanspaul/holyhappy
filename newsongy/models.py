from django.db import models


class Person(models.Model):

    DEPARTMENT = (('U', '대학부'),('Y', '청년부'))
    name = models.CharField(max_length=50)
    dept = models.CharField(choices=DEPARTMENT, max_length=1)
    group = models.CharField(max_length=3)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'person'


