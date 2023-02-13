import requests
import re
import sys

session = requests.session()

github_url = "https://github.com:443/email_validity_checks"
req = session.get("https://github.com/signup")

authenticity_token = re.findall('data-csrf="true" value="(.*?)"', req.text)[0]

github_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://github.com/signup",
    "Content-Type": "multipart/form-data; boundary=---------------------------38585130253766616109330333206",
    "Origin": "https://github.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers",
}
github_data = (
    '-----------------------------38585130253766616109330333206\r\nContent-Disposition: form-data; name="authenticity_token"\r\n\r\n'
    + authenticity_token
    + '\r\n-----------------------------38585130253766616109330333206\r\nContent-Disposition: form-data; name="value"\r\n\r\n'
    + sys.argv[1]
    + "\r\n-----------------------------38585130253766616109330333206--\r\n\r\n\r\n"
)
req = session.post(
    github_url,
    headers=github_headers,
    data=github_data,
    allow_redirects=False,
)
print(req.status_code)
