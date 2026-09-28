from app.services.scraper import scrape_job, extract_job_details
from app.models.job import Job


url = "https://jobs.lever.co/scottlogic/46628ab4-a3ec-45e7-98a4-921cdd57a3ca"

html = scrape_job(url)

job_data = extract_job_details(html)

job = Job(
    title=job_data["title"],
    company=job_data["company"],
    location=job_data["location"],
    description=job_data["description"],
    url=url,
    source="lever"
)

print(job)
print()
print("TITLE:", job.title)
print("COMPANY:", job.company)
print("LOCATION:", job.location)
print("SOURCE:", job.source)