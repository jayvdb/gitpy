from gitpy.core.auth import GitPy

def authentication_module_using_configFile():
    config_data = GitPy.get_initial_configuration()
    g = GitPy(username=config_data['username'],token=config_data['token'])
    print(config_data)
    print(g.check_connectivity()) # Connected
    print(g.authorization()) # Authorization Successfull {username}

def authentication_module_using_Credentials(): # bad practice -> never hard-code username & token in file
    g = GitPy(username = 'username',token = 'token')
    print(g.check_connectivity()) # Connected
    print(g.authorization()) # Authorization Successfull {username}


def main():
    authentication_module_using_configFile()
    authentication_module_using_Credentials()

if __name__ == '__main__':
    main()
