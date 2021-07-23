from django.db import models


class Employee(models.Model):
    eno = models.CharField(max_length=100)
    ename = models.CharField(max_length=100)
    emobile = models.CharField(max_length=100)
    esal = models.CharField(max_length=100)

    def __str__(self):
        return self.eno