import threading


class SkillCalculationThread(threading.Thread):
    def __init__(self, skill_query):
        self.skill_query = skill_query
        print("skill thread started")
        threading.Thread.__init__(self)

    def run(self):
        for skill_obj in self.skill_query:
            skill_obj.related_job_titles = skill_obj.job_title.all().count()
            skill_obj.save()
        print("skill thread done")


class DescriptionCalculationThread(threading.Thread):
    def __init__(self, description_query):
        self.description_query = description_query
        print("description thread started")
        threading.Thread.__init__(self)

    def run(self):
        for description_obj in self.description_query:
            description_obj.related_job_titles = description_obj.job_title.all().count()
            description_obj.save()
        print("description thread done")
            
class JobCalculationThread(threading.Thread):
    def __init__(self, skill_query,description_query,job_title_query):
        self.skill_query = skill_query
        self.description_query = description_query
        self.job_title_query = job_title_query
        print('job thread started')
        threading.Thread.__init__(self)

    def run(self):
        for job_obj in self.job_title_query:
            job_obj.related_descriptions = self.description_query.filter(
                job_title__in=[job_obj]).count()
            job_obj.related_skills = self.skill_query.filter(
                job_title__in=[job_obj]).count()
            job_obj.save()
        print("job thread done")