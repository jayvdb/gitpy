## Configuration Steps for Gitpy (Before Installation : 2 minutes)

Gitpy works on Username & Token of a GitHub Account. So it requires few configuration before Installation.

For configuration we have two methods available.

## Download gitpy

```
# git clone https://github.com/babygame0ver/gitpy.git && cd gitpy

```

### Method 1. Using Configuration from Local File.

- Create a File with username and token & name it config.json

![alt text](tests/after_install/media/file_config/1-config_file.PNG)

- Copy the absolute path of file from file system

![alt text](tests/after_install/media/file_config/2-config_file_path.png)

- Change the git_config_path variable in gitpy/core/auth.py

![alt text](tests/after_install/media/file_config/3-config_file_path_in_gitpy.PNG)

---

2. Creating Environment variable 'username' & 'token' in your machine.

- Obtain Access token from your GitHub Account.

- Add Username & Token to Environment variables in your Machine.
