# jobs/models.py
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    career_url = models.URLField()
    scraper_name = models.CharField(max_length=100)  


    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    apply_url = models.URLField()
    description = models.TextField(blank=True)
    posted_date = models.CharField(max_length=100, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.company.name}"

