import requests
def generate_dkim_key(access_token, domain_name):
    print('ZOHO.generate_dkim_key.STARTS')


    org_id = 60018218815

    api_end_point = f'https://mail.zoho.in/api/organization/{org_id}/domains/{domain_name}'
    api_end_point = f'https://mail.zoho.in/api/organization/<{org_id}/domains/{domain_name}'

    body_json = {
        "mode": "regenerateDkimKey",
        "dkimId": "100000500000888000"
    }

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}

    response = requests.request(
        "PUT", api_end_point, headers=headers, json=body_json).json()
    print('ZOHO.generate_dkim_key.ENDS')


# for debugging

# verify_domain('1000.f960a6f1f79e6160339663463c4508af.ba8a01356a437d2065b4563e8bba03fa', 'dropdegree.com')
