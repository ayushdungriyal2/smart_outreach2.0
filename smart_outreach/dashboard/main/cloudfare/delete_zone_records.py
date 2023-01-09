def delete_zone_records(zone_identifier,list_dns_records, cloudfare_email, cloudfare_auth_code):
    print('CLOUDFARE.delete_zone_records.STARTS')

    import requests
    for dns_id in list_dns_records[0]:

        url = f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records/{dns_id['id']}"

        headers = {
                    "Content-Type": "application/json",
                    "X-Auth-Email": f"{cloudfare_email}",
                    "Authorization": f"Bearer {cloudfare_auth_code}"
        }

        response = requests.request("DELETE", url, headers=headers).json()
    print('CLOUDFARE.delete_zone_records.ENDS')