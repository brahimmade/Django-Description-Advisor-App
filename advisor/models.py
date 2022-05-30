from django.db import models

# Create your models here.

class JobTitle(models.Model):
    name = models.CharField(max_length=250)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

class Skill(models.Model):
    name = models.CharField(max_length=200)
    job_title = models.ManyToManyField(JobTitle)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Description(models.Model):
    job_title = models.ManyToManyField(JobTitle)
    is_core = models.BooleanField(default=True)
    text= models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    