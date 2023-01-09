import requests


def update_dkim_records(zone_identifier,dkim_public_Key, cloudfare_email, cloudfare_auth_code):
    print('CLOUDFARE.update_dkim_records.STARTS')

    # DNS RECORDS
    print(dkim_public_Key)

    type = ['TXT']
    name = ['zoho._domainkey']
    content = [f'{dkim_public_Key}']
    priority = [None]

    for type, content, name, priority in zip(type, name, content, priority):

        url = f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records"

        payload = {
            # "content": f"{content}",
            # "name": f"{name}",
            "content": f"{name}",
            "name": f"{content}",
            "priority": priority,
            "proxied": False,
            "ttl": 3600,
            "type": f"{type}"
        }
        headers = {
            "Content-Type": "application/json",
            "X-Auth-Email": f"{cloudfare_email}",
            "Authorization": f"Bearer {cloudfare_auth_code}"
        }
        response = requests.request(
            "POST", url, json=payload, headers=headers).json()

        print(response)

    print('CLOUDFARE.update_dkim_records.ENS')
