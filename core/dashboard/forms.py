from django import forms 
from .models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.core.cache import cache
class DescriptionForm(forms.ModelForm):
    text = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%','min-width':'600px', 'height': '250px'}}))
    class Meta:
        model = Description
        fields = ['job_title','text']    
    
    def __init__(self, *args, **kwargs):
        super(DescriptionForm, self).__init__(*args, **kwargs)
        self.fields['job_title'].queryset = self.get_job_titles()
        
    def get_job_titles(self):
        if cache.get("job_titles_query") is None:
            job_query = JobTitle.objects.filter(is_archived=False)
            cache.set("job_titles_query",job_query,30)
            print('set cache')
        return cache.get("job_titles_query")

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['job_title','name']    
    
    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.fields['job_title'].queryset = self.get_job_titles()
    
    def get_job_titles(self):
        if cache.get("job_titles_query") is None:
            job_query = JobTitle.objects.filter(is_archived=False)
            cache.set("job_titles_query",job_query,30)
            print('set cache')
        return cache.get("job_titles_query")

class SkillArchiveForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['id']

class DescriptionArchiveForm(forms.ModelForm):
    class Meta:
        model = Description
        fields = ['id']
        

class JobTitleArchiveForm(forms.ModelForm):
    class Meta:
        model = JobTitle
        fields = ['id']