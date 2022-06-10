from django.core.management.base import BaseCommand
import random
from datetime import datetime
import sqlite3
from dashboard.models import JobTitle


class Command(BaseCommand):
    help = "inserting job titles data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)


    def handle(self, *args, **options):
        job_titles = JobTitle.objects.filter(is_archived=False,name__contains='job')
        string_name = ["job titles","Jobs"]
        for job in job_titles:
            for name in string_name:
                if name in job.name:
                    job.name = (job.name).replace(name,"")
                    print((job.name).replace(name,""))
                    
            job.save()
        
            