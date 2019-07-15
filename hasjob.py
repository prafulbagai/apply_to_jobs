"""HasJob.py."""

import requests
from bs4 import BeautifulSoup
import dateutil.parser as parser

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
>>>>>>> f5e5922be8cfa638440c8d42fe22b153f89e4ff1

class Settings:
    """Settings."""

    MAIN_URL = 'https://hasjob.co'

    APPLY_URL = MAIN_URL + '%s/apply'

    REVEAL_URL = MAIN_URL + '%s/reveal'

    APPLICATION_DATA = {
        'form.id': 'applyform',
<<<<<<< HEAD
        'csrf_token': '%s',
        'apply_email': 'prafulbagai04@gmail.com',
        'apply_phone': '9971010041',
        'apply_message': "<p>Hello,</p><p>Nice to e-Connect with you.</p><p>I saw your job posting. I'm currently working as a Tech Lead for Seynse Technologies, a FinTech organization. I've 6 years of overall experience in building large scale distributed systems. Having worked at organizations at different growth levels, I recognize different business and product requirements. Also, I'm well equipped to handle teams or work independently.</p><p>Although the accompanying resume illustrates my background well, I feel that a personal interview would better demonstrate my knowledge and abilities. Therefore, I would appreciate the opportunities to interview with you at a convenient time.</p><p>Thank you for your review and consideration. Looking forward to your reply.</p><p>Resume :- https://drive.google.com/open?id=180wQUjSvMCGwo4QyRUiML30kqdn0YI2b</p><p>LinkedIn Profile :- https://www.linkedin.com/in/prafulbagai/</p><p>Notice Period - 1 month</p><p></p><p>Regards</p>"
    }

    HEADERS = {
        'cookie': '__cfduid=dc34a13ddeb5fee3f2c0763ab388de7de1555064307; ext_name=ojplmecpdpgccookcobabopnaifgidhf; _ga=GA1.2.784406599.1555065224; bhInfV_cl_id=8ZQQwlRf2Xf37S9dQAtVxecEJ1enHwZsvs18LDX0KI4k5DPFA2; _gid=GA1.2.1309881411.1558296661; lastuser=eyJhbGciOiJIUzUxMiIsInYiOjF9.eyJzZXNzaW9uaWQiOiJJSlk1SXpQS1ExZVNZcHBjeTNjamJ3IiwidXNlcmlkIjoiMGNUZG5RM3RUWk9QaXcyUXV0a0JhZyIsInVwZGF0ZWRfYXQiOiIyMDE5LTA1LTE5VDIwOjE0OjAxLjc0OTU3MCswMDowMCJ9.8PeBbpm5ybyK1x63fPB9rCSCClgF7m4U1SX7AMQu7SL6UloiMr0ZY9jOoHUj2BWx4ARj3jZWThLgZcvpCCHEqg; session=.eJw9jl1rwjAYhf9KyHUu8vGmaQteiHOjsmSIHZIOGZ1pt0ZbxQ9GK_3vyybs6pyLcx6eG96eT_X75bCrOpzeMPrAKbbDojFeC7te9pbPxUu-_yryfWPzOS8elkPhp4P1j63hi51us6FYv_bmezLBI8HV-Q9zDRgVAyhaM8WkAwkiAaVoVMdqC6UUnP7OP6tDV7ZV48LtjfGIQcwI40rwRISMEiUpibiUDNSG4OZYOnf6F9U-G5591psVCD0DMNO7RHO83DVcGK2uHUEsQbrsEaehcJoymsoYPekcj-MPAhxI7w.XOG5LQ.KAPgZKjwyPhyF3l6YbZnOzqAgFg',
=======
        'csrf_token': csrf_token,
        'apply_email': 'YOUR_EMAIL',
        'apply_phone': 'YOUR_PHONE_NUMBER',
        'apply_message': 'YOUR_MESSAGE'
>>>>>>> f5e5922be8cfa638440c8d42fe22b153f89e4ff1
    }

    ERROR_LIMIT = 5


class HasJob(object):
    """Utils Class."""

    def __init__(self):
        """Init Method."""
        self.startdate = None

    def update_last_date(self, soup):
        """Update `startdate` variable to fetch the jobs listed after it."""
        dates = soup.findAll('span', {'class': 'annotation top-right'})
        if dates:
            date = dates[-1].text
            date = ''.join(e for e in date if e.isalnum())
            self.startdate = parser.parse(date).isoformat() + 'z'

    def get_job_urls(self):
        """Fetch all job urls after `start_date`."""
        params = {
            'startdate': self.startdate,
            # 'l': ['delhi', 'gurgaon', 'sohna', 'noida']

        }
        html = requests.post(Settings.MAIN_URL, headers=Settings.HEADERS,
                             params=params)
        print('\nUrl :- *****%s*****' % (html.url))
        html = html.content
        # print (html)
        soup = BeautifulSoup(html, 'lxml')
        links = soup.findAll('a', {'class': 'stickie'}) + \
            soup.findAll('div', {'class': 'stickie'})

        # Getting job urls
        job_urls = []
        for link in links:
            if link.get('data-href'):
                job_urls.append(link['data-href'])
            else:
                job_urls.append(link['href'])

        self.update_last_date(soup)
        return job_urls

    def get_csrf_of_job(self, url):
        """Get csrf token of the job applying for."""
        url = Settings.REVEAL_URL % (url)
        html = requests.post(url, headers=Settings.HEADERS).content
        soup = BeautifulSoup(html, 'lxml')
        try:
            return soup.find('input', {'id': 'csrf_token'}).get('value')
        except Exception:  # arises when the position has already been applied.
            # error = {
            #     'job_id': url,
            #     'exception': html,
            #     'type': 'reveal'
            # }
            # logging.error(error)
            return None

    def apply(self, csrf_token, url):
        """Applying for the job."""
        Settings.APPLICATION_DATA['csrf_token'] = csrf_token
        url = Settings.APPLY_URL % (url)
        html = requests.post(url, data=Settings.APPLICATION_DATA,
                             headers=Settings.HEADERS).content
        soup = BeautifulSoup(html, 'lxml')
        success = soup.find('div', {'class': 'flash'})
        if not success:
            # error = {
            #     'job_id': url,
            #     'exception': html,
            #     'type': 'apply'
            # }
            return False
        return True

    def start(self):
        """Main function."""
        errors, already_applied, flag = 0, 0, False
        job_urls = self.get_job_urls()

        for url in job_urls:
            # Fetching csrf_token of specific job form.
            csrf_token = self.get_csrf_of_job(url)
            if not csrf_token:
                print('Already applied on `%s`, Continuing...' % (url))
                already_applied += 1
                if already_applied >= Settings.ERROR_LIMIT:
                    flag = True
                    break
                continue

            # Applying.
            success = self.apply(csrf_token, url)
            if not success:
                errors += 1
                # If more than 5 errors, then break.
                if errors >= Settings.ERROR_LIMIT:
                    flag = True
                    break
                continue

            # re-setting. Will only break, if there are consecutive
            # re-applications/errors found.
            already_applied, errors = 0, 0

            print('Applied on `%s`' % (url))

        if flag:
            # There were many `already_applied` jobs in previous page,
            # now checking for next page.
            return self.start()

        return None


def main():
    """Call function."""
    hasjob = HasJob()
    hasjob.start()
    print('\n******** END ********')


if __name__ == "__main__":
    main()
