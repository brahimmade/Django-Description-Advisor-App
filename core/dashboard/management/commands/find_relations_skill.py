from django.core.management.base import BaseCommand
import random
from datetime import datetime
import sqlite3
from dashboard.models import Skill,JobTitle


class Command(BaseCommand):
    help = "inserting job skills data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.con = sqlite3.connect('databases/fetched_skills.db')
        self.cur = self.con.cursor()

    def handle(self, *args, **options):
        self.cur.execute('SELECT * FROM job_skill')
        rows = self.cur.fetchall()
        for row in rows:
            if '<' not in str(row[6]):
                # Skill.objects.get_or_create(name=str(row[6]))
                try:
                    job_title_obj = JobTitle.objects.get(name=row[-1])
                    # print(job_title_obj.name,'-',row[6])
                    skill_obj = Skill.objects.get(name=row[6])
                    skill_obj.job_title.add(job_title_obj)
                    skill_obj.save()
                except Skill.DoesNotExist:
                    print(f"didnt found skill - {row[6]}")
                except JobTitle.DoesNotExist:
                    print(f"didnt found skill - {row[-1]}")
            

        print('added skill records')   