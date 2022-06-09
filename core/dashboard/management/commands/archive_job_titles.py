from django.core.management.base import BaseCommand
import random
from datetime import datetime
import sqlite3
from dashboard.models import JobTitle


class Command(BaseCommand):
    help = "inserting job titles data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.job_title_id_list = open('databases/job_titles_id.txt',encoding='utf-8').readlines()


    def handle(self, *args, **options):
        
        for id in self.job_title_id_list:
            if (id.strip()).isdigit():
                try:
                    job_title_obj = JobTitle.objects.get(id=int(id.strip()))
                    job_title_obj.is_archived = True
                    job_title_obj.save()
                    print(job_title_obj.name,' - archived')
                except JobTitle.DoesNotExist:
                    print("this",id,"doesnt exist")
                
            
            
        print('added job title records')
            