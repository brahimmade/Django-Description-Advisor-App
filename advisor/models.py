from django.db import models

# Create your models here.

class JobTitle(models.Model):
    name = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Skill(models.Model):
    name = models.CharField(max_length=200)
    job_title = models.ManyToManyField(JobTitle)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Description(models.Model):
    job_title = models.ManyToManyField(JobTitle)
    is_core = models.BooleanField(default=True)
    text= models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_date',)
        
    def __str__(self):
        return f"{self.id} - {self.snippets}"
    
    @property
    def snippets(self):
        return self.text[:20] + "..."