
import requests

# Get jobs.
main_url = 'https://www.instahyre.com'
openings_url = main_url + '/api/v1/candidate_opportunity'
headers = {
    'Cookie': 'csrftoken=eWUfmsIleH9XcfZVm2h62MqvqMZSZdvR; _ga=GA1.2.492545165.1502790162; _gid=GA1.2.45754374.1502790162; _gat=1; _hp2_ses_props.2646653911=%7B%22ts%22%3A1502790161605%2C%22d%22%3A%22www.instahyre.com%22%2C%22h%22%3A%22%2Flogin%2F%22%7D; _hp2_id.2646653911=%7B%22userId%22%3Anull%2C%22pageviewId%22%3A%226992789291936664%22%2C%22sessionId%22%3A%228134033306543629%22%2C%22identity%22%3A%22praful.bagai1991%40gmail.com%22%2C%22trackerVersion%22%3A%223.0%22%7D; sessionid=8f6ovlzqsdsb5u4wteppipaj79b74jfv',
}
jobs = requests.get(openings_url, headers=headers).json()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;',
    'X-CSRFToken': 'eWUfmsIleH9XcfZVm2h62MqvqMZSZdvR',
    'Referer': 'https://www.instahyre.com/job-5167-sde-2-at-amazon-6/',
    'Cookie': 'csrftoken=eWUfmsIleH9XcfZVm2h62MqvqMZSZdvR; _ga=GA1.2.492545165.1502790162; _gid=GA1.2.45754374.1502790162; _hp2_ses_props.2646653911=%7B%22ts%22%3A1502790161605%2C%22d%22%3A%22www.instahyre.com%22%2C%22h%22%3A%22%2Flogin%2F%22%7D; _hp2_id.2646653911=%7B%22userId%22%3Anull%2C%22pageviewId%22%3A%224656845657177700%22%2C%22sessionId%22%3A%228134033306543629%22%2C%22identity%22%3A%22praful.bagai1991%40gmail.com%22%2C%22trackerVersion%22%3A%223.0%22%7D; sessionid=8f6ovlzqsdsb5u4wteppipaj79b74jfv',
}
data = {
    'is_interested': True
}
for job in jobs['objects']:
    if job['id'] == 1461519:
        apply_url = main_url + job['resource_uri'] + '/apply'
        r = requests.post(apply_url, data=data, headers=headers).json()
        print r, job['employer']['company_name'], job['id']
