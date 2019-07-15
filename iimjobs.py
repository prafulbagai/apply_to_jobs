"""IIMJob.py."""

import requests
from bs4 import BeautifulSoup


class Settings:
    """Settings."""

    MAIN_URL = 'https://www.iimjobs.com/'

    JOBFEED_URL = MAIN_URL + 'jobfeed/filter/delhi_delhi-ncr_faridabad_ghaziabad_gurgaon-gurugram_noida-36_1_40_41_37_38-0-%s-%s.html'

    APPLY_URL = MAIN_URL + 'registration/applyform_controller.php'

    CHECK_APPLIED_JOBS_URL = MAIN_URL + 'includes/getajaxresponse.php'

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
        'name': 'Henna Malik',
        'email': 'hennamalik91@gmail.com',
        'phone': '8860850789',
        'dob': '1991-09-05',
        'cloc': '221',
        'ploc': '221,5,9',
        'industries': '8',
        'expyear': '4y',
        'expmonth': '0m',
        'currentctc': '8',
        'expectedctc': '12',
        'confidential': '0',
        'negotiable': '1',
        'eduFrom[0][id]': '602086',
        'eduFrom[0][institute]': '106',
        'eduFrom[0][otherInstitute]': 'Osmania University',
        'eduFrom[0][coursetype]': '1',
        'eduFrom[0][degree]': '8',
        'eduFrom[0][regbatchfrom]': '2009',
        'eduFrom[0][regbatchto]': '2012',
        'proFrom[0][id]': '693592',
        'exp_status': '0',
        'proFrom[0][designation]': 'Communication Specialist',
        'proFrom[0][organizationval]': 'Scientific Animations',
        'proFrom[0][organization]': 'Scientific Animations',
        'resumename': '2018-04-19-15-03-10-638404.docx',
        'atchcvrletter': 'on',
    }

    HEADERS = {
        'Cookie': 'PHPSESSID=p45e4hhqsoh17lva7cf68f2426; PHPSESSID=dca02ffd23778d74aee01482b63b8a1a; IIMXID=dca02ffd23778d74aee01482b63b8a1a; __utmc=1; __utmz=1.1530979161.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ext_name=jaehkpjddfdgiiefcnhahapilbejohhj; __utma=1.239524285.1530979161.1530979161.1530982803.2; IIMJOBS_CK1=52pQ%2F9LDzkcO96%2FHwurgubSdE9qofvsp8Y%2FtdyHG4nKiA4GAqYpTZOZEycwHXP%2BwxT82suDnTA0QpzHMT3l4Ng%3D%3D; ck12pb=NjM4NDA0LS1oZW5uYW1hbGlrOTFAZ21haWwuY29t; filterexp=0; filterexp=0; 638404name=Henna+Malik; __utmt=1; __utmb=1.428.0.1530988098960; userjobcount=0; IIMJOBS_LASTACT=08-07-2018; 638404prostatus=0; 638404prolastdate=0',
    }

    ERROR_LIMIT = 5
    ERROR_CODE = 'E'

    SUCCESS_RESPONSE = 'SUCCESS'
    SUCCESS_CODE = 'S'

    ALREADY_APPLIED_RESPONSE = b'ALLREADY_APPLIED'
    ALREADY_APPLIED_CODE = 'A'


class IIMJob(object):
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

    def get_list_of_unapplied_job_ids(self, available_job_ids):
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
        print(unapplied_jobs)
        return unapplied_jobs

    def get_job_ids(self, url):
        """Fetch all job ids from the page."""
        html = requests.get(url, headers=Settings.HEADERS).content
        soup = BeautifulSoup(html, 'lxml')

        # getting list of all job ids from the page url.
        job_id_divs = soup.findAll('div', {'class': 'jobRow'})
        available_job_ids = [div.get('data-jobid') for div in job_id_divs]

        # return the list of unapplied jobs from the above list of job_ids.
        return self.get_list_of_unapplied_job_ids(available_job_ids)

    def apply(self, job_id):
        """Applying for the job."""
        if not job_id:
            return None

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
            print(response)
            return Settings.ERROR_CODE

    def start(self):
        """Main function."""
        url = self.get_page_url()
        job_ids = self.get_job_ids(url)
        if not job_ids:
            return

        errors, already_applied, flag = 0, 0, False
        for job_id in job_ids:
            if not job_id:
                continue

            # Applying.
            status = self.apply(job_id)
            print(status)
            # if status == Settings.ALREADY_APPLIED_CODE:
            #     print('Already applied on `%s`, Continuing...' % (job_id))
            #     already_applied += 1
            #     # If more than 5 errors, then break.
            #     if already_applied >= Settings.ERROR_LIMIT:
            #         flag = True
            #         break
            #     continue

            # elif status == Settings.ERROR_CODE:
            #     print('Some error on `%s`, Continuing...' % (job_id))
            #     errors += 1
            #     # If more than 5 errors, then break.
            #     if errors >= Settings.ERROR_LIMIT:
            #         flag = True
            #         break
            #     continue

            # re-setting. Will only break, if there are consecutive
            # re-applications/errors found.
            # already_applied, errors = 0, 0

            print('Applied on `%s`' % (job_id))

        if flag:
            # There were many `already_applied` jobs in previous page,
            # now checking for next page.
            return self.start()

        return None


def main():
    """Call function."""
    iimjob = IIMJob()
    iimjob.start()
    print('\n******** END ********')


if __name__ == "__main__":
    main()
