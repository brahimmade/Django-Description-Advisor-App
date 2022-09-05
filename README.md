# Django-Description-Advisor-App
 this is a sample app for creating and managing the current descriptions


removing old database sessions 
python manage.py shell
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()