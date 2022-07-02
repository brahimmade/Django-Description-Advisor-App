from django.db import models

# Create your models here.

class JobTitle(models.Model):
    name = models.CharField(max_length=250)
    is_core = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    related_skills = models.IntegerField(default=0)
    related_descriptions = models.IntegerField(default=0)
    is_archived = models.BooleanField(default=False)
    is_marked = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created_date',)
class Skill(models.Model):
    name = models.CharField(max_length=200)
    is_core = models.BooleanField(default=True)
    job_title = models.ManyToManyField(JobTitle)
    is_archived = models.BooleanField(default=False)
    is_marked = models.BooleanField(default=False)
    related_job_titles = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_date',)
    # def get_absolute_url(self):
    #     return reverse('dashboard:skill-')

class Description(models.Model):
    job_title = models.ManyToManyField(JobTitle)
    is_core = models.BooleanField(default=True)
    text= models.TextField()
    is_archived = models.BooleanField(default=False)
    is_marked = models.BooleanField(default=False)
    related_job_titles = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_date',)
        
    def __str__(self):
        return f"{self.id} - {self.snippets}"
    
    @property
    def snippets(self):
        return f"{self.text[:20]} ..."