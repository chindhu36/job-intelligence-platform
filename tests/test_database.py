from app.models.job import Job
from app.services.database import create_tables, save_job


create_tables()

job = Job(
    title="Data Engineer",
    company="Scott Logic",
    location="Bristol",
    description="Python, SQL, Spark and Databricks",
    salary=None,
    source="lever",
    url="https://jobs.lever.co/scottlogic/46628ab4-a3ec-45e7-98a4-921cdd57a3ca"
)

job_id = save_job(job)

print("Saved job ID:", job_id)