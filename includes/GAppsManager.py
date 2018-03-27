from __future__ import print_function
from ghelpers import *
from helpers import write_json_log


class GAppsManager(object):
    def __init__(self, config):
        admin_email = config['super_admin_email']
        key_path = config['key_file_path']
        scopes = [
            'https://www.googleapis.com/auth/admin.directory.group',
            'https://www.googleapis.com/auth/admin.directory.group.member',
            'https://www.googleapis.com/auth/admin.directory.orgunit',
            'https://www.googleapis.com/auth/admin.directory.user',
            'https://www.googleapis.com/auth/admin.directory.user.alias',
            'https://www.googleapis.com/auth/admin.directory.domain'
        ]
        self.client = build_service(get_credentials(key_path, admin_email, scopes))
        write_json_log({
            'action': 'gapps',
            'message': 'Connected to Google!',
            'log-type': 'information'
        })

    def new_account(self, account):
        return True

    def update_account(self, account):
        return True

    def delete_account(self, account):
        return True

    def restore_account(self, account):
        return True
