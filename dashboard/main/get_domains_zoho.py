

def get_domains_zoho(refresh_token,client_id,client_secret,zoho_domain):
    import requests
    from .zoho import get_access_token
    from .zoho import get_org_id as get_org_id
    print('ZOHO.get_domains_zoho.STARTS')
    
    
    access_token = get_access_token.get_access_token(
        refresh_token, client_id, client_secret, zoho_domain)

    org_id = get_org_id.get_org_id(access_token, zoho_domain)


    # Define API End Point
    api_end_point = f'https://mail.{zoho_domain}/api/organization/{org_id}/domains'

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}

    response = requests.request(
        "GET", api_end_point, headers=headers).json()
    
    domain_name_dic = {'domain_name':[]}

    for data in response['data']['domainVO']:

        domain_name = data['domainName']
        if data['verificationStatus'] == True:
            domain_name_dic['domain_name'].append(domain_name)

    print(domain_name_dic)
    print('ZOHO.get_domains_zoho.ENDS')
    return domain_name_dic

