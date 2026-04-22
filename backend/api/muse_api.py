import requests

def fetch_muse_jobs(query):

    url = "https://www.themuse.com/api/public/jobs"
    jobs = []

    try:
        for page in range(1, 4):  # fetch 3 pages

            res = requests.get(url, params={"page": page}, timeout=10)
            data = res.json()

            for job in data.get("results", []):
                jobs.append({
                    "title": job.get("name"),
                    "company": job.get("company", {}).get("name"),
                    "location": job.get("locations")[0]["name"] if job.get("locations") else "N/A",
                    "description": job.get("contents", ""),
                    "url": job.get("refs", {}).get("landing_page")
                })

    except:
        return jobs

    return jobs