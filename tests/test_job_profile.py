from app.models.job_profile import JobProfile

from app.services.database import (
    create_tables,
    create_job_profiles_table,
    save_job_profile
)


create_tables()
create_job_profiles_table()


profile = JobProfile(
    job_id=3,

    summary="Senior / Lead Data Engineer",

    seniority="Senior / Lead",

    technical_skills=[
        "Data engineering",
        "Data pipelines",
        "Data modelling"
    ],

    programming_languages=[
        "Python",
        "SQL"
    ],

    cloud_platforms=[
        "AWS",
        "Azure"
    ],

    data_platforms=[
        "Databricks"
    ],

    databases=[
        "Snowflake"
    ],

    bi_tools=[
        "Power BI"
    ],

    frameworks=[
        "Spark",
        "PySpark"
    ],

    engineering_practices=[
        "Agile",
        "CI/CD"
    ],

    responsibilities=[
        "Build data platforms",
        "Develop data pipelines"
    ],

    requirements=[
        "Experience with Python",
        "Experience with SQL"
    ]
)


profile_id = save_job_profile(profile)


print("Saved profile ID:", profile_id)

print()
print("Job ID:", profile.job_id)
print("Summary:", profile.summary)
print("Seniority:", profile.seniority)
print("Technical skills:", profile.technical_skills)
print("Programming languages:", profile.programming_languages)
print("Cloud platforms:", profile.cloud_platforms)
print("Data platforms:", profile.data_platforms)
print("Databases:", profile.databases)
print("BI tools:", profile.bi_tools)
print("Frameworks:", profile.frameworks)
print("Engineering practices:", profile.engineering_practices)
print("Responsibilities:", profile.responsibilities)
print("Requirements:", profile.requirements)