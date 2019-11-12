import requests

from gitpy.core.auth import GitPy

class branches():

    def __init__(self):
        self.configuration_data = GitPy.get_initial_configuration()
        self.username = self.configuration_data['username']
        self.token = self.configuration_data['token']
        self.gitpy_object = GitPy(username = self.username,token = self.token)
        self.gitpy_object.authorization()


    def get_all_branches_of_a_repo(self,repo_name):
        ''' List all the branches of given repository
        https://developer.github.com/v3/repos/branches/#list-branches
        '''
        return_msg = ''
        if (self.gitpy_object.authorized):
            required_link = self.gitpy_object.developer_api + '/repos/{}/{}/branches'.format(self.username,repo_name)
            try:
                session = requests.session()
                response = requests.get(required_link,headers=self.gitpy_object.authorization_data)
                session.close()
                if response.status_code == 200:
                    return_msg = response.json()
                else:
                    return_msg = 'Bad Request : {}'.format(response.status_code)
            except requests.exceptions.RequestException as e:
                return_msg = 'Request Error'
        else:
            if not (self.gitpy_object.is_connected):
                return_msg = 'Please connect to Internet'
            else:
                return_msg = 'Access Denied'
        return return_msg
