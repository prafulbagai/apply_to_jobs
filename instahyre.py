
import requests

# Get jobs.
main_url = 'https://www.instahyre.com'
openings_url = main_url + '/api/v1/candidate_opportunity'
headers = {
    'Cookie': 'YOUR_COOKIE',
}
jobs = requests.get(openings_url, headers=headers).json()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;',
    'X-CSRFToken': 'YOUR_CSRF_TOKEN',
    'Referer': 'https://www.instahyre.com/job-5167-sde-2-at-amazon-6/',
    'Cookie': 'YOUR_COOKIE',
}
data = {
    'is_interested': True
}
for job in jobs['objects']:
    if job['id'] == 1461519:
        apply_url = main_url + job['resource_uri'] + '/apply'
        r = requests.post(apply_url, data=data, headers=headers).json()
        print r, job['employer']['company_name'], job['id']
