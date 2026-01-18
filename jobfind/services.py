# jobs/services.py
from .models import Job

def save_jobs(company, job_list):
    for j in job_list:
        Job.objects.get_or_create(
            company=company,
            title=j["title"],
            location=j["location"],
            apply_url=j["apply_url"]
        )
