from gitpy.repository.repos import Repository


def RepositoryModule():

    r = Repository()
    print(r.list_all_user_repositories()) # JSON response
    print(r.create_public_repository('My-Public-Repository'))
    print(r.create_private_repository('My-Private-Repository'))
    print(r.delete_a_repository('My-Public-Repository'))
    print(r.delete_a_repository('My-Private-Repository'))


def main():
    RepositoryModule()


if __name__ == '__main__':
    main()
