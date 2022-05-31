from django.forms import ModelForm
from .models import Description


class DescriptionForm(ModelForm):
    class Meta:
        model = Description
        fields = ['job_title', 'text', 'is_core']    