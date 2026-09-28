from app.services.scraper import scrape_job


url =  "https://jobs.lever.co/scottlogic/46628ab4-a3ec-45e7-98a4-921cdd57a3ca"

html = scrape_job(url)


print(html[:500])