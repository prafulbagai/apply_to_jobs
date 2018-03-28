
import requests

data = {
    'appid': 107,
    'applySrc': 'jobsearchDesk',
    'closebtn': 'y',
    'crossdomain': False,
    'flowtype': 'show',
    'jobid': '040717002091',
    'jquery': 1,
    'logstr': '--jobsearchDesk-7-F-0-1-',
    'mid': '',
    'sid': '1502822410776'
}

headers = {
    'Cookie': 'YOUR_COOKIE'

}
url = 'https://www.naukri.com/ims/intercept'
r = requests.post(url, data=data, headers=headers, allow_redirects=False)
print r.content
