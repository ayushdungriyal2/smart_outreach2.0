import requests


def add_domain(domain_name, access_token, org_id,zoho_domain):
    print('ZOHO.add_domain.STARTS')

    # Define API End Point

    api_end_point = f'https://mail.{zoho_domain}/api/organization/{org_id}/domains'

    # Define Body And Json Here

    body_json = {'domainName': f'{domain_name}', }

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}

    response = requests.request(
        "POST", api_end_point, headers=headers, json=body_json).json()
    try:
        CNAMEVerificationCode = response['data']['CNAMEVerificationCode']
        print('ZOHO.add_domain.ENDS')
        print('ZOHO.add_domain.ENDS')
        return (CNAMEVerificationCode)

    except:
        print('error in zoho.add_domain 🤒')
        print('-----------------------------')
        print(response)
        print('-----------------------------')
        print('ZOHO.add_domain.ENDS')
        return 'error'




# for debugging

# add_domain('dropdegree.com')
