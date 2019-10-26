import json
import logging
import unittest
import os
from gitpy import GitPy

class TestGitPy(unittest.TestCase):

    logger = None

    @classmethod
    def setUpClass(cls):
        ''' Setting up logger before testing whole script '''
        file_name = os.path.basename(__file__).split('.')[0]
        cls.logger = logging.Logger(file_name)
        cls.logger.setLevel(logging.DEBUG)
        file_handle = logging.FileHandler(file_name + '.log')
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handle.setFormatter(log_format)
        cls.logger.addHandler(file_handle)
        cls.logger.debug('Setting up Logger')

        ''' Setting up config file path env'''
        git_config_path = r'C:\Users\baby\Google Drive\meta-data\github\babygame0ver'
        os.environ['gitpy_path'] = git_config_path

    @classmethod
    def tearDownClass(cls):
        cls.logger.debug('Shutting down logger')

    def test_intial_configuration(self):
        self.logger.info('calling test_intial_configuration')
        config_file = os.environ['gitpy_path'] + '\config.json'
        with open(config_file,'r') as f:
            data = json.loads(f.read())
        self.assertEqual(data,GitPy.get_initial_configuraion())
        self.logger.info('completed test_intial_configuration')

if __name__ == '__main__':
    unittest.main()
