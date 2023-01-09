def get_zone_identifier(domain_name,cloudfare_email,cloudfare_auth_code):

    print('CLOUDFARE.get_zone_identifier.START')

    # First Retrive List Of All ZONES

    import requests

    url = f"https://api.cloudflare.com/client/v4/zones/"

    headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": f"{cloudfare_email}",
        "Authorization": f"Bearer {cloudfare_auth_code}"
    }

    response = requests.request("GET", url, headers=headers).json()
    
    # storing all zones and their all details in zone list 

    zone_list = response['result']

    for zone in zone_list:
        if zone['name'] == domain_name:
            zone_identifier = zone['id']

    print('CLOUDFARE.get_zone_identifier.ENDS')
    print(zone_identifier)
    return zone_identifier


# get_zone_identifier('dropdegree.com')