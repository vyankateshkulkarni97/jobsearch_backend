import requests
from bs4 import BeautifulSoup
from .base import BaseScraper

class GoogleScraper(BaseScraper):

# In GoogleScraper.scrape method

    def scrape(self, url):
        print(f"Scraping URL: {url}")  # Debug print
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        jobs = []
        for job in soup.select(".gc-card"):
            title = job.select_one("h2").text.strip()
            location = job.select_one(".gc-job-location").text.strip()
            link = "https://careers.google.com" + job.a["href"]

            print(f"Found job: {title} at {location}")  # Debug print

            jobs.append({
                "title": title,
                "location": location,
                "apply_url": link,
                "description": "",
                "skills": []
            })

        return jobs

