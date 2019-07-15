
import requests

# Get jobs.
get_jobs_url = 'https://angel.co/job_listings/startup_ids'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:49.0) Gecko/20100101 Firefox/49.0',
    'X-CSRF-Token': 'z8O11p9/rrKTl0Yhnb7OjwiDmMpBdhSnoRoOyzJ0BeM6YO+xPe93O9E9vnlLmxwNZUXsUszMlPtoILDL4j14/g==',
    'Cookie': '__cfduid=dcba5ddbe1cd9b1792fef99c3d45be2561555090666; ajs_group_id=null; ext_name=ojplmecpdpgccookcobabopnaifgidhf; intercom-id-og2vxfl5=a63cf7df-5a23-4355-89fe-d49d5d0bc67b; bhInfV_cl_id=O2jf3D0XMxzFvX8KLGCnZjnIzrDQsUgmfDGBGgxyH9JQgiv5qx; __cf_bm=c70c02041506c2e2b610b4b1e096abd93650366a-1555313093-1800-AUhvYetWJHbYya4xJp/rQKpgR0NV56tuvLsIypeQAOeYFn73zLdOIx0pxvlBZ7gnrE8Hr/mIuWR7UKNBeDiz6vY=; visitor_hash=3227dfefd720358ddb652dde383c6efa; ajs_anonymous_id=%22ea43e63b1976369f300ac37dedc3a311%22; _angellist=0204223abde2a0234a4eed0c8c2b2a89; ajs_user_id=%22520277%22',
}
data = {
    'filter_data[roles][]': 'Software Engineer',
    'filter_data[types][]': 'full-time',
    'tab': 'find'
}

jobs = requests.post(get_jobs_url, data=data, headers=headers)
print(jobs)
startups = jobs['ids']
listings = jobs['listing_ids']

apply_url = 'https://angel.co/job_pairings'
erros = []

for startup, listing in zip(startups, listings):
    data = {
        'job_pairing[startup_id]': startup,
        'job_pairing[user_interested]': 1,
        'job_pairing[candidate_processed_listing_ids][]': listings,
        'job_pairing[user_note]': "Having a diversified profile and always excited about learning new technologies, I feel that I'll be the best fit to the organization.Although my profile illustrates my background well, I feel that a personal interview would better demonstrates my knowledge and abilities. Therefore, I would appreciate the opportunities to interview with you at a convenient time.",
        'tab': 'find'
    }
    apply_on_jobs = requests.post(apply_url, data=data, headers=headers)
    # print apply_on_jobs.json()['success']
