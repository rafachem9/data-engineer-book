import os
import logging
import datetime
from util.utils import PROJECT_DIR


def create_log_file(logs_name):
    LOG_DIR = os.path.join(PROJECT_DIR, 'logs')
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    timestamp = '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now())
    log_file_dir = os.path.join(LOG_DIR, f"{timestamp}.log")

    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s-%(pathname)s:%(lineno)s-%(levelname)s-%(message)s",
                        handlers=[logging.FileHandler(log_file_dir),
                                  logging.StreamHandler()])

    logger = logging.getLogger(logs_name)
    return logger
