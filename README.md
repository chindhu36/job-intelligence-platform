# Job Intelligence Platform

A Python-based job intelligence platform that ingests job postings, extracts structured job requirements using an LLM, and stores the resulting data for further analysis and job-to-CV matching.

## Overview

The goal of this project is to build an end-to-end platform for analysing job opportunities and understanding how well a candidate's skills align with a role.

The platform combines:

- Python and Flask REST APIs
- Job data ingestion and extraction
- Data cleaning and structuring
- SQLite data storage
- LLM-based job profile extraction
- Automated testing

The project is being developed incrementally, with future stages focused on CV analysis, job-to-CV matching, skill-gap analysis, and data engineering pipelines.

## Current Features

### Job ingestion

The API accepts a job URL and retrieves the permitted job posting content.

### Job data extraction

The platform extracts information such as:

- Job title
- Company
- Location
- Job description

### LLM-based job profiling

The job description is processed by an LLM to extract structured information including:

- Seniority
- Technical skills
- Programming languages
- Cloud platforms
- Data platforms
- Databases
- BI tools
- Frameworks
- Engineering practices
- Responsibilities
- Requirements

### Data storage

Job postings and structured job profiles are stored in SQLite.

### REST API

The application exposes Flask REST endpoints for analysing and retrieving job data.

## Architecture

```text
                 Job URL
                    |
                    v
             Flask REST API
                    |
                    v
              Job Scraper
                    |
                    v
          Data Extraction/Cleaning
                    |
                    v
                 SQLite
                    |
                    v
             LLM Job Profiling
                    |
                    v
          Structured Job Profile
```

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | REST API |
| Requests | HTTP requests |
| BeautifulSoup | HTML parsing |
| SQLite | Data storage |
| OpenAI API | Job profile extraction |
| Pytest | Automated testing |
| Git/GitHub | Version control |

## Project Structure

```text
job-intelligence-platform/
|
+-- app/
|   +-- models/
|   |   +-- cv_profile.py
|   |   +-- job.py
|   |   +-- job_profile.py
|   |
|   +-- routes/
|   |   +-- cv.py
|   |   +-- jobs.py
|   |
|   +-- services/
|       +-- cv_parser.py
|       +-- database.py
|       +-- llm_service.py
|       +-- scraper.py
|
+-- tests/
|   +-- test_api.py
|   +-- test_config.py
|   +-- test_cv_parser.py
|   +-- test_database.py
|   +-- test_extraction.py
|   +-- test_job_profile.py
|   +-- test_llm_extraction.py
|   +-- test_scraper.py
|
+-- .gitignore
+-- requirements.txt
+-- run.py
+-- README.md
```

## API

### Analyse a job

```http
POST /api/jobs/analyze
```

Request:

```json
{
  "job_url": "https://example.com/job"
}
```

The API retrieves the job posting, extracts job information, creates a structured job profile, and stores the data.

### Retrieve jobs

```http
GET /api/jobs
```

Returns previously analysed job postings.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/chindhu36/job-intelligence-platform.git
cd job-intelligence-platform
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

Do not commit `.env` to GitHub.

### 6. Run the API

```bash
python run.py
```

The API will run locally on:

```text
http://127.0.0.1:5000
```

## Testing

Run the test suite with:

```bash
pytest
```

## Current Status

**MVP - In Development**

The current version supports job ingestion, structured job extraction, LLM-based job profiling, and database persistence.

## Roadmap

### Phase 1 - Job Intelligence MVP

- [x] Job ingestion
- [x] Job data extraction
- [x] SQLite persistence
- [x] LLM-based job profiling
- [x] Automated tests

### Phase 2 - Candidate Intelligence

- [ ] CV parsing
- [ ] Structured CV profile
- [ ] CV-to-job matching
- [ ] Skill gap analysis
- [ ] Match scoring

### Phase 3 - Data Engineering Pipeline

- [ ] Bronze/Silver/Gold data architecture
- [ ] PySpark processing
- [ ] Databricks integration
- [ ] Data quality checks
- [ ] Analytics layer

### Phase 4 - Analytics

- [ ] Job market analytics
- [ ] Skills demand analysis
- [ ] Salary analysis
- [ ] Power BI dashboard

## Disclaimer

Job data ingestion should only be performed against sources where automated access is permitted. The project should respect website terms of service, robots.txt requirements, rate limits, website terms of service, and applicable laws.
