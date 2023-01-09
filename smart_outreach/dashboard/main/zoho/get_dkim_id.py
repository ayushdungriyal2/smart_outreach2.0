import requests
def get_dkim_id(access_token, domain_name, org_id,zoho_domain):

    print('ZOHO.get_dkim_id.STARTS')


    api_end_point = f'https://mail.{zoho_domain}/api/organization/{org_id}/domains/{domain_name}'

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}

    response = requests.request(
        "GET", api_end_point, headers=headers).json()

    dkim_id = response['data']['dkimDetailList'][0]['dkimId']

    print('ZOHO.get_dkim_id.ENDS')

    return dkim_id


# for debugging


