import requests


def get_org_id(access_token,zoho_domain):
    print('ZOHO.get_org_id.STARTS')
    print(zoho_domain)
    print(access_token)
    # Define API End Point

    api_end_point = f'https://mail.{zoho_domain}/api/organization'

    # Define Body And Json Here

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}

    response = requests.request(
        "GET", api_end_point, headers=headers).json()


    org_id = response['data']['zoid']

    print('ZOHO.get_org_id.ENDS')

    return org_id



# for debugging

# add_domain('dropdegree.com')
