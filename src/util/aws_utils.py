import boto3
from util.variables import logger
from util.utils import CONFIG_DIR
from util.config_utils import get_aws_env


def connect_s3():
    logger.info('Connecting to AWS S3')
    profile_name = get_aws_env()
    session = boto3.Session(profile_name=profile_name)
    return session.client('s3')


def connect_sns():
    logger.info('Connecting to AWS SNS')
    profile_name, region_name = get_aws_env(config_dir=CONFIG_DIR, section='AWS')
    session = boto3.Session(profile_name=profile_name, region_name=region_name)
    return session.client('sns')


def connect_rekon():
    logger.info('Connecting to AWS rekognition')
    profile_name, region_name = get_aws_env(config_dir=CONFIG_DIR, section='AWS')
    session = boto3.Session(profile_name=profile_name, region_name=region_name)
    return session.client('rekognition')


def connect_translate():
    logger.info('Connecting to AWS translate')
    profile_name, region_name = get_aws_env(config_dir=CONFIG_DIR, section='AWS')
    session = boto3.Session(profile_name=profile_name, region_name=region_name)
    return session.client('translate')


def connect_comprehend():
    logger.info('Connecting to AWS comprehend')
    profile_name, region_name = get_aws_env(config_dir=CONFIG_DIR, section='AWS')
    session = boto3.Session(profile_name=profile_name, region_name=region_name)
    return session.client('comprehend')
