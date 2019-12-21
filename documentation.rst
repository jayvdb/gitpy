
=========================================================
GitPy : Python Interface to GitHub's developer API
=========================================================

Overview :

A command line package purely written in Python3 consumes GitHub developer's API and provides all the functionalities in one place using Python Function.

* Core : Deals with authentication with GitHub API using Authentication token.

* Repository : Deals with information & actions related to both public & private Repositories.


1. Using Gitpy to Authenticate the username and token

.. code-block:: python

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

    def main():
        authentication_module()

    if __name__ == '__main__':
        main()
