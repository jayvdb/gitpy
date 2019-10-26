'''
GitPy is a command line tool to consume the developer_api of github using authentication Token
It shows all the public/private information for a github account with token.
Functionality of the script
1. Initial configuration
2. Test authentication token for account using header
'''
import json
import os
import requests

class GitPy:

    git_config_path = r'C:\Users\baby\Google Drive\meta-data\github\babygame0ver'
    os.environ['gitpy_path'] = git_config_path

    def __init__(self,username=None,password=None,token=None):
        self.authorized = False
        self.username = username
        self.password = password
        self.token = None

    @staticmethod
    def get_initial_configuraion():
        '''Get Initial configuration from file'''
        if GitPy.git_config_path is None:
            print('Please specify the token path in Script')
            return None
        else:
            config_path = os.environ['gitpy_path'] + '\config.json'
            with open(config_path,'rb') as f:
                dict = json.load(f)
                return dict

def main():
    configuration = GitPy.get_initial_configuraion()
    print(configuration.keys())
    print('Username : ',configuration['username'])


if __name__ == '__main__':
    main()
