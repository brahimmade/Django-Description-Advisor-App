from django.contrib import admin
from .models import Description,Skill,JobTitle

# Register your models here.
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id','name','get_titles']
    
    def get_titles(self,obj):
        return ",".join([p.name for p in obj.job_title.all()])
        
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['id','text','get_titles']
    
    def get_titles(self,obj):
        return ",".join([p.name for p in obj.job_title.all()])
        

admin.site.register(Description,DescriptionAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(JobTitle,JobTitleAdmin)