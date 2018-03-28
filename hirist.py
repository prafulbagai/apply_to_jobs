
import requests
from bs4 import BeautifulSoup

# Get jobs.
main_url = 'http://www.hirist.com/k/filter/python-jobs-in-any-location-9-0-0-500-6.html'
html = requests.get(main_url).content
soup = BeautifulSoup(html, 'lxml')

links = soup.findAll('div', {'class': 'jobRow'})
count = 0
jobs = []
data = {
    'submitaction': 'APPLYALL',
    'mulsubmit': 'APPLY ALL',
}
headers = {
    'Cookie': 'YOUR_COOKIE',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:49.0) Gecko/20100101 Firefox/49.0'
}
for link in links:
    job_id = link.get('data-jobid')
    if not job_id:
        continue

    jobs.append(int(job_id))
    count += 1
    if count == 50:
        apply_url = 'http://www.hirist.com/registration/applydetail.php'
        data['mulapply[]'] = jobs
        r = requests.post(apply_url, data=data, headers=headers, allow_redirects=False)
        jobs = []
        count = 0
