'''
this program is using the underlying api of Github https://developer.github.com/v3/
with requests module. The aim of this program is to get the repository from
user/orgranization (public/private).
Also to create the repository within organization and directly to user account.
'''
import requests

def get_access_token_from_directory():
    path = r'/home/baby/Desktop/github/account/access_token.txt'
    if path == None:
        print ("Please enter the path in the program")
        exit()
    access_token = open(path,'r').read().rstrip() # use rstrip() to remove trailing \n
    return access_token

class Github():

    base_link_api = "https://api.github.com"

    def __init__(self,token,username):
        self.token = token
        self.username = username
        self.authorized = False
        self.authorization_error = 'Call authorization() method first'
        self.authorization_data = {}

    def authorization(self):
        ''' https://developer.github.com/v3/#authentication '''
        authorization_data = {'Authorization':'token {}'.format(self.token)}

        required_link = "https://api.github.com/users/:username" # required_link format in case of authorization
        required_link = Github.base_link_api + '/users/' + self.username # overiding required_link
        response = requests.get(required_link,headers=authorization_data)

        # print (response.headers # for debugging purpose)
        # for key in response.headers:
        #     print (key ,response.headers[key])

        if response.headers['X-RateLimit-Limit'] == "5000" and response.headers['Status'] == "200 OK": # authorization will increase limit
            self.authorized = True
            self.authorization_data = {'Authorization':'token {}'.format(self.token)}
            print ('Your Token is working Correctly and Username is also correct.')
        else:
            if response.headers['Status'] == '401 Unauthorized':
                print ('Your authentication token in not correct')
            elif response.headers['Status'] == '404 Not Found':
                print ('Enter your Username Correctly')

    def get_user_repos(self): # get all repos in the users account only
        if self.authorized:
            pass
        else:
            print (self.authorization_error)

    def get_organization_repos(self,orgranization):
        ''' https://developer.github.com/v3/repos/#list-organization-repositories '''
        if self.authorized:
            required_link = "https://api.github.com/orgs/:org/repos" # required_link format in case of getting orgranization respositories
            org_link = '/orgs/{}/repos'.format(orgranization)
            required_link = Github.base_link_api + org_link # overiding required_link
            response = requests.get(required_link,headers=self.authorization_data)
            # print (response.status_code)
            print ((response.json())[0])
        else:
            print (self.authorization_error) # get all the repositories in an organization)

    # main function for gitcrypt
    def create_a_repo_in_an_organization(self,organization_name,repo_name):
        ''' https://developer.github.com/v3/repos/#create '''

        ''' Actual command from curl is :
        curl -H "Authorization: token xxx" https://api.github.com/orgs/capstone27/repos -d
        '{ "name": "Hello-World",
        "description": "This is your first repository",
        "homepage": "https://github.com",
        "private": false,
        "has_issues": true,
        "has_projects": true,
        "has_wiki": true }'
        ''' # hence the post data is actually a string in form of dictionary
        if self.authorized:
            required_link = 'https://api.github.com/orgs/:org/repos' # name of repository will be passed in post request.
            required_link = Github.base_link_api + '/orgs/{}/repos'.format(organization_name)
            repo_data = {
              "name": "{}".format(repo_name),
              "description": "",
              "homepage": "",

              "has_issues": True,
              "has_projects": True,
              "has_wiki": True
            }
                                        # string format % data      # dictionary comprehension --> converting dictionary into string
            repo_data_string = ','.join(['"%s":"%s"' % (key, value) for (key, value) in repo_data.items()])
            repo_data_string = '{' + repo_data_string +  '}' # data has to be submitted in the form of string-dictionary / only dictionary always

            response = requests.post(required_link,data=repo_data_string,headers=self.authorization_data) # for post request data + authentication_token

            if response.status_code == 201: # success
                new_repo_link = 'https://www.github.com/{}/{}'.format(organization_name,repo_name)
                print ('repository has been created with name {} in orgranization {} at link {}'.format(repo_name,organization_name,new_repo_link))
            elif response.status_code == 422: #failed
                print ('repository creatio failed as the name is already existing')

        else:
            print (self.authorization_error) # create a repository in an organization)

    def create_a_file_in_repo(self,file_name):
        ''' https://developer.github.com/v3/repos/contents/#create-a-file '''
        if self.authorized:
            pass
        else:
            print (self.authorization_error) # create a file in repository




def main():
    token = get_access_token_from_directory()
    username = 'babygame0ver'

    git = Github(token,username)

    git.authorization() # this will help to check the authorization
    git.create_a_repo_in_an_organization('testingbaby','testing-3')

if __name__ == '__main__':
    main()
