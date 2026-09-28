import os
import json

from dotenv import load_dotenv
from openai import OpenAI
from app.models.job_profile import JobProfile


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def extract_job_profile(job_id, job_description):

    response = client.responses.create(
        model="gpt-5.4-nano",

        instructions="""
You are a job description analysis system.

Extract information only from the supplied job description.

Classification rules:

technical_skills:
- Data engineering concepts and technical capabilities.
- Examples: ETL, data modelling, data pipelines, data integration, system design.
- Do not put programming languages, cloud platforms, databases, BI tools, or engineering practices here.

programming_languages:
- Programming or query languages explicitly mentioned.
- Examples: Python, JavaScript, SQL.

cloud_platforms:
- Cloud providers only.
- Examples: AWS, Azure, GCP.

data_platforms:
- Data platforms and data engineering products.
- Examples: Databricks, Snowflake.
- If a product is clearly a database, prefer the databases category.

databases:
- Database technologies explicitly mentioned.
- Do not include generic concepts such as "data warehouse" or "data lake".

bi_tools:
- Business intelligence and reporting products.
- Example: Power BI.

frameworks:
- Software/data frameworks explicitly mentioned.
- Examples: Spark, PySpark.

engineering_practices:
- Engineering methodologies, delivery practices, or development practices.
- Examples: CI/CD, Agile.

Do not invent technologies.
Only include technologies or practices supported by the job description.

Keep each item concise and standardised.

If information is not present, return an empty list or null.

Seniority should be concise, such as:
Junior, Mid-level, Senior, Lead, or Senior / Lead.
""",

        input=f"""
Analyse this job description:

{job_description}
""",

        text={
            "format": {
                "type": "json_schema",
                "name": "job_profile",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "summary": {
                            "type": ["string", "null"]
                        },
                        "seniority": { 
                            "type": ["string", "null"]
                        },
                        "technical_skills": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "programming_languages": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "cloud_platforms": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "data_platforms": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "databases": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "bi_tools": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "frameworks": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "engineering_practices": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "responsibilities": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "requirements": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "required": [
                        "summary",
                        "seniority",
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
                    ],
                    "additionalProperties": False
                }
            }
        }
    )

    return json.loads(response.output_text)


def build_job_profile(job_id, profile_data):

    return JobProfile(
        job_id=job_id,
        summary=profile_data.get("summary"),
        seniority=profile_data.get("seniority"),

        technical_skills=profile_data.get(
            "technical_skills", []
        ),

        programming_languages=profile_data.get(
            "programming_languages", []
        ),

        cloud_platforms=profile_data.get(
            "cloud_platforms", []
        ),

        data_platforms=profile_data.get(
            "data_platforms", []
        ),

        databases=profile_data.get(
            "databases", []
        ),

        bi_tools=profile_data.get(
            "bi_tools", []
        ),

        frameworks=profile_data.get(
            "frameworks", []
        ),

        engineering_practices=profile_data.get(
            "engineering_practices", []
        ),

        responsibilities=profile_data.get(
            "responsibilities", []
        ),

        requirements=profile_data.get(
            "requirements", []
        )
    )