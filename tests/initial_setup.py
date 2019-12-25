import logging
import json
import os

def initial_config_setup():
    ''' Setting up config file path env'''
    git_config_path = r'C:\Users\baby\Google Drive\meta-data\github\blackhathack3r'
    os.environ['gitpy_path'] = git_config_path
    config_file = os.environ['gitpy_path'] + '\config.json'
    try:
        with open(config_file,'r') as f:
            configuration_data = json.loads(f.read())
    except FileNotFoundError: # if not found go to travis environment variables
        config_data = {'username' : '', 'token' : ''}
        username = os.environ['username']
        token = os.environ['token']
        config_data['username'] = username
        config_data['token'] = token
        return config_data
    return configuration_data
