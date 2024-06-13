import configparser
import os


def read_config_file(config_dir, section):
    config = configparser.RawConfigParser()
    config.read(config_dir)
    items_section = dict(config.items(section))
    return items_section


def get_mysql_config(config_dir, section):
    settings = read_config_file(config_dir=config_dir, section=section)
    host = settings['host']
    user = settings['user']
    password = settings['password']
    database = settings['database']
    return host, user, password, database


def get_connection_config(config_dir, section):
    settings = read_config_file(config_dir=config_dir, section=section)
    host = settings['host']
    port = int(settings['port'])
    return host, port


def get_sqlite_file_env():
    sqlite_db = os.environ['sqlite_db']
    return sqlite_db


def get_arduino_env():
    host = os.environ['arduino_host']
    user = os.environ['arduino_user']
    return host, user


def get_mysql_env():
    host = os.environ['mysql_host']
    user = os.environ['mysql_user']
    password = os.environ['mysql_password']
    database = os.environ['mysql_database']
    return host, user, password, database


def get_postgres_env():
    host = os.environ['postgres_host']
    user = os.environ['postgres_user']
    password = os.environ['postgres_password']
    database = os.environ['postgres_database']
    return host, user, password, database


def get_sockets_env():
    host = os.environ['socket_host']
    user = os.environ['socket_user']
    return host, user


def get_mqtt_env():
    host = os.environ['mqtt_host']
    port = int(os.environ['mqtt_port'])
    client = os.environ['mqtt_client']
    return host, port, client


def get_aws_env():
    profile_name = os.environ['aws_profile_name']
    region_name = os.environ['aws_region_name']
    return profile_name, region_name
