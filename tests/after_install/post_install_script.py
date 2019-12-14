from gitpy.core.auth import GitPy

def authentication_module():
    config_data = GitPy.get_initial_configuration()
    print(config_data)
    g = GitPy(username = config_data['username'], token = config_data['token'])
    '''
    or
    g = GitPy(username = 'username',token = 'token')
    '''
    print(g.check_connectivity()) # Connected
    print(g.authorization()) # Authorization Successfull {username}

if __name__ == '__main__':
    main()
