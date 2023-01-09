import requests
import time
def verify_domain (access_token,domain_name,org_id,zoho_domain):
    
    print('ZOHO.verify_domain.STARTS')
    
    api_end_point = f'https://mail.{zoho_domain}/api/organization/{org_id}/domains/{domain_name}'

    body_json = {
    "mode": "verifyDomainByCName"
    }

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}


    response = requests.request("PUT", api_end_point,headers=headers, json=body_json).json()

    if response['status']['code'] != 200:
        time.sleep(2)
        print('sleep')
        verify_domain (access_token,domain_name,org_id,zoho_domain)


    print('ZOHO.verify_domain.ENDS')



# for debugging 

# verify_domain('1000.f960a6f1f79e6160339663463c4508af.ba8a01356a437d2065b4563e8bba03fa', 'dropdegree.com') 