
import requests

# Get jobs.
get_jobs_url = 'https://angel.co/job_listings/startup_ids'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:49.0) Gecko/20100101 Firefox/49.0',
    'X-CSRF-Token': 'YOUR_CSRF_TOKEN',
    'Cookie': 'YOUR_COOKIE',
}
data = {
    'filter_data[roles][]': 'Software Engineer',
    'filter_data[salary][max]': 200,
    'filter_data[salary][min]': 25,
    'filter_data[types][]': 'full-time',
    'tab': 'find'
}

jobs = requests.post(get_jobs_url, data=data, headers=headers).json()
startups = jobs['ids']
listings = jobs['listing_ids']

apply_url = 'https://angel.co/job_pairings'
erros = []

for startup, listing in zip(startups, listings):
    data = {
        'job_pairing[startup_id]': startup,
        'job_pairing[user_interested]': 1,
        'job_pairing[candidate_processed_listing_ids][]': listings,
        'job_pairing[user_note]': "YOUR_MESSAGE",
        'tab': 'find'
    }
    apply_on_jobs = requests.post(apply_url, data=data, headers=headers)
    print apply_on_jobs.json()['success']
