def get_access_token(refresh_token, client_id, client_secret, zoho_domain):
    # refresh access token for zoho
    from .zoho import get_access_token
    access_token = get_access_token.get_access_token( refresh_token, client_id, client_secret, zoho_domain)
    print('new access token generated')
    return access_token



def zoho_cloudfare_dns_automation(access_token, domain_name, mail_1, mail_2, refresh_token, client_id, client_secret, zoho_domain, cloudfare_email, cloudfare_auth_code):

    from .cloudfare import update_dmarc_record, get_zone_identifier, update_dns_records, update_dkim_records, list_dns_records, delete_zone_records as update_dmarc_record, get_zone_identifier, update_dns_records, update_dkim_records, list_dns_records, delete_zone_records
    from .zoho import get_dkim_id, verify_dkim_records, verify_spf_records, verify_mx_records, get_access_token, add_domain, verify_domain, get_dkim_key, enable_domain_hosting, get_org_id, delete_domain as get_dkim_id, verify_dkim_records, verify_spf_records, verify_mx_records, get_access_token, add_domain, verify_domain, get_dkim_key, enable_domain_hosting, get_org_id, delete_domain
    from .zoho import get_dkim_id as get_dkim_id
    from .cloudfare import update_dmarc_record as update_dmarc_record
    import time

    # get zoid or org_id form zoho

    org_id = get_org_id.get_org_id(access_token, zoho_domain)

    # Delete if domain already exist

    delete_domain.delete_domain(domain_name, access_token, org_id, zoho_domain)

    # Add Domain To Zoho and retive CNAME Record values

    CNAMEVerificationCode = add_domain.add_domain(
        domain_name, access_token, org_id, zoho_domain)  # Domain Name Added To Zoho

    # checking if domain was added 

    if CNAMEVerificationCode == 'error':
        # intentionally sending eror 
        access_token = ' '
        cloudfare_email = ' '

    # get domain name's zone_identifier from cloudfare

    zone_identifier = get_zone_identifier.get_zone_identifier(
        domain_name, cloudfare_email, cloudfare_auth_code)

    # list current dns records

    list_dns_records = list_dns_records.list_dns_records(
        zone_identifier, cloudfare_email, cloudfare_auth_code)

    # delete current dns records in cloudfare

    delete_zone_records.delete_zone_records(
        zone_identifier, list_dns_records, cloudfare_email, cloudfare_auth_code)

    # update dns records on cloud fare

    update_dns_records.update_dns_records(
        zone_identifier, CNAMEVerificationCode, zoho_domain, cloudfare_email, cloudfare_auth_code)

    # verify cname records form zoho

    verify_domain.verify_domain(access_token, domain_name, org_id, zoho_domain)

    #  Enable Domain Email Hosting from zoho

    enable_domain_hosting.enable_domain_hosting(
        access_token, domain_name, org_id, zoho_domain)

    # Get dkim record from zoho

    dkim_public_Key = get_dkim_key.get_dkim_key(
        domain_name, access_token, org_id, zoho_domain)

    # update dns records for dkim key cloudfare

    update_dkim_records.update_dkim_records(
        zone_identifier, dkim_public_Key, cloudfare_email, cloudfare_auth_code)

    # get dkim id from zoho

    dkim_id = get_dkim_id.get_dkim_id(
        access_token, domain_name, org_id, zoho_domain)

    # verify mx records in zoho

    verify_mx_records.verify_mx_records(
        domain_name, access_token, org_id, zoho_domain)

    # verify spf records in zoho

    verify_spf_records.verify_spf_records(
        domain_name, access_token, org_id, zoho_domain)

    # verify dkim records in zoho
    dkim_attemp_no = 0
    verify_dkim_records.verify_dkim_records(
        domain_name, access_token, org_id, dkim_id, zoho_domain, dkim_attemp_no)

    # update dmarc record Cloudfare

    update_dmarc_record.update_dmarc_record(
        mail_1, mail_2, zone_identifier, cloudfare_email, cloudfare_auth_code)

    print('zoho_cloudfare_dns_automation completed successfully!🎉')
    return True

    # create new user in zoho and return zuid_accountid_list


def zoho_create_users(access_token, refresh_token, client_id, client_secret, email, name, password, zoho_domain):

    from .zoho_user import create_user, enable_imap_active_s as create_user, enable_imap_active_s
    from .zoho_user import create_user as create_user
    from .zoho import get_access_token as get_access_token
    from .zoho import get_org_id as get_org_id

    # get org id
    org_id = get_org_id.get_org_id(access_token, zoho_domain)
    print(org_id)

    zuid_accountid_list = create_user.create_user(
        access_token, org_id, email, name, password, zoho_domain)

    print(zuid_accountid_list)

    if type(zuid_accountid_list) == str:
        print(zuid_accountid_list)
        return zuid_accountid_list

    else:

        # seperating zuid and account_id from zuid_accountid_list
        zu_id = zuid_accountid_list[0]
        account_id = zuid_accountid_list[1]

        # Enable IMAP & Active Sync on zoho

        enable_imap_active_s.enable_imap_active_s(
            access_token, org_id, zu_id, account_id, zoho_domain)

        print('zoho_create_users completed successfuly! 🎉')

        return True
