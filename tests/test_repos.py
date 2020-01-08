import json ,logging , os , requests, unittest
from gitpy.repository.repos import Repository
from .initial_setup import initial_config_setup

class TestRepository(unittest.TestCase):

    logger = None
    configuration_data = dict()
    gitpy_object = None

    @classmethod
    def setUpClass(cls):
        ''' Setting up logger before testing whole script '''
        file_name = os.path.basename(__file__).split('.')[0]
        dir_path = os.path.dirname(os.path.realpath(__file__))
        log_file_path = os.path.join(dir_path, 'logs', file_name + '.log')
        cls.logger = logging.Logger(file_name)
        cls.logger.setLevel(logging.DEBUG)
        file_handle = logging.FileHandler(log_file_path)
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s: - %(message)s')
        file_handle.setFormatter(log_format)
        cls.logger.addHandler(file_handle)
        cls.logger.debug('Setting up Logger')
        cls.configuration_data = initial_config_setup()

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
        required_link = self.repository_object.gitpy_object.developer_api + '/users/{}/repos'.format(self.repository_object.gitpy_object.username)
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
        self.logger.info('executing')
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
        self.logger.info('completed')
        return [response.status_code,return_msg]

    def test_create_public_repository(self):
        self.logger.info('executing')
        repo_name = 'repository-three-public'
        response = self.repository_object.create_public_repository(repo_name) #  created repository
        if len(response) == 3: # created
            self.assertEqual(response[2],'Repository Created Sucessfully')
        elif len(response) == 2: # already existed
            self.assertEqual(response[0],'The repository {} already exists on this account'.format(repo_name))
        else: # errors handling
            if not (self.repository_object.gitpy_object.is_connected):
                self.assertEqual(response[0],'Please connect to Internet')
            else:
                if not (self.repository_object.gitpy_object.authorized): # not(False) -> True
                    self.assertEqual(response[0],'Access Denied')
        self.logger.info('completed')

    def test_create_private_repository(self):
        self.logger.info('executing')
        repo_name = 'repository-four-private'
        response = self.repository_object.create_private_repository(repo_name) #  created repository
        if len(response) == 3: # created
            self.assertEqual(response[2],'Repository Created Sucessfully')
        elif len(response) == 2: # already existed
            self.assertEqual(response[0],'The repository {} already exists on this account'.format(repo_name))
        else: # errors handling
            if not (self.repository_object.gitpy_object.is_connected):
                self.assertEqual(response[0],'Please connect to Internet')
            else:
                if not (self.repository_object.gitpy_object.authorized): # not(False) -> True
                    self.assertEqual(response[0],'Access Denied')
        self.logger.info('completed')

    def test_delete_a_repository(self):
        self.logger.info('executing')
        repos_list = ['repository-four-private','repository-three-public']
        response = self.repository_object.delete_a_repository(repos_list[0])
        if (response[1] == 204):
            self.assertEqual('{} Sucessfully Deleted'.format(repos_list[0]),response[0])
        else:
            self.assertEqual('Organization members cannot delete repositories.',response[0])
        response = self.repository_object.delete_a_repository(repos_list[1])
        if (response[1] == 204):
            self.assertEqual('{} Sucessfully Deleted'.format(repos_list[1]),response[0])
        else:
            self.assertEqual('Organization members cannot delete repositories.',response[0])
        self.logger.info('completed')
