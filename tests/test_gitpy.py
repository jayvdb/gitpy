import json
import logging
import unittest
import os

from core.gitpy import GitPy

class TestGitPy(unittest.TestCase):

    logger = None
    configuration_data = dict()
    gitpy_object = None

    @classmethod
    def setUpClass(cls):
        ''' Setting up logger before testing whole script '''
        file_name = os.path.basename(__file__).split('.')[0]
        cls.logger = logging.Logger(file_name)
        cls.logger.setLevel(logging.DEBUG)
        file_handle = logging.FileHandler(file_name + '.log')
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s: - %(message)s')
        file_handle.setFormatter(log_format)
        cls.logger.addHandler(file_handle)
        cls.logger.debug('Setting up Logger')

        ''' Setting up config file path env'''
        git_config_path = r'C:\Users\baby\Google Drive\meta-data\github\blackhathack3r'
        os.environ['gitpy_path'] = git_config_path
        config_file = os.environ['gitpy_path'] + '\config.json'
        with open(config_file,'r') as f:
            cls.configuration_data = json.loads(f.read())

    @classmethod
    def tearDownClass(cls):
        cls.logger.debug('Shutting down logger\n')

    def test_intial_configuration(self):
        self.logger.info('executing')
        config_file = os.environ['gitpy_path'] + '\config.json'
        with open(config_file,'r') as f:
            self.configuration_data = json.loads(f.read())
        self.assertEqual(self.configuration_data,GitPy.get_initial_configuraion())
        self.logger.info('completed')

    def test_authorization(self):
        self.logger.info('executing')
        username = self.configuration_data['username']
        token = self.configuration_data['token']
        self.gitpy_object = GitPy(username=username,token=token)
        msg = self.gitpy_object.authorization()
        if(self.gitpy_object.is_connected == False):
            self.assertEqual(msg,'Please connect to Internet')
        else:
            self.gitpy_object = GitPy(username=username,token=token+'nonce')
            self.assertEqual(self.gitpy_object.authorization(),'Access Denied : Wrong Token')
            self.gitpy_object = GitPy(username=username+'nonce',token=token)
            self.assertEqual(self.gitpy_object.authorization(),'Access Denied : Wrong Username')
            self.gitpy_object = GitPy(username=username,token=token)
            self.assertEqual(self.gitpy_object.authorization(),'Authorization Successfull {}'.format(username))
            self.logger.info('completed')

    def test_check_connectivity(self):
        self.logger.info('executing')
        username = self.configuration_data['username']
        token = self.configuration_data['token']
        self.gitpy_object = GitPy(username=username,token=token)
        msg = self.gitpy_object.check_connectivity()
        if(self.gitpy_object.is_connected):
            self.assertEqual(msg,'Connected')
        else:
            self.assertEqual(smg,'Please connect to Internet')
        self.logger.info('completed')

if __name__ == '__main__':
    unittest.main()
