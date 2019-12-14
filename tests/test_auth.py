import json ,logging , os , requests, unittest
from .initial_setup import initial_config_setup
from gitpy.core.auth import GitPy

class TestAuth(unittest.TestCase):

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
        self.username = self.configuration_data['username']
        self.token = self.configuration_data['token']
        self.gitpy_object = GitPy(username=self.username,token=self.token)

    def test_intial_configuration(self):
        self.logger.info('executing')
        self.assertEqual(self.configuration_data,GitPy.get_initial_configuration())
        self.logger.info('completed')

    def test_check_connectivity(self):
        self.logger.info('executing')
        msg = self.gitpy_object.check_connectivity()
        if(self.gitpy_object.is_connected):
            self.assertEqual(msg,'Connected')
        else:
            self.assertEqual(msg,'Please connect to Internet')
        self.logger.info('completed')

    def test_authorization(self):
        self.logger.info('executing')
        msg = self.gitpy_object.authorization()
        if(self.gitpy_object.is_connected == False):
            self.assertEqual(msg,'Please connect to Internet')
        else:
            self.gitpy_object = GitPy(username=self.username,token=self.token+'nonce')
            self.assertEqual(self.gitpy_object.authorization(),'Access Denied : Wrong Token')
            self.gitpy_object = GitPy(username=self.username+'nonce',token=self.token)
            self.assertEqual(self.gitpy_object.authorization(),'Access Denied : Wrong Username')
            self.gitpy_object = GitPy(username=self.username,token=self.token)
            self.assertEqual(self.gitpy_object.authorization(),'Authorization Successfull {}'.format(self.username))
            self.logger.info('completed')

if __name__ == '__main__':
    unittest.main()
