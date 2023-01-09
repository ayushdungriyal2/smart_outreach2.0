import requests

def enable_imap_active_s(access_token, org_id,zu_id, account_id, zoho_domain):
    print('ZOHO.ZOHO_USER.enable_imap_active_s.STARTS')

    api_end_point = f'https://mail.{zoho_domain}/api/organization/{org_id}/accounts/{account_id}'

    body_json = {
        "zuid": f"{zu_id}",
        "mode": "updateMobileSyncStatus",
        "activeSyncEnabled": "true"
    }

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}

    response = requests.request(
        "PUT", api_end_point, headers=headers, json=body_json).json()

    # ---------------------------------------------------------------------------------------------

    # Define Body And Json Here

    body_json = {
        "zuid": f"{zu_id}",
        "mode": "updateIMAPStatus",
        "imapAccessEnabled": "true",
    }

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}

    response = requests.request(
        "PUT", api_end_point, headers=headers, json=body_json).json()

    print('ZOHO.ZOHO_USER.enable_imap_active_s.ENDS')


# enable_imap_active_s(
#     '1000.a332e0a9926b6b8ae32601ca501f3f2b.a64123f7458dffd5df3788e5ed8e32fe', 60018218815, 2880362000000002002)