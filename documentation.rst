
=========================================================
Initial Configuration for GitPy : Create a config.json file with Username and Token in Your System or Create env variable with Username and Token having values as username and token.
=========================================================

For config.json file you need to edit git_config_path in auth.py file as follow.

File Location for editing git_config_path: gitpy/core/auth.py

.. image :: tests/after_install/config_json.PNG

After Installation

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
