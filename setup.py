import configparser
import os

def create_config():
    config_file_path = "./config.conf"
    check_if_config_file_exists = os.path.exists(config_file_path)

    if check_if_config_file_exists is False:
        config = configparser.ConfigParser()
        config['path'] = {'file_path' : ""}
        config['exceptions'] = {}

        with open('config.conf','w') as config_file:
            config.write(config_file)

