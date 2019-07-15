"""Hirist.py."""

import requests
from bs4 import BeautifulSoup


COUNT = 0


class Settings:
    """Settings."""

    MAIN_URL = 'https://www.hirist.com'

    JOBFEED_URL = MAIN_URL + '/jobfeed/filter/any-location-0-0-%s-%s.html'

    APPLY_URL = MAIN_URL + '/registration/applyform_controller.php'

    CHECK_APPLIED_JOBS_URL = MAIN_URL + '/includes/getajaxresponse.php'

    CHECK_APPLIED_JOBS_APPLICATION_DATA = {
        'act': 'get_user_data',
        'job_ids': []
    }

    APPLICATION_DATA = {
        'flowtype': '21',
        'jobid': '%s',
        'ref': 'jf',
        'refkey': '4',
        'cover': '',
        'inline': '',
        'formaction': 'ajaxsubmit',
        'name': 'Praful Bagai',
        'email': 'prafulbagai04@gmail.com',
        'phone': '9971010041',
        'dob': '1991-01-04',
        'cloc': '221',
        'ploc': '213',
        'industries': '1',
        'expyear': '5y',
        'expmonth': '10m',
        'currentctc': '33',
        'expectedctc': '45',
        'confidential': '1',
        'negotiable': '1',
        'eduFrom[0][id]': '75748',
        'eduFrom[0][institute]': 'guru tegh bahadur institute of technology',
        'eduFrom[0][otherInstitute]': 'guru tegh bahadur institute of technology',
        'eduFrom[0][coursetype]': '1',
        'eduFrom[0][degree]': '6',
        'eduFrom[0][regbatchfrom]': '2009',
        'eduFrom[0][regbatchto]': '2013',
        'proFrom[0][id]': '782652',
        'exp_status': '0',
        'proFrom[0][designation]': 'Tech Lead',
        'proFrom[0][organizationval]': 'Senynse Technologies',
        'proFrom[0][organization]': 'Senynse Technologies',
        'resumename': '2019-04-29-17-13-18-93376.pdf',
        'atchcvrletter': 'on',
    }

    HEADERS = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'PHPSESSID=sggd7s2435mk2jlhgq6m687pn7; PHPSESSID=e1f4024edd99847d444906bde790af5e; IIMXID=e1f4024edd99847d444906bde790af5e; __utmc=1; __utmz=1.1555065735.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ext_name=ojplmecpdpgccookcobabopnaifgidhf; bhInfV_cl_id=8ZQQwlRf2Xf37S9dQAtVxecEJ1enHwZsvs18LDX0KI4k5DPFA2; filterexp=0; hide_test=true; filterexp=0; 93376name=Praful+Bagai; AKA_A2=A; __utma=1.1350250950.1555065735.1556528181.1556533991.5; __utmt=1; HIRIST_CK1=Y45eh9eanC%2BgLgypzbZnHrW23pyLLZIgRtFFvLu5cRMQEV%2FOWGNscq85tgHuBSgk3sIq%2Bciq%2BElIKTONafrxWw%3D%3D; HIRIST_LASTACT=29-04-2019; 93376prostatus=0; 93376prolastdate=0; userjobcount=0; ck12pb=OTMzNzYtLXByYWZ1bGJhZ2FpMDRAZ21haWwuY29t; selfAssessment=1; __utmb=1.179.9.1556536047018',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }

    ERROR_LIMIT = 5
    ERROR_CODE = 'E'

    SUCCESS_RESPONSE = b'\nSUCCESS'
    SUCCESS_CODE = 'S'

    ALREADY_APPLIED_RESPONSE = b'\nALLREADY_APPLIED'
    ALREADY_APPLIED_CODE = 'A'


class Hirist(object):
    """Utils Class."""

    def __init__(self):
        """Init Method."""
        self.PAGE_NUMBER = 1
        self.MULTIPLIER = 100

    def get_page_url(self):
        """Build page url."""
        total_results_in_page = (self.PAGE_NUMBER - 1) * self.MULTIPLIER
        url = Settings.JOBFEED_URL % (total_results_in_page, self.PAGE_NUMBER)

        self.PAGE_NUMBER += 1
        print('\n Url:- %s' % url)
        return url

    def get_job_ids(self, url):
        """Fetch all job ids from the page."""
        def get_list_of_unapplied_job_ids(available_job_ids):
            """Return the list of applied jobs from the given job_ids."""
            data = Settings.CHECK_APPLIED_JOBS_APPLICATION_DATA
            data['job_ids'] = available_job_ids
            response = requests.post(Settings.CHECK_APPLIED_JOBS_URL,
                                     data=data,
                                     headers=Settings.HEADERS)
            try:
                applied_jobs = response.json()['data']['applied_jobs']
            except:
                return available_job_ids

            unapplied_jobs = []
            for job_id in available_job_ids:
                if not applied_jobs.get(job_id):
                    unapplied_jobs.append(job_id)
            return unapplied_jobs

        html = requests.get(url, headers=Settings.HEADERS).content
        soup = BeautifulSoup(html, 'lxml')

        # getting list of all job ids from the page url.
        job_id_divs = soup.findAll('div', {'class': 'jobRow'})
        available_job_ids = [div.get('data-jobid') for div in job_id_divs]

        # return the list of unapplied jobs from the above list of job_ids.
        return get_list_of_unapplied_job_ids(available_job_ids)

    def apply(self, job_id):
        """Applying for the job."""
        data = Settings.APPLICATION_DATA
        data['jobid'] = job_id
        response = requests.post(Settings.APPLY_URL,
                                 data=data,
                                 headers=Settings.HEADERS,
                                 allow_redirects=False).content
        if response == Settings.SUCCESS_RESPONSE:
            return Settings.SUCCESS_CODE
        elif response == Settings.ALREADY_APPLIED_RESPONSE:
            return Settings.ALREADY_APPLIED_CODE
        else:
            # print(response)
            return Settings.ERROR_CODE

    def start(self):
        """Main function."""
        global COUNT
        url = self.get_page_url()
        job_ids = self.get_job_ids(url)
        if not job_ids:
            COUNT += 1
            if COUNT == 5:
                return
            return self.start()

        for job_id in job_ids:
            if not job_id:
                continue

            status = self.apply(job_id)
            print (status, job_id)

        return self.start()


def main():
    """Call function."""
    hirist = Hirist()
    hirist.start()
    print('\n******** END ********')


if __name__ == "__main__":
    main()
