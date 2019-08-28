#!/usr/bin/env python3



import requests

class GitHubPy:

    access_token_path = 'path'

    def __init__(self,username):
        self.username = username

    @staticmethod
    def get_access_token():
        ''' Get access token from local directory '''
        return(GitHubPy.access_token_path)

def main():
    print(GitHubPy.get_access_token())


if __name__ == '__main__':
    main()
