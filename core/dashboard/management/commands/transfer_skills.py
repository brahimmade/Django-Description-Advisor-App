from django.core.management.base import BaseCommand
import random
from datetime import datetime
import sqlite3
from dashboard.models import Skill


class Command(BaseCommand):
    help = "inserting job skills data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.con = sqlite3.connect('databases/unique_skills.db')
        self.cur = self.con.cursor()

    def handle(self, *args, **options):
        self.cur.execute('SELECT * FROM skills_name')
        rows = self.cur.fetchall()
        for row in rows:
            if '<' not in str(row[6]):
                Skill.objects.get_or_create(name=str(row[6]))

        print('added skill records')
            