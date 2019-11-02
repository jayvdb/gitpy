[1mdiff --git a/tests/test_repos.py b/tests/test_repos.py[m
[1mindex d59efe9..a3ff327 100644[m
[1m--- a/tests/test_repos.py[m
[1m+++ b/tests/test_repos.py[m
[36m@@ -73,7 +73,7 @@[m [mclass TestRepository(unittest.TestCase):[m
     def test_list_all_public_repositories(self):[m
         self.logger.info('executing')[m
         msg = ''[m
[31m-        required_link = self.repository_object.gitpy_object.developer_api + '/repositories'[m
[32m+[m[32m        required_link = self.repository_object.gitpy_object.developer_api + '/users/{}/repos'.format(self.repository_object.gitpy_object.username)[m
         try:[m
             session = requests.session()[m
             response = requests.get(required_link)[m
[36m@@ -115,21 +115,21 @@[m [mclass TestRepository(unittest.TestCase):[m
     def test_create_public_repository(self):[m
         self.logger.info('executing')[m
         repo_name = 'repository-three-public'[m
[31m-        self.repository_object.create_public_repository(repo_name)[m
         required_link = self.repository_object.gitpy_object.developer_api+'/repos/{}/{}'.format(self.repository_object.username,repo_name)[m
         response = requests.get(required_link)[m
[32m+[m[32m        self.assertEqual(response.status_code,403) # not found repository not created yet[m
[32m+[m[32m        self.repository_object.create_public_repository(repo_name) #  created repository[m
[32m+[m[32m        response = requests.get(required_link)[m
         self.assertEqual(response.status_code,200) # found create repository[m
[31m-        response = requests.get(required_link+'s')[m
[31m-        self.assertEqual(response.status_code,404) # not found repository[m
         self.logger.info('completed')[m
 [m
     def test_create_private_repository(self):[m
         self.logger.info('executing')[m
         repo_name = 'repository-four-private'[m
[31m-        self.repository_object.create_private_repository(repo_name)[m
         required_link = self.repository_object.gitpy_object.developer_api+'/repos/{}/{}'.format(self.repository_object.username,repo_name)[m
         response = requests.get(required_link,headers=self.repository_object.gitpy_object.authorization_data)[m
[32m+[m[32m        self.assertEqual(response.status_code,404) # not found repository not created yet[m
[32m+[m[32m        self.repository_object.create_private_repository(repo_name)[m
[32m+[m[32m        response = requests.get(required_link,headers=self.repository_object.gitpy_object.authorization_data)[m
         self.assertEqual(response.status_code,200) # found create repository[m
[31m-        response = requests.get(required_link+'s')[m
[31m-        self.assertEqual(response.status_code,404) # not found repository[m
         self.logger.info('completed')[m
