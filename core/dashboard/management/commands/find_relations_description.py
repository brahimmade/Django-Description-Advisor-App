from django.core.management.base import BaseCommand
import random
from datetime import datetime
import sqlite3
from dashboard.models import Description,JobTitle


class Command(BaseCommand):
    help = "finding relations for description data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.con = sqlite3.connect('databases/fetched_description.db')
        self.cur = self.con.cursor()

    def handle(self, *args, **options):
        self.cur.execute('SELECT * FROM job_description')
        rows = self.cur.fetchall()
        for row in rows:
            if '<' not in str(row[6]):
                try:
                    job_title_obj = JobTitle.objects.get(name=row[-1])
                    description_obj = Description.objects.get(text =row[6])
                    description_obj.job_title.add(job_title_obj)
                    description_obj.save()
                except JobTitle.DoesNotExist:
                    print(f"job title {row[-1]} doesnt exist ")
                except Description.DoesNotExist:
                    print(f"description {row[6]} doesnt exist")
                except:
                    print('something else happened')
                    
        print('added description related records')   