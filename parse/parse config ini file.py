import configparser

# parse config file
config = configparser.RawConfigParser()
config.read('config.ini')

a = config['RECURSIVE=Yes']['type_dir']
