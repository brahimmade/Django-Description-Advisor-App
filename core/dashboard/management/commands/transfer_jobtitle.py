from django.core.management.base import BaseCommand
import random
from datetime import datetime
import sqlite3
from dashboard.models import JobTitle


class Command(BaseCommand):
    help = "inserting job titles data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.con = sqlite3.connect('databases/fetched_jobs_title.db')
        self.cur = self.con.cursor()

    def handle(self, *args, **options):
        self.cur.execute('SELECT * FROM job_titles')
        rows = self.cur.fetchall()
        for row in rows:
            JobTitle.objects.get_or_create(name=(str(row[1])).replace('\n',''))
            
        print('added job title records')
            