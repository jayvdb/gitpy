

def common_setup(cls,logger):
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
