import requests

def fetch_arbeitnow_jobs(query):

    url = "https://arbeitnow.com/api/job-board-api"

    try:
        res = requests.get(url, timeout=10)
        data = res.json()
    except:
        return []

    jobs = []

    for job in data.get("data", []):

        jobs.append({
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("location"),
            "description": " ".join(job.get("tags", [])),  # 🔥 use tags as description
            "url": job.get("url")
        })

    return jobs