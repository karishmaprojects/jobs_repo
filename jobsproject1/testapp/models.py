from django.db import models

class HydJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=60)
    title=models.CharField(max_length=60)
    eligibility=models.CharField(max_length=60)
    address=models.CharField(max_length=120)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()

class BngJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=60)
    title=models.CharField(max_length=60)
    eligibility=models.CharField(max_length=60)
    address=models.CharField(max_length=120)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()

class PuneJobs(models.Model):
        date=models.DateField()
        company=models.CharField(max_length=60)
        title=models.CharField(max_length=60)
        eligibility=models.CharField(max_length=60)
        address=models.CharField(max_length=120)
        email=models.EmailField()
        phonenumber=models.BigIntegerField()
