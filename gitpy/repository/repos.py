import requests
from gitpy.core.auth import GitPy

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

    def create_post_data(self,repo_name,access):
        ''' https://developer.github.com/v3/repos/#create
         Actual command from curl is :
        curl -H "Authorization: token xxx" https://api.github.com/user/repos -d
        '{ "name": "Hello-World",
        "description": "This is your first repository",
        "homepage": "https://github.com",
        "private": false/true,
        "has_issues": true,
        "has_projects": true,
        "has_wiki": true }'''

        required_link = 'https://api.github.com/user/repos' # name of repository will be passed in post request.
        repo_meta_data = {
          "name": "{}".format(repo_name),
          "description": "",
          "homepage": "",
          "has_issues": True,
          "has_projects": True,
          "has_wiki": True
        }
        if(access): # for private repo
            repo_meta_data["private"] = "True"

        repo_data_string = ','.join(['"%s":"%s"' % (key, value) for (key, value) in repo_meta_data.items()])
        repo_data_string = '{' + repo_data_string +  '}' # data has to be submitted in the form of string-dictionary / only dictionary always
        return repo_data_string

    def create_repository(self,repo_name,access):
        ''' Creating repository'''
        payload = self.create_post_data(repo_name,access)
        required_link = 'https://api.github.com/user/repos'
        return_msg = ''
        try:
            session = requests.session()
            response = session.post(required_link,data = payload, headers = self.gitpy_object.authorization_data)
            session.close()
        except requests.exceptions.RequestException as e:
            return_msg = ['Bad Request {}'.format(self.username)]
        if self.gitpy_object.is_connected:
            if self.gitpy_object.authorized:
                if response.status_code == 201:
                    return_msg = [response.json() , response.status_code , 'Repository Created Sucessfully'] #3
                elif response.status_code == 422:
                    return_msg = ['The repository {} already exists on this account'.format(repo_name),response.status_code] # 2
                else:
                    return_msg = ['Please Try Again'] # 1
            else:
                return_msg = ['Access Denied'] #1
        else:
            return_msg = ['Please connect to Internet'] #1
        return return_msg

    def create_public_repository(self,repo_name):
        return self.create_repository(repo_name,False)

    def create_private_repository(self,repo_name):
        return self.create_repository(repo_name,True)

    def delete_a_repository(self,repo_name):
        ''' Deletes a repository using it's name
        https://developer.github.com/v3/repos/#delete-a-repository
        https://api.github.com/repos/:owner/:repo
        '''
        response = None
        return_msg = ''
        required_link = self.gitpy_object.developer_api + '/repos/{}/{}'.format(self.gitpy_object.username,repo_name)
        try:
            session = requests.session()
            response = session.delete(url = required_link , headers = self.gitpy_object.authorization_data)
            session.close()
        except requests.exceptions.RequestException as e:
            return_msg = ['Bad Request {}'.format(self.username)]
        if response.status_code == 204:
            return_msg = ['{} Sucessfully Deleted'.format(repo_name),response.status_code]
        elif response.status_code == 403:
            return_msg = ['Organization members cannot delete repositories.',response.status_code]
        return return_msg

def main():
    pass

if __name__ == '__main__':
    main()
