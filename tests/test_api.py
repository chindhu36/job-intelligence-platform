from app import create_app


def test_analyze_job(monkeypatch):
    app = create_app()
    client = app.test_client()

    # Mock the scraper so no external website is contacted
    def mock_scrape_job(url):
        return "<html>Mock job page</html>"

    def mock_extract_job_details(html):
        return {
            "title": "Data Engineer",
            "company": "Scott Logic",
            "location": "Bristol",
            "description": "Python, SQL and data engineering",
            "salary": None,
        }

    # Mock the LLM so no OpenAI API call is made
    def mock_extract_job_profile(job_id, job_description):
        return {
            "job_id": job_id,
            "summary": "A Data Engineer role",
            "seniority": "Senior",
            "technical_skills": ["Python", "SQL"],
            "programming_languages": ["Python"],
            "cloud_platforms": ["AWS"],
            "data_platforms": ["Databricks"],
            "databases": ["PostgreSQL"],
            "bi_tools": ["Power BI"],
            "frameworks": ["PySpark"],
            "engineering_practices": ["CI/CD"],
            "responsibilities": ["Build data pipelines"],
            "requirements": ["Python experience"],
        }

    monkeypatch.setattr(
        "app.routes.jobs.scrape_job",
        mock_scrape_job,
    )
    monkeypatch.setattr(
        "app.routes.jobs.extract_job_details",
        mock_extract_job_details,
    )
    monkeypatch.setattr(
        "app.routes.jobs.extract_job_profile",
        mock_extract_job_profile,
    )

    response = client.post(
        "/api/jobs/analyze",
        json={"job_url": "https://example.com/mock-job"},
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["title"] == "Data Engineer"
    assert data["company"] == "Scott Logic"
    assert data["location"] == "Bristol"
    assert data["profile"]["technical_skills"] == ["Python", "SQL"]