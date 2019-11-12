from gitpy.core.auth import GitPy

def main():
    config_data = GitPy.get_initial_configuration()
    print(config_data)

if __name__ == '__main__':
    main()
