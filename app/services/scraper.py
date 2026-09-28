import requests
from bs4 import BeautifulSoup


def scrape_job(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return response.text

    except requests.exceptions.RequestException as e:
        raise Exception(f"Unable to fetch job page: {e}")


def extract_job_details(html):
    soup = BeautifulSoup(html, "html.parser")

    # Job title
    title = soup.find("h2")

    # Location
    location = None

    categories = soup.select(".posting-categories .sort-by-time")

    for category in categories:
        text = category.get_text(" ", strip=True)

        if "Bristol" in text:
            location = text
            break

    if not location:
        page_text = soup.get_text(" ", strip=True)

        if "Bristol" in page_text:
            location = "Bristol"

    # Complete job description
    description_parts = []

    for section in soup.select(".section"):
        section_text = section.get_text(" ", strip=True)

        if not section_text:
            continue

        # Stop before the benefits section
        if "What you’ll get in return is" in section_text:
            break

        description_parts.append(section_text)

    description = " ".join(description_parts)

    return {
        "title": title.get_text(" ", strip=True) if title else None,
        "company": "Scott Logic",
        "location": location,
        "description": description
    }