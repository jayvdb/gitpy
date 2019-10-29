import requests
from core.gitpy import GitPy

class Repository():

    def __init__(self):
        self.configuration_data = GitPy.get_initial_configuration()
        self.username = self.configuration_data['username']
        self.token = self.configuration_data['token']
        self.gitpy_object = GitPy(username = self.username,token = self.token)
        self.gitpy_object.authorization()

    def list_all_user_repositories(self):
        '''List all the repositories of User https://api.github.com/:user/repos '''
        return_msg = 'Please connect to Internet'
        if (self.gitpy_object.authorized):
            required_link = self.gitpy_object.developer_api + '/user/repos'
            try:
                session = requests.session()
                response = session.get(required_link,headers=self.gitpy_object.authorization_data)
                if response.status_code == 200:
                    return_msg = response.json()
                else:
                    return_msg = 'Bad Request : {}'.format(response.status_code)
                session.close()
            except requests.exceptions.RequestException as e:
                return_msg = 'Request Error'
        else:
            if not (self.gitpy_object.is_connected):
                return_msg = 'Please connect to Internet'
            else:
                return_msg = 'Access Denied'
        return return_msg


    def list_all_public_repositories(self):
        '''List all public repositories GET /repositories '''
        return_msg = 'Please connect to Internet'
        if (self.gitpy_object.authorized):
            required_link = self.gitpy_object.developer_api + '/users/{}/repos'.format(self.username)
            try:
                response = requests.get(required_link)
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

def main():
    user_repos = Repository()



if __name__ == '__main__':
    main()
