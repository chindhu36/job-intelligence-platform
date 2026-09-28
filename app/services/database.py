import sqlite3
import json

from app.models.job import Job
from app.models.job_profile import JobProfile


DATABASE = "jobs.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT,
            description TEXT,
            salary TEXT,
            source TEXT,
            url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_job(job: Job):
    connection = get_connection()
    cursor = connection.cursor()

    # Check whether this job URL already exists
    cursor.execute(
        "SELECT id FROM jobs WHERE url = ?",
        (job.url,)
    )

    existing_job = cursor.fetchone()

    if existing_job:
        job_id = existing_job[0]
        connection.close()
        return job_id

    # Insert the job only if the URL is new
    cursor.execute("""
        INSERT INTO jobs (
            title,
            company,
            location,
            description,
            salary,
            source,
            url
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        job.title,
        job.company,
        job.location,
        job.description,
        job.salary,
        job.source,
        job.url
    ))

    connection.commit()

    job_id = cursor.lastrowid

    connection.close()

    return job_id


def get_all_jobs():
    connection = get_connection()
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            company,
            location,
            description,
            salary,
            source,
            url,
            created_at
        FROM jobs
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return [dict(row) for row in rows]


def create_job_profiles_table():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job_profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            job_id INTEGER NOT NULL UNIQUE,

            summary TEXT,

            seniority TEXT,

            technical_skills TEXT,

            programming_languages TEXT,

            cloud_platforms TEXT,

            data_platforms TEXT,

            databases TEXT,

            bi_tools TEXT,

            frameworks TEXT,

            engineering_practices TEXT,

            responsibilities TEXT,

            requirements TEXT,

            FOREIGN KEY (job_id) REFERENCES jobs(id)
        )
    """)

    connection.commit()
    connection.close()


def save_job_profile(profile: JobProfile):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO job_profiles (
        job_id,
        summary,
        seniority,
        technical_skills,
        programming_languages,
        cloud_platforms,
        data_platforms,
        databases,
        bi_tools,
        frameworks,
        engineering_practices,
        responsibilities,
        requirements
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(job_id) DO UPDATE SET
        summary = excluded.summary,
        seniority = excluded.seniority,
        technical_skills = excluded.technical_skills,
        programming_languages = excluded.programming_languages,
        cloud_platforms = excluded.cloud_platforms,
        data_platforms = excluded.data_platforms,
        databases = excluded.databases,
        bi_tools = excluded.bi_tools,
        frameworks = excluded.frameworks,
        engineering_practices = excluded.engineering_practices,
        responsibilities = excluded.responsibilities,
        requirements = excluded.requirements
    """, (
        profile.job_id,
        profile.summary,
        profile.seniority,
        json.dumps(profile.technical_skills),
        json.dumps(profile.programming_languages),
        json.dumps(profile.cloud_platforms),
        json.dumps(profile.data_platforms),
        json.dumps(profile.databases),
        json.dumps(profile.bi_tools),
        json.dumps(profile.frameworks),
        json.dumps(profile.engineering_practices),
        json.dumps(profile.responsibilities),
        json.dumps(profile.requirements)
    ))

    connection.commit()

    profile_id = cursor.lastrowid

    connection.close()

    return profile_id

def get_job_by_id(job_id):
    connection = get_connection()
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            j.id,
            j.title,
            j.company,
            j.location,
            j.description,
            j.salary,
            j.source,
            j.url,
            j.created_at,
            p.summary,
            p.seniority,
            p.technical_skills,
            p.programming_languages,
            p.cloud_platforms,
            p.data_platforms,
            p.databases,
            p.bi_tools,
            p.frameworks,
            p.engineering_practices,
            p.responsibilities,
            p.requirements
        FROM jobs j
        LEFT JOIN job_profiles p ON j.id = p.job_id
        WHERE j.id = ?
    """, (job_id,))

    row = cursor.fetchone()
    connection.close()

    return dict(row) if row else None