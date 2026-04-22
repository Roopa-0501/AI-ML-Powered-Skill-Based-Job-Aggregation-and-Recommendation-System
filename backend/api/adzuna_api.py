import requests

APP_ID = "xxxxxxxx"
APP_KEY = "xxxxxxxxxxxxxxxxxxxxx"

def fetch_jobs(query, limit=50):

    url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": query,
        "results_per_page": 50
    }

    try:
        res = requests.get(url, params=params, timeout=8)
        data = res.json()
    except:
        return []

    jobs = []

    for job in data.get("results", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name","N/A"),
            "location": job.get("location", {}).get("display_name","N/A"),
            "description": job.get("description",""),
            "url": job.get("redirect_url")
        })

    return jobs
