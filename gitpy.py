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

    developer_api = "https://api.github.com"
    git_config_path = r'C:\Users\baby\Google Drive\meta-data\github\blackhathack3r'
    os.environ['gitpy_path'] = git_config_path

    def __init__(self,username=None,password=None,token=None):
        self.authorized = False
        self.authorization_data = dict()
        self.username = username
        self.password = password
        self.token = token

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

    def authorization(self):
        ''' https://developer.github.com/v3/#authentication '''
        authorization_data = {'Authorization':'token {}'.format(self.token)}
        required_link = "https://api.github.com/users/:username" # required_link format in case of authorization
        required_link = self.developer_api + '/users/' + self.username # overiding required_link
        response = requests.get(required_link,headers=authorization_data)

        # print (response.headers # for debugging purpose)
        # for key in response.headers:
        #     print (key ,response.headers[key])

        if response.headers['X-RateLimit-Limit'] == "5000" and response.headers['Status'] == "200 OK": # authorization will increase limit
            self.authorized = True
            self.authorization_data = {'Authorization':'token {}'.format(self.token)}
            return('Authorization Successfull {}'.format(self.username))
        else:
            if response.headers['Status'] == '401 Unauthorized':
                return('Access Denied')
            elif response.headers['Status'] == '404 Not Found':
                return('Wrong Information')

def main():
    configuration = GitPy.get_initial_configuraion()
    username = configuration['username']
    token = configuration['token']
    g = GitPy(username = username,token = token)
    print(g.authorization())


if __name__ == '__main__':
    main()
