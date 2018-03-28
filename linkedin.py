
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
    'Cookie': '_ncenv[lang]=en; _ncenv[env]=locale; test=naukri.com; _t_ds=0557145001502794127-FAC64C0AB366-7D1B4F564E2E; _t_s=direct; __utma=159336229.723011715.1502794129.1502794129.1502820555.2; __utmz=159336229.1502794129.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.723011715.1502794129; _gid=GA1.2.1977671088.1502794131; __gads=ID=512b6529245d804b:T=1502794132:S=ALNI_MZIsRMPas-7hcnAzLQNlXYBV2QEBw; _t_us=599338C9; ak_bmsc=FE5E3CAD4CB3AF27EADEC07323033523174C9D8DE9390000C9389359AA12321D~plbLR9XdPCE/Fc+7/jAlxeAhacl7715A0vBG/K/bGMJ2JLv42XbFhItnYnQBPyJkRaq+WXTWvnZhmf9CYvpIYlS6LlqQkTCu8+0jIp/9ieFG1S7cWxrC4CTo8XOsw4gecrpgUnSAr6JKFIWwr0bGnzS7d583h1Vi38EBzbzViVkNz/P/HI+chPnlwDteJtim20IxF3jEFLN44ajp9tiyaeQZxIKku+0IgZeNHWCBZSpE8=; __utmb=159336229.16.9.1502820727277; __utmt=1; _t_r=1092%2F%2F; PHPSESSID=2eja9kt28ns9h15kk689bkv5i1; bm_mi=707D25053323967865354FB27A9B1EA3~ezKg+PIlD2S3QXFb+GsCUKnnJfX4zcxHpHQTPtEmhRCGslx9qG24P1ohBp8iyOpdeOCTg/mgQMxkFNYq/AP0ZmU0h9Gqxc2gLD5wLSC6vkpmKA8vANuxqYaFJja4byh+g7o1Zt/8E3qgVECOEc3p5CrN9ZMUhia6GcYsoPC6EpjR6DKgmhoFecxyiMlexqYVJiPBaXVVJNyKVoTWyv9UAWtQrbFqO7whY3bEDmecEv7kqHOdywwfupfGibZS70bRg401Y8Qpnl0Asj5ZJzlsgU78qoA+UghCRr/OaDDTPYQ=; __utmc=159336229; MYNAUKBMS[resolution]=1280; HOWTORT=ul=1502820954547&r=https%3A%2F%2Fwww.naukri.com%2Fjob-listings-Python-Developer-full-Stack-Wigzo-Technologies-Startup-Delhi-3-to-5-years-140817900137%3Fsrc%3DjobsearchDesk%26sid%3D15028206436051%26xp%3D7%26qp%3Dpython%26srcPage%3Ds&hd=1502820939130&cl=1502820942219&nu=https%3A%2F%2Fwww.naukri.com%2Fjob-listings-Python-Developer-full-Stack-Wigzo-Technologies-Startup-Delhi-3-to-5-years-140817900137%3Fsrc%3DjobsearchDesk%26sid%3D15028206436051%26xp%3D7%26qp%3Dpython%26srcPage%3Ds; MYNAUKRI[ID]=7eb881cfeac8fd1e6c400efe563204d4e4d7e2ba6f45f462d74faf597045a3a6ff003c62a2e1a36431b890266d0ecd01%7CX%7CY%7CX%7CU; MYNAUKRI[TOUT]=1502820954; MYNAUKRI[RESID]=884d4e01e65dd31b81aeaddf5f29afe4f5f386eb65881e30; MYNAUKRI[USERID]=4c8dde7561511ec9f6278c167c35c780f8c0c35a811352d1; MYNAUKRI[UNID]=3ac74e642423192827; _gat_UA-182658-1=1'

}
url = 'https://www.naukri.com/ims/intercept'
r = requests.post(url, data=data, headers=headers, allow_redirects=False)
print r.content
