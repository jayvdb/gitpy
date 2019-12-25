import json
import os
import requests

class GitPy:

    developer_api = "https://api.github.com"
    git_config_path = r'C:\Users\baby\Desktop\github\github'
    os.environ['gitpy_path'] = git_config_path

    def __init__(self,username=None,password=None,token=None):
        self.authorized = False
        self.authorization_data = dict()
        self.username = username
        self.password = password
        self.token = token
        self.is_connected = False

    @staticmethod
    def get_initial_configuration():
        '''Get Initial configuration from file'''
        if GitPy.git_config_path is None:
            return('Please specify the token path in Script')
        else:
            config_path = os.environ['gitpy_path'] + '\config.json'
            try:
                with open(config_path,'r') as f:
                    return json.loads(f.read())
            except:
                config_data = {'username' : '', 'token' : ''}
                username = os.environ['username']
                token = os.environ['token']
                config_data['username'] = username
                config_data['token'] = token
                return config_data

    def check_connectivity(self):
        try:
            response = requests.get(self.developer_api)
            self.is_connected = True
            return('Connected')
        except requests.exceptions.RequestException as e:
            return('Please connect to Internet')


    def authorization(self):
        ''' https://developer.github.com/v3/#authentication '''
        self.check_connectivity()
        if self.is_connected:
            return_msg = None
            authorization_data = {'Authorization':'token {}'.format(self.token)}
            api_url = "https://api.github.com/users/:username" # required_link format in case of authorization
            api_url = self.developer_api + '/users/' + self.username # overiding required_link
            try:
                response = requests.get(api_url,headers=authorization_data)
            except requests.exceptions.RequestException as e:
                return_msg = 'Please connect to Internet'
            if response.headers['X-RateLimit-Limit'] == "5000" and response.headers['Status'] == "200 OK" and (self.is_connected): # authorization will increase limit
                self.authorized = True
                self.authorization_data = {'Authorization':'token {}'.format(self.token)}
                return_msg = 'Authorization Successfull {}'.format(self.username)
            else:
                if response.headers['Status'] == '401 Unauthorized':
                    return_msg = 'Access Denied : Wrong Token'
                elif response.headers['Status'] == '404 Not Found':
                    return_msg ='Access Denied : Wrong Username'
            return return_msg
        else:
            return('Please connect to Internet')

def main():
    pass


if __name__ == '__main__':
    main()
