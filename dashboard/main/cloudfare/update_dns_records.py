import requests

def update_dns_records(zone_identifier, CNAMEVerificationCode,zoho_domain, cloudfare_email, cloudfare_auth_code):

    print('CLOUDFARE.update_dns_records.STARTS')
    
    type = ['CNAME', 'MX', 'MX', 'MX', 'TXT', 'TXT', 'A', 'CNAME',]
    content = [f'{CNAMEVerificationCode}', '@', '@', '@', '@', '@', 'www', 'smart',]
    name = [f'zmverify.{zoho_domain}', f'mx.{zoho_domain}', f'mx2.{zoho_domain}', f'mx3.{zoho_domain}',
               f'v=spf1 include:{zoho_domain} ~all', '192.0.2.1', '192.0.2.1', 'open.sleadtrack.com',]

    priority = [10, 10, 20, 50, None, None, None, None, None]

    for type, content, name, priority in zip(type, name, content, priority):

        url = f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records"

        payload = {
            "content": f"{content}",
            "name": f"{name}",
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
    print('CLOUDFARE.update_dns_records.ENDS')


# update_dns_records('dropdegree.com')

