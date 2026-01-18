from .models import Company
from .services import save_jobs
from .google import GoogleScraper

SCRAPER_MAP = {
    "google": GoogleScraper,
}

# In your run_company_scraper function

def run_company_scraper(company):
    print(f"Running scraper for company: {company.name}")  # Debug print
    
    scraper_class = SCRAPER_MAP.get(company.scraper_name)
    if not scraper_class:
        print(f"No scraper found for: {company.scraper_name}")
        return

    scraper = scraper_class()
    jobs = scraper.scrape(company.career_url)
    
    print(f"Scraped {len(jobs)} jobs from {company.name}")
    save_jobs(company, jobs)

