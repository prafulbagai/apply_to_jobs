
import requests
from bs4 import BeautifulSoup

# Getting the main page.
main_url = 'https://hasjob.co'
headers = {
    'cookie': '_gat=1; _ga=GA1.2.1239332014.1497597866; _gid=GA1.2.1124343132.1502641845; ext_name=jaehkpjddfdgiiefcnhahapilbejohhj; lastuser=eyJhbGciOiJIUzI1NiIsInYiOjF9.eyJzZXNzaW9uaWQiOiI0TzBuT0ZKa0VlZVBTZHMxOVdmdUpBIiwidXNlcmlkIjoiMGNUZG5RM3RUWk9QaXcyUXV0a0JhZyJ9.9s8pDNfEdBCgsERdwZLY_GMNqW6ZtBKIOmdj4np2JjA; session=.eJxFjk9rgzAchr9KyDmH_DHGCD0UHLJBAt0sQ8cY1l-mttWWtmHU4ndf1h52ei_P-_DccHM-fX9dDjs34vSG0Qan2PIVq97Xohyqzhb7wU4wlFvzY6anqMpeuirbXcup25vta2_y56vJV8K2iwWeCXbnu8YHDeUgtXKO0dhFDkDHUvFaJ3QDCQA0f3jrDmM9uB7C7YNxJbiOyGNF2FgrSUnMpWSR-iS4P9YAp__QrPEhypti7W2xvAf0x8sjAQLw5keCmEBL3yJOmUIsSYVOOUO5KfA8_wLyQkoU.DHIwBg.ZMvow9GeM3_rVxOV5wxBdBp16mE',
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
        'apply_email': 'praful.bagai1991@gmail.com',
        'apply_phone': '9971081696',
        'apply_message': '<p>Hello ,<br />Nice to e-Connect with you.I saw your job posting for the Software Developer Position. Although the accompanying resume illustrates my background well, I feel that a personal interview would better demonstrates my knowledge and abilities. Therefore, I would appreciate the opportunities to interview with you at a convenient time.</p><p>Thank you for your review and consideration. Looking forward for your reply.</p><p>Resume :-&nbsp;<a href="https://drive.google.com/open?id=0BwBxFtjIcKzlOEx4ajFNcG1YZUk" target="_blank">https://drive.google.com/open?id=0BwBxFtjIcKzlOEx4ajFNcG1YZUk</a></p><p>LinkedIn Profile :-&nbsp;<a href="https://www.linkedin.com/in/prafulbagai" target="_blank">https://www.linkedin.com/in/prafulbagai</a></p><p>Notice Period - 15 Days</p>'
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
