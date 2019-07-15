"""StackOVerflow.py."""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class Settings:
    """Settings."""

    MAIN_URL = 'https://stackoverflow.com'

    JOBFEED_URL = MAIN_URL + '/jobs'

    JOB_URL = MAIN_URL + '/jobs/%s/'

    DISMISS_JOB_URL = MAIN_URL + '/jobs/dismiss-job'

    DISMISS_JOB_DATA = {
        'fkey': 'f7a4a2e4d2f72e68dcea4188e79557735b4161bd45f99bdc2a593e91b0dee49b'
    }

    APPLY_URL = MAIN_URL + '/api/v1/candidate_opportunity/apply_bulk'

    APPLICATION_DATA = {
        'opp_ids': []
    }

    DISMISS_HEADERS = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '69',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://stackoverflow.com',
        'referer': 'https://stackoverflow.com/jobs?med=site-ui&ref=jobs-tab',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'cookie': 'prov=f8f4584f-69a8-d456-9071-d8eb7fcb94bb; ext_name=ojplmecpdpgccookcobabopnaifgidhf; uc=8fcc693b-0362-441e-88a1-7aaa95ec2b49; job-alert-tooltip-dismissed=Fri%2C%2012%20Apr%202019%2017%3A38%3A11%20GMT; se-consent=%7b%22s%22%3a1%2c%22d%22%3a%222019-04-12T17%3a39%3a21.1653691Z%22%7d; cc=9eca424f099d4f8fa2b18d07c78ee86b; notice-ctt=4%3B1555138568706; bhInfV_cl_id=8ZQQwlRf2Xf37S9dQAtVxecEJ1enHwZsvs18LDX0KI4k5DPFA2; interest-tour-dismissed=1; acct=t=f4kaY45Yey481kmVGeMMCyYUMvlImZNF&s=QoCsZsGG4fF3npDbi7EZh%2f6LQPIi79u8'
    }

    HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'cookie': 'prov=f8f4584f-69a8-d456-9071-d8eb7fcb94bb; ext_name=ojplmecpdpgccookcobabopnaifgidhf; uc=8fcc693b-0362-441e-88a1-7aaa95ec2b49; job-alert-tooltip-dismissed=Fri%2C%2012%20Apr%202019%2017%3A38%3A11%20GMT; se-consent=%7b%22s%22%3a1%2c%22d%22%3a%222019-04-12T17%3a39%3a21.1653691Z%22%7d; cc=9eca424f099d4f8fa2b18d07c78ee86b; notice-ctt=4%3B1555138568706; bhInfV_cl_id=8ZQQwlRf2Xf37S9dQAtVxecEJ1enHwZsvs18LDX0KI4k5DPFA2; interest-tour-dismissed=1; acct=t=rkpkVqigMawYFJMBXS8mH4%2fk%2b0MaCr8q&s=Kwq7o%2feEc2zkRrcibAkoJ3GGbL%2bW%2bW21'
    }


class StackOverflow(object):
    """Utils Class."""

    def _get_job_ids(self, page):
        """Fetch all job ids from the page."""
        params = {
            'sort': 'i',
            'pg': page
        }
        html = requests.get(Settings.JOBFEED_URL, params=params,
                            headers=Settings.HEADERS)
        print('\nUrl :- *****%s*****' % (html.url))
        html = html.content
        soup = BeautifulSoup(html, 'lxml')
        jobs = soup.findAll('div', {'class': '-job'})
        return [job.get('data-jobid') for job in jobs]

    def _check_is_one_click_apply(self, apply_url):
        """Checking if it's 1-click apply or outside apply."""
        url = urlparse(apply_url)
        base_url = '%s://%s' % (url.scheme, url.netloc)
        return base_url == Settings.MAIN_URL

    def _get_job_apply_url(self, job_id):
        url = Settings.JOB_URL % (job_id)
        html = requests.get(url, headers=Settings.HEADERS).content
        soup = BeautifulSoup(html, 'lxml')
        jobs = soup.findAll('a', {'class': 'js-url-apply'})
        return jobs[0].get('href') if jobs else None

    def _dismiss_job(self, job_id, page):
        params = {
            'id': job_id,
            'referrer': 'JobSearch',
            'url': 'https://stackoverflow.com/jobs?med=site-ui&ref=jobs-tab'

        }

        r = requests.post(Settings.DISMISS_JOB_URL,
                          data=Settings.DISMISS_JOB_DATA,
                          params=params, headers=Settings.DISMISS_HEADERS)
        if r.ok:
            print('Dismissing job :- %s' % (r.url))
        else:
            print('Could not dismiss job :- %s' % (r))

    def _apply(self, apply_url):
        """Applying for the job."""
        Settings.APPLICATION_DATA['opp_ids'] = job_ids
        response = requests.post(Settings.APPLY_URL,
                                 json=Settings.APPLICATION_DATA,
                                 headers=Settings.HEADERS)
        print(response.content())
        return True

    def start(self):
        """Main function."""
        page = 1
        while True:
            job_ids = self._get_job_ids(page=page)
            if not job_ids:
                break

            for job_id in job_ids:
                apply_url = self._get_job_apply_url(job_id)
                if not apply_url:
                    continue

                if not self._check_is_one_click_apply(apply_url):
                    # dismissing the job, so that it does not appear again in
                    # the search result.
                    # self._dismiss_job(job_id=job_id, page=page)
                    continue

                self._apply(apply_url)

            page += 1


def main():
    """Call function."""
    stackoverflow = StackOverflow()
    stackoverflow.start()
    print('\n******** END ********')


if __name__ == "__main__":
    main()
