import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs

ua = UserAgent(verify_ssl=False)
ua1 = ua.random
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Accept': '*/*',
    'Host': 'shimo.im',
    'Accept-Language': 'en-sg',
    'Accept-Encoding': 'br, gzip, deflate',
    'Origin': 'https://shimo.im',
    'Referer': 'https://shimo.im/login?from=home',
    'Content-Length': '76',
    'User-Agent': ua1,
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lpvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1593950187; Hm_lvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1593947547; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2241852717%22%2C%22%24device_id%22%3A%22172fb797f1ab8e-012435c9977fc4-481f3700-1296000-172fb797f1ba8d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22172fb797f1ab8e-012435c9977fc4-481f3700-1296000-172fb797f1ba8d%22%7D; sensorsdata2015session=%7B%7D; shimo_gatedlaunch=3; anonymousUser=-8162825785; shimo_sid=s%3AUeYZokoxgnrzYb5y5kkbAG9ECZ4Y3ybu.L%2Bowkk0Jz7zdS4su3azva08ZfiYiCGcnNosYNNlmbo0; _bl_uid=IXk0vcIL870zwngX2yLFdR5kUn1I; deviceId=6490ce65-26bf-443c-8399-554bb6d4de45; deviceIdGenerateTime=1593356940867; shimo_kong=4; shimo_svc_edit=1694; _csrf=srCyCv7jwyTG52PfOzjVap_s',
    'x-requested-with': 'XmlHttpRequest',
    'x-source': 'lizard-desktop'
}

s = requests.Session()

login_url = 'https://shimo.im/lizard-api/auth/password/login'
form_data = {
    'MIME Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'email': 'qilaidihaha@gmail.com',
    'mobile': '+86undefined',
    'password': 'test123!'
}

response = s.post(login_url, data=form_data, headers=headers)
print(response.status_code)

# headers2 = {
#     'cache-control': 'no-store, no-cache, must-revalidate',
#     'content-encoding': 'gzip',
#     'content-type': 'text/html; charset=utf-8',
#     'date': 'Sun, 05 Jul 2020 11:50:31 GMT',
#     'expires': 'Mon, 26 Jul 1997 05:00:00 GMT',
#     'server': 'openresty/1.15.8.2',
#     'set-cookie': 'shimo_gatedlaunch=8; Domain=.shimo.im; Path=/; Expires=Fri, 05 Jul 2030 11:50:31 GMT',
#     'set-cookie': 'shimo_gatedlaunch=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT',
#     'status': '200',
#     'strict-transport-security': 'max-age=15724800; includeSubDomains',
#     'vary': 'Accept-Encoding',
#     'x-request-id': '8d2e932c-6a61-416d-a102-9aa72bb0dae7',
#     'x-served-by': 'SHIMO-COW'
# }
#
# response = s.get('https://shimo.im/dashboard/favorites')
# print(bs(response.text, 'html.parser').find('title').text)

