
import requests
from bs4 import BeautifulSoup

# Getting the main page.
main_url = 'https://hasjob.co'
headers = {
    'cookie': 'YOUR_COOKIE',
}
html = requests.get(main_url, headers=headers).content
soup = BeautifulSoup(html, 'lxml')

links = soup.findAll('a', {'class': 'stickie'}) + \
    soup.findAll('div', {'class': 'stickie'})

# Getting job urls
job_urls = [link['data-href'] if link.get('data-href') else link['href'] for link in links]

errors = []
for url in job_urls:
    # Fetching csrf_token of specific job form.
    reveal_url = main_url + url + '/reveal'
    html = requests.post(reveal_url, headers=headers).content
    soup = BeautifulSoup(html, 'lxml')
    try:
        csrf_token = soup.find('input', {'id': 'csrf_token'}).get('value')
    except Exception, e:
        error = {
            'job_id': url,
            'exception': html,
            'type': 'reveal'
        }
        errors.append(error)
        continue

    # Applying for the job.
    apply_url = main_url + url + '/apply'
    data = {
        'form.id': 'applyform',
        'csrf_token': csrf_token,
        'apply_email': 'YOUR_EMAIL',
        'apply_phone': 'YOUR_PHONE_NUMBER',
        'apply_message': 'YOUR_MESSAGE'
    }

    html = requests.post(apply_url, data=data, headers=headers).content
    soup = BeautifulSoup(html, 'lxml')
    success = soup.find('div', {'class': 'flash'})
    if not success:
        error = {
            'job_id': url,
            'exception': html,
            'type': 'apply'
        }
        errors.append(error)
        continue

    print 'Applied on ' + url


# print errors
