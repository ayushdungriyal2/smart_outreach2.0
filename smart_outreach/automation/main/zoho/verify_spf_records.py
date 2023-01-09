import requests
import time
def verify_spf_records(domain_name,access_token,org_id,zoho_domain):    

    print('ZOHO.verify_spf_records.STARTS')    

    api_end_point = f'https://mail.{zoho_domain}/api/organization/{org_id}/domains/{domain_name}'

    body_json = {
    "mode": "VerifySpfRecord"
    }

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}


    response = requests.request("PUT", api_end_point,headers=headers, json=body_json).json()

    if response['status']['code'] != 200:
        time.sleep(2)
        print('sleep')
        verify_spf_records(domain_name,access_token,org_id,zoho_domain)

    print('ZOHO.verify_spf_records.ENDS')


