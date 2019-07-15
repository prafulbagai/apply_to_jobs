
# """Instahyre.py."""

# import requests


# class Settings:
#     """Settings."""

#     MAIN_URL = 'https://angel.co'

#     JOBFEED_URL = MAIN_URL + '/job_listings/startup_ids'

#     APPLY_URL = MAIN_URL + '/job_pairings'

#     GET_JOBS_DATA = {
#         'filter_data[roles][]': 'Software Engineer',
#         # 'filter_data[types][]': 'full-time',
#         'tab': 'find'
#     }

#     APPLICATION_DATA = {
#         'job_pairing[startup_id]': None,
#         'job_pairing[user_interested]': 1,
#         'job_pairing[candidate_processed_listing_ids][]': None,
#         'job_pairing[user_note]': "Having a diversified profile and always excited about learning new technologies, I feel that I'll be the best fit to the organization.Although my profile illustrates my background well, I feel that a personal interview would better demonstrates my knowledge and abilities. Therefore, I would appreciate the opportunities to interview with you at a convenient time.",
#         'tab': 'find'
#     }

#     HEADERS = {
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
#         'x-csrf-token': 'LQyxpy8lyaitdSayE2wswXeP3HXSOhmLV4wixPTPyNfYr+vAjbUQIe/f3urFSf5DGkmo7V+AmdeetpzEJIa1yg==',
#         'cookie': '__cfduid=dcba5ddbe1cd9b1792fef99c3d45be2561555090666; ajs_group_id=null; ext_name=ojplmecpdpgccookcobabopnaifgidhf; intercom-id-og2vxfl5=a63cf7df-5a23-4355-89fe-d49d5d0bc67b; ajs_anonymous_id=%22ea43e63b1976369f300ac37dedc3a311%22; _angellist=0204223abde2a0234a4eed0c8c2b2a89; ajs_user_id=%22520277%22; bhInfV_cl_id=8ZQQwlRf2Xf37S9dQAtVxecEJ1enHwZsvs18LDX0KI4k5DPFA2; __cf_bm=75ee8cbf254658e798726a15f8b432f29d5ba272-1556540130-1800-ASL8kLcWsMKsKs0v0VkDBxbBj9m+c81x3GNs5FBb/J9vs/sCBraXatA1WE6t4qWiPxL1XN2Q5oEHPDymzpPGbsc=',
#         'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'x-requested-with': 'XMLHttpRequest',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'en-US,en;q=0.9',
#         'origin': 'https://angel.co',
#         'referer': 'https://angel.co/jobs'
#     }


# class Angel(object):
#     """Utils Class."""

#     def get_job_ids(self):
#         """Fetch all job ids from the page."""
#         response = requests.post(Settings.JOBFEED_URL,
#                                  data=Settings.GET_JOBS_DATA,
#                                  headers=Settings.HEADERS)
#         print(response)#.json()
#         return (response.get('ids', []), response.get('listing_ids', []))

#     def apply(self, startup_id, listing_ids):
#         """Applying for the job."""
#         Settings.APPLICATION_DATA['job_pairing[startup_id]'] = startup_id
#         Settings.APPLICATION_DATA['job_pairing[candidate_processed_listing_ids][]'] = listing_id
#         response = requests.post(Settings.APPLY_URL,
#                                  json=Settings.APPLICATION_DATA,
#                                  headers=Settings.HEADERS)
#         print(response.json())
#         return True

#     def start(self):
#         """Main function."""
#         startups, listings = self.get_job_ids()
#         if len(startups) != len(listings):
#             print('***** Some error..*****')
#             return

#         for startup_id, listing_ids in zip(startups, listings):
#             self.apply(startup_id, listing_ids)


# def main():
#     """Call function."""
#     angel = Angel()
#     angel.start()
#     print('\n******** END ********')


# if __name__ == "__main__":
#     main()
import math
def return_divisors(n) : 
      
    divisors = []
    i = 1
    while i <= math.sqrt(n): 
        if (n % i == 0) : 
            if (n / i != i) : 
                divisors.append(int(n/i))
            divisors.append(i)
        i = i + 1
    
    return divisors

print(return_divisors(100))