def list_dns_records(zone_identifier, cloudfare_email,cloudfare_auth_code):
    print('CLOUDFARE.list_dns_records.START')    
    list_dns_records = []
    
    import requests

    url = f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records"

    headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": f"{cloudfare_email}",
        "Authorization": f"Bearer {cloudfare_auth_code}"
    }

    response = requests.request("GET", url, headers=headers).json()


    list_dns_records.append(response['result'])
    print('CLOUDFARE.list_dns_records.ENDS')    
    return list_dns_records


