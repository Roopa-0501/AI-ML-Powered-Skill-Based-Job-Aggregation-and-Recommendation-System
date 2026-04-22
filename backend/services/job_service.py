# from services.cache import get_cache, set_cache
# from api.job_api import fetch_jobs
# import json

# def load_local_jobs():
#     try:
#         with open("data/jobs_sample.json") as f:
#             return json.load(f)
#     except:
#         return []

# def get_jobs(query):
#     cached = get_cache(query)
#     if cached:
#         return cached

# # 2. Fetch from API
#     jobs = fetch_jobs(query, limit=50)

# # 3. Fallback if API fails
#     if not jobs:
#         jobs = load_local_jobs()

# # 4. Store cache
#     set_cache(query, jobs)

#     return jobs

from api.adzuna_api import fetch_jobs as fetch_adzuna_jobs
from api.muse_api import fetch_muse_jobs
from api.arbeitnow_api import fetch_arbeitnow_jobs

def remove_duplicates(jobs):

    seen = set()
    unique_jobs = []

    for job in jobs:
        key = (job["title"], job["company"])

        if key not in seen:
            seen.add(key)
            unique_jobs.append(job)

    return unique_jobs


def get_jobs(query):

    jobs = []

    try:
        jobs += fetch_adzuna_jobs(query)
    except:
        print("Adzuna failed")

    try:
        jobs += fetch_muse_jobs(query)
    except:
        print("Muse failed")

    try:
        jobs += fetch_arbeitnow_jobs(query)
    except:
        print("Arbeitnow failed")

    return remove_duplicates(jobs)

