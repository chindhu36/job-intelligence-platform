from app.services.scraper import scrape_job, extract_job_details
from app.services.llm_service import (
    extract_job_profile,
    build_job_profile
)


url = "https://jobs.lever.co/scottlogic/46628ab4-a3ec-45e7-98a4-921cdd57a3ca"


html = scrape_job(url)

job_data = extract_job_details(html)


profile_data = extract_job_profile(
    job_id=3,
    job_description=job_data["description"]
)


profile = build_job_profile(
    job_id=3,
    profile_data=profile_data
)


print()
print("JOB PROFILE:")
print(profile)

print()
print("TECHNICAL SKILLS:")
print(profile.technical_skills)

print()
print("PROGRAMMING LANGUAGES:")
print(profile.programming_languages)

print()
print("CLOUD:")
print(profile.cloud_platforms)

print()
print("DATA PLATFORMS:")
print(profile.data_platforms)

print()
print("DATABASES:")
print(profile.databases)

print()
print("BI TOOLS:")
print(profile.bi_tools)

print()
print("FRAMEWORKS:")
print(profile.frameworks)

print()
print("ENGINEERING PRACTICES:")
print(profile.engineering_practices)

print()
print("RESPONSIBILITIES:")
print(profile.responsibilities)

print()
print("REQUIREMENTS:")
print(profile.requirements)