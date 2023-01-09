import requests
import time
def verify_mx_records(domain_name,access_token,org_id,zoho_domain):

    print('ZOHO.verify_mx_records.STARTS')    

    api_end_point = f'https://mail.{zoho_domain}/api/organization/{org_id}/domains/{domain_name}'

    body_json = {
    "mode": "verifyMxRecord"
    }

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}


    response = requests.request("PUT", api_end_point,headers=headers, json=body_json).json()

    if response['status']['code'] != 200:
        time.sleep(2)
        print('sleep')
        verify_mx_records(domain_name,access_token,org_id,zoho_domain)

    print('ZOHO.verify_mx_records.ENDS')


