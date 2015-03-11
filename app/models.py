from django.db import models


class Recruitment(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    mail = models.EmailField(max_length=256, null=False, blank=False)


class Skills(models.Model):
    name = models.CharField(max_length=10)
    value = models.IntegerField()
    recruitment = models.ForeignKey(Recruitment)