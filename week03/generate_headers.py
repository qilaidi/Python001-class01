import re

def generate_header(content):
    headers = {}
    content = raw_formatter(content)
    content = content.split("\n")
    content = [item.split(": ") for item in content]
    for item in content:
        headers[item[0]] = item[1]
    return headers

def raw_formatter(content):
    content = content.strip("\n")
    content = content.strip()
    return content

if __name__ == "__main__":
    content = """
Cookie: LGRID=20200711214951-dbab9452-a404-460c-b504-61526fa0d84a; LGSID=20200711214951-7dce6cbe-0d10-4e75-bcc3-d44d5a7b4aa4; PRE_HOST=; PRE_LAND=https%3A%2F%2Fm.lagou.com%2F; PRE_SITE=; PRE_UTM=; _ga=GA1.2.2123862506.1594475391; _gid=GA1.2.1199929341.1594475391; _ga=GA1.3.2123862506.1594475391; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1594475390; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1594475390; X_HTTP_TOKEN=669644b246cf4e3c09357449514e10057f70f9a86e; Hm_lpvt_2f04b07136aeba81b3a364fd73385ff4=1594475391; Hm_lvt_2f04b07136aeba81b3a364fd73385ff4=1594475391; JSESSIONID=ABAAABAABGJABAJE0B81011D1314364EAFF9A09AAE00B6F; user_trace_token=20180415145551-08b1713b-407a-11e8-b885-5254005c3644; LGUID=20170219212343-a2a41067-f6a6-11e6-9012-5254005c3644
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Host: m.lagou.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15
Accept-Language: en-sg
Accept-Encoding: br, gzip, deflate
Connection: keep-alive
    """
    print(generate_header(content))
