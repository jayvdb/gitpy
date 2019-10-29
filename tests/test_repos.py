import json
import logging
import os
import requests
import unittest
from repository.repos import Repository

class TestRepository(unittest.TestCase):

    logger = None
    configuration_data = dict()
    gitpy_object = None

    @classmethod
    def setUpClass(cls):
        ''' Setting up logger before testing whole script '''
        file_name = os.path.basename(__file__).split('.')[0]
        dir_path = os.path.dirname(os.path.realpath(__file__))
        log_file_path = os.path.join(dir_path,'logs\\') + file_name + '.log'
        cls.logger = logging.Logger(file_name)
        cls.logger.setLevel(logging.DEBUG)
        file_handle = logging.FileHandler(log_file_path)
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s: - %(message)s')
        file_handle.setFormatter(log_format)
        cls.logger.addHandler(file_handle)
        cls.logger.debug('Setting up Logger')

        ''' Setting up config file path env'''
        git_config_path = r'C:\Users\baby\Google Drive\meta-data\github\blackhathack3r'
        os.environ['gitpy_path'] = git_config_path
        config_file = os.environ['gitpy_path'] + '\config.json'
        try:
            with open(config_file,'r') as f:
                cls.configuration_data = json.loads(f.read())
        except FileNotFoundError: # if not found go to travis environment variables
            config_data = {'username' : '', 'token' : ''}
            username = os.environ['username']
            token = os.environ['token']
            config_data['username'] = username
            config_data['token'] = token
            cls.configuration_data = config_data

    @classmethod
    def tearDownClass(cls):
        cls.logger.debug('Shutting down logger\n')

    def setUp(self):
        self.logger.info('executing')
        self.repository_object = Repository()
        self.repo_meta_data = {
          "description": "",
          "homepage": "",
          "has_issues": True,
          "has_projects": True,
          "has_wiki": True
        }
        self.logger.info('completed')

    def test_list_all_repositories(self):
        self.logger.info('executing')
        msg = ''
        required_link = self.repository_object.gitpy_object.developer_api + '/user/repos'
        try:
            session = requests.session()
            response = session.get(required_link,headers=self.repository_object.gitpy_object.authorization_data)
            msg = response.json()
            session.close()
        except requests.exceptions.RequestException as e:
            msg = 'Please connect to Internet'
        self.assertEqual(self.repository_object.list_all_user_repositories(),msg)
        self.logger.info('completed')

    def test_list_all_public_repositories(self):
        self.logger.info('executing')
        msg = ''
        required_link = self.repository_object.gitpy_object.developer_api + '/repositories'
        try:
            session = requests.session()
            response = requests.get(required_link)
            msg = response.json()
            session.close()
        except  requests.exceptions.RequestException as e:
            msg = 'Network Error'
        msg = self.repository_object.list_all_public_repositories()
        self.assertEqual(self.repository_object.list_all_public_repositories(),msg)
        self.logger.info('completed')

    def create_repository(self,repo_name,access):
        return_msg = ''
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
        # print(repo_data_string,required_link)
        try:
            session = requests.session()
            response = session.post(required_link,data = repo_data_string, headers = self.repository_object.gitpy_object.authorization_data)
            return_msg = response.json()
            session.close()
        except requests.exceptions.RequestException as e:
            return_msg = 'Bad Request {}'.format(self.username)
        return [response.status_code,return_msg]

    def test_create_public_repository(self):
        self.logger.info('executing')
        repo_name = 'repository-three-public'
        self.repository_object.create_public_repository(repo_name)
        required_link = self.repository_object.gitpy_object.developer_api+'/repos/{}/{}'.format(self.repository_object.username,repo_name)
        response = requests.get(required_link)
        self.assertEqual(response.status_code,200) # found create repository
        response = requests.get(required_link+'s')
        self.assertEqual(response.status_code,404) # not found repository
        self.logger.info('completed')

    def test_create_private_repository(self):
        self.logger.info('executing')
        repo_name = 'repository-four-private'
        self.repository_object.create_private_repository(repo_name)
        required_link = self.repository_object.gitpy_object.developer_api+'/repos/{}/{}'.format(self.repository_object.username,repo_name)
        response = requests.get(required_link,headers=self.repository_object.gitpy_object.authorization_data)
        self.assertEqual(response.status_code,200) # found create repository
        response = requests.get(required_link+'s')
        self.assertEqual(response.status_code,404) # not found repository
        self.logger.info('completed')
