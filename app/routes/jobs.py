from flask import Blueprint, request, jsonify
import json

from app.services.scraper import scrape_job, extract_job_details
from app.models.job import Job
from app.services.database import (
    create_tables,
    save_job,
    get_all_jobs,
    create_job_profiles_table,
    save_job_profile,
    get_job_by_id
)
from app.services.llm_service import (
    extract_job_profile,
    build_job_profile
)

jobs_bp = Blueprint("jobs", __name__)


@jobs_bp.route("/analyze", methods=["POST"])
def analyze_job():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    job_url = data.get("job_url")

    if not job_url:
        return jsonify({
            "error": "job_url is required"
        }), 400

    try:
        # 1. Scrape the job page
        html = scrape_job(job_url)

        # 2. Extract job details
        job_data = extract_job_details(html)

        # 3. Create Job object
        job = Job(
            title=job_data["title"],
            company=job_data["company"],
            location=job_data["location"],
            description=job_data["description"],
            salary=job_data.get("salary"),
            source="lever",
            url=job_url
        )

        # 4. Ensure database tables exist
        create_tables()
        create_job_profiles_table()

        # 5. Save the job
        job_id = save_job(job)

        # 6. Extract structured information using the LLM
        profile_data = extract_job_profile(
            job_id=job_id,
            job_description=job.description
        )

        # 7. Build the JobProfile object
        profile = build_job_profile(
            job_id=job_id,
            profile_data=profile_data
        )

        # 8. Save the profile
        save_job_profile(profile)

        # 9. Return job details and profile
        return jsonify({
            "id": job_id,
            "title": job.title,
            "company": job.company,
            "location": job.location,
            "salary": job.salary,
            "source": job.source,
            "url": job.url,
            "description": job.description,
            "profile": {
                "summary": profile.summary,
                "seniority": profile.seniority,
                "technical_skills": profile.technical_skills,
                "programming_languages": profile.programming_languages,
                "cloud_platforms": profile.cloud_platforms,
                "data_platforms": profile.data_platforms,
                "databases": profile.databases,
                "bi_tools": profile.bi_tools,
                "frameworks": profile.frameworks,
                "engineering_practices": profile.engineering_practices,
                "responsibilities": profile.responsibilities,
                "requirements": profile.requirements
            }
        }), 200

    except Exception as e:

        return jsonify({
            "error": "Unable to analyze job",
            "details": str(e)
        }), 502



@jobs_bp.route("", methods=["GET"])
def get_jobs():

    try:
        jobs = get_all_jobs()

        return jsonify(jobs), 200

    except Exception as e:

        return jsonify({
            "error": "Unable to retrieve jobs",
            "details": str(e)
        }), 500


@jobs_bp.route("/<int:job_id>", methods=["GET"])
def get_job(job_id):
    job = get_job_by_id(job_id)

    if job is None:
        return jsonify({"error": "Job not found"}), 404

    # Convert JSON strings stored in the database back into lists
    list_fields = [
        "technical_skills",
        "programming_languages",
        "cloud_platforms",
        "data_platforms",
        "databases",
        "bi_tools",
        "frameworks",
        "engineering_practices",
        "responsibilities",
        "requirements"
    ]

    for field in list_fields:
        if job.get(field):
            job[field] = json.loads(job[field])
        else:
            job[field] = []

    return jsonify(job), 200