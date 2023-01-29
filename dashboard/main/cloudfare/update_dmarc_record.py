import requests
import time

def update_dmarc_record(mail_1,mail_2,zone_identifier, cloudfare_email, cloudfare_auth_code):

    print('CLOUDFARE.update_dmarc_records.STARTS')

    url = f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records"

    payload = {
        "content":f"v=DMARC1; p=quarantine; rua=mailto:{mail_1}; ruf=mailto:{mail_2}; fo=1",
        "name": "_dmarc",
        # "priority": "",
        "proxied": False,
        "ttl": 3600,
        "type": "TXT"
    }

    headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": f"{cloudfare_email}",
        "Authorization": f"Bearer {cloudfare_auth_code}"
    }
    response = requests.request(
        "POST", url, json=payload, headers=headers).json()

    print(response)

    print('CLOUDFARE.update_dmarc_records.ENDS')
