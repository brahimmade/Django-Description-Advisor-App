from django.core.management.base import BaseCommand
import random
from datetime import datetime
import sqlite3
from dashboard.models import Description


class Command(BaseCommand):
    help = "inserting job skills data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.con = sqlite3.connect('databases/unique_description.db')
        self.cur = self.con.cursor()

    def handle(self, *args, **options):
        self.cur.execute('SELECT * FROM job_description')
        rows = self.cur.fetchall()
        for row in rows:
            if '<' not in str(row[6]):
                Description.objects.get_or_create(text=str(row[6]))

        print('added description records')