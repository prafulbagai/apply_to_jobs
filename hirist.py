
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
    'Cookie': 'PHPSESSID=skf76c1aru952es1ph3vpimmd0; PHPSESSID=skf76c1aru952es1ph3vpimmd0; IIMXID=skf76c1aru952es1ph3vpimmd0; filterexp=0; __utma=1.1336474.1502794259.1502794259.1502794259.1; __utmb=1.19.0.1502794260003; __utmc=1; __utmz=1.1502794259.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; HIRIST_CK1=x60KBjRVmip3Sx68yJzw7VOCXIwqTR%2FhbvZicZMNdl51NKoQLRkQYdL7oNv3ZgvLxUGGvTFEoNhVqVpX1%2Fr42w%3D%3D; userjobcount=0; HIRIST_LASTACT=15-08-2017; 93376prostatus=0; 93376prolastdate=0; 93376name=Praful+Bagai; ck12pb=OTMzNzYtLXByYWZ1bC5iYWdhaTE5OTFAZ21haWwuY29t; successmsgstr=meRIfg372I5YU2VHNifjjwSWLv%2FWXTl8yjIrT1XfDHqvNLoVlBWIV1oTlYjaz0w8IU9KYQc764CjBsIOo%2F4Qng%3D%3D',
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
