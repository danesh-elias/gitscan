import requests
import re
import time

# import os
# from dotenv import load_dotenv

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "127.0.0.1:8080",
}

# load_dotenv()

# token = os.getenv("TOKEN")


def github_email_check(filename):
    with open(filename) as f:
        email_addresses = f.readlines()

    email_addresses = [email.strip() for email in email_addresses]

    email_count = 0

    session = requests.session()

    for email in email_addresses:
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
            + email
            + "\r\n-----------------------------38585130253766616109330333206--\r\n\r\n\r\n"
        )
        req = session.post(
            github_url,
            headers=github_headers,
            data=github_data,
            allow_redirects=False,
        )
        print(str(req.status_code) + "  :  " + email)

        email_count += 1
        if email_count % 50 == 0:
            print(f"Pausing for 60 seconds after processing {email_count} requests")
            time.sleep(60)
        else:
            time.sleep(1)


def github_repo_check(filename):
    with open(filename) as f:
        email_addresses = f.readlines()

    email_addresses = [email.strip() for email in email_addresses]

    email_count = 0

    # session = requests.session()

    for email in email_addresses:
        github_url = "https://api.github.com:443/search/users?q="
        github_headers = {
            "Accept-Encoding": "gzip, deflate",
            "Accept": "*/*",
            # "Authorization": "Bearer " + token,
            "Accept-Language": "en-US;q=0.9,en;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36",
            "Connection": "close",
            "Cache-Control": "max-age=0",
        }
        github_url = github_url + email
        req = requests.get(
            github_url,
            headers=github_headers,
        )
        print(req.json())

        email_count += 1
        if email_count % 10 == 0:
            print(f"Pausing for 60 seconds after processing {email_count} requests")
            time.sleep(60)
        else:
            # pass
            time.sleep(1)
