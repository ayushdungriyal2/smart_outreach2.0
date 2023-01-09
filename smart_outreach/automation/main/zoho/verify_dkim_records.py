import requests
import time


def verify_dkim_records(domain_name, access_token, org_id, dkim_id ,zoho_domain,dkim_attemp_no):
    dkim_attemp_no += 1
    print('ZOHO.verify_dkim_records.START')
    api_end_point = f'https://mail.{zoho_domain}/api/organization/{org_id}/domains/{domain_name}'

    body_json = {
        "mode": "verifyDkimKey",
        "dkimId": dkim_id
    }

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}

    response = requests.request(
        "PUT", api_end_point, headers=headers, json=body_json).json()

    if response['data']['dkimstatus'] == True:
        return response

    else:
        print(response)
        sleep_time = 30

        if dkim_attemp_no >= 5:
            sleep_time = 480
        for i in range(0, sleep_time):
            print(
                f"Waiting for cloudfare to update DKIM records] {i}/{sleep_time} seconds.", end="\r", flush=True)
            time.sleep(1)
        verify_dkim_records(domain_name, access_token, org_id, dkim_id, zoho_domain,dkim_attemp_no)

    print('ZOHO.verify_dkim_records.ENDS')


# verify_dkim_records('dropdegree.com','1000.416673d5e4467d87446b4840b1812cd4.bcb9ff6f6a23a0b0fb226ae62d23a60d','60018218815',5000011704025)
