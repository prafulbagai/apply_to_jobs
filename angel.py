
import requests

# Get jobs.
get_jobs_url = 'https://angel.co/job_listings/startup_ids'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:49.0) Gecko/20100101 Firefox/49.0',
    'X-CSRF-Token': 'Vueu2m8NCwywNBkp+EOUGIin3E8PBMoPP+wWpKIeGHkLWIaASEyUUcWciTEvTty3OoC4mm0xhKJb0Fr8d61TRw==',
    'Cookie': '_angellist=0ba9f735ed33c0440267ce78c37337b2; _ga=GA1.2.12242733.1502734621; _gid=GA1.2.1031921909.1502734621; ajs_user_id=%22520277%22; ajs_group_id=null; ajs_anonymous_id=%222a9878204be17c729d0a8b037568c396%22; amplitude_idangel.co=eyJkZXZpY2VJZCI6IjIzNTg0OGUyLWZjZjItNDE3NC05ZmRjLTJhMTkxZjllYTRjNlIiLCJ1c2VySWQiOiI1MjAyNzciLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE1MDI3ODUwNzIxMzIsImxhc3RFdmVudFRpbWUiOjE1MDI3ODU1MDk5MzIsImV2ZW50SWQiOjYsImlkZW50aWZ5SWQiOjEwLCJzZXF1ZW5jZU51bWJlciI6MTZ9',
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
        'job_pairing[user_note]': "Having a diversified profile and always excited about learning new technologies, I feel that I'll be the best fit to the organization.Although my profile illustrates my background well, I feel that a personal interview would better demonstrates my knowledge and abilities. Therefore, I would appreciate the opportunities to interview with you at a convenient time.",
        'tab': 'find'
    }
    apply_on_jobs = requests.post(apply_url, data=data, headers=headers)
    print apply_on_jobs.json()['success']
