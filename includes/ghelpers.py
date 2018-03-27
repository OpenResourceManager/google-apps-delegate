from __future__ import print_function
from httplib2 import Http
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials


# Gets credentials from OAuth provider and impersonates the designated super admin.
def get_credentials(key_path, admin_emil, scopes):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(key_path, scopes)
    return credentials.create_delegated(admin_emil)


# Builds a google directory service
def build_service(credentials):
    http = credentials.authorize(Http())
    return discovery.build('admin', 'directory_v1', http=http)


def get_user(client, account, mail_domain):
    return client.users().get(account['username'] + '@' + mail_domain)


def update_or_create_user(client, account, mail_domain):
    return True
