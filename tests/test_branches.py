import json ,logging , os , requests, unittest
from gitpy.repository.branch.branches import branches
from .initial_setup import initial_config_setup

class TestBranches(unittest.TestCase):

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
        cls.configuration_data = initial_config_setup()

    @classmethod
    def tearDownClass(cls):
        cls.logger.debug('Shutting down logger\n')

    def setUp(self):
        self.logger.info('executing')
        self.branch_object = branches()
        self.logger.info('completed')

    def test_get_all_branches_of_a_repo(self):
        self.logger.info('executing')
        msg = ''
        repo_name = 'repository-two'
        required_link = self.branch_object.gitpy_object.developer_api + '/repos/{}/{}/branches'.format(self.branch_object.username,repo_name)
        try:
            session = requests.session()
            response = session.get(required_link,headers=self.branch_object.gitpy_object.authorization_data)
            msg = response.json()
            session.close()
        except requests.exceptions.RequestException as e:
            msg = 'Please connect to Internet'
        self.assertEqual(self.branch_object.get_all_branches_of_a_repo(repo_name),msg)
        self.logger.info('completed')
