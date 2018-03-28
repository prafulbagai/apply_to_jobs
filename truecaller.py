
import requests

url = 'https://search5.truecaller.com/v2/search?q=8860850789&countryCode=IN&type=4&placement=SEARCHRESULTS,HISTORY,DETAILS&clientId=1&myNumber=lS579715a6df1651386d98435cPt6MDMPUwQcx8UdxAoknMr&registerId=164437037&encoding=json'


print requests.get(url).json()
