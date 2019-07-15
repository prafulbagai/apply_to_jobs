"""Instahyre.py."""

import requests


class Settings:
    """Settings."""

    MAIN_URL = 'https://www.instahyre.com'

    JOBFEED_URL = MAIN_URL + '/api/v1/candidate_opportunity?limit=10'

    APPLY_URL = MAIN_URL + '/api/v1/candidate_opportunity/apply_bulk'

    APPLICATION_DATA = {
        'opp_ids': []
    }

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;',
        # 'X-CSRFToken': 'eWUfmsIleH9XcfZVm2h62MqvqMZSZdvR',
        'Referer': 'https://www.instahyre.com/job-5167-sde-2-at-amazon-6/',
        'Cookie': 'ext_name=ojplmecpdpgccookcobabopnaifgidhf; bhInfV_cl_id=O2jf3D0XMxzFvX8KLGCnZjnIzrDQsUgmfDGBGgxyH9JQgiv5qx; csrftoken=yCodMwCgYUDPNAogox35zJOrgjHzkj6L; sessionid=j96799kk9nyecqvksnpucvgq28gn6czd',
    }


class Instahyre(object):
    """Utils Class."""

    def __init__(self):
        self.STOP = False
        self.URL = Settings.JOBFEED_URL

    def get_job_ids(self):
        """Fetch all job ids from the page."""
        if not self.URL:
            return []

        response = requests.get(self.URL, headers=Settings.HEADERS).json()
        meta = response.get('meta', {})
        next = meta.get('next')
        if next:
            self.URL = Settings.MAIN_URL + next
        else:
            self.URL = None
        jobs = response.get('objects', [])
        return [job.get('id') for job in jobs]

    def apply(self, job_ids):
        """Applying for the job."""
        if not job_ids:
            return None

        print(job_ids)
        Settings.APPLICATION_DATA['opp_ids'] = job_ids
        response = requests.post(Settings.APPLY_URL,
                                 json=Settings.APPLICATION_DATA,
                                 headers=Settings.HEADERS)
        print(response.json())
        return True

    def start(self):
        """Main function."""

        while True:
            job_ids = self.get_job_ids()
            if not job_ids:
                break
            self.apply(job_ids)


def main():
    """Call function."""
    instahyre = Instahyre()
    instahyre.start()
    print('\n******** END ********')


if __name__ == "__main__":
    main()
