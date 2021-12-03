import sys
import time
import json
import requests
from threading import Timer

def send_data(cookie):

    checkin = requests.post(
        'https://glados.rocks/api/user/checkin',
        headers={'cookie': cookie,
            'referer': 'https://glados.rocks/console/checkin',
            'origin':'https://glados.rocks',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
            'content-type':'application/json;charset=UTF-8'
            },
        data=json.dumps({
            'token': 'glados_network'
        })
    )
    # url2= "https://glados.rocks/api/user/status"
    # state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
    res = json.loads(checkin.text)
    del res["list"]
    print("Time:", time.asctime(time.localtime()), res)
    assert res["code"] in [0,1]


if __name__ == "__main__":
    cookie = sys.argv[1]
    if cookie:
        send_data(cookie)
