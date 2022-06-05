from django import forms 
from .models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class DescriptionForm(forms.ModelForm):
    text = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%','min-width':'600px', 'height': '250px'}}))
    class Meta:
        model = Description
        fields = ['job_title','text']    

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