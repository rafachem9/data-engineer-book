import os

os.chdir("../")
PROJECT_DIR = os.getcwd()
DATA_DIR = os.path.join(PROJECT_DIR, 'data')
DATABASE_DIR = os.path.join(PROJECT_DIR, 'database')
CONFIG_DIR = os.path.join(PROJECT_DIR, 'settings', 'settings.cfg')
SQL_DIR = os.path.join(PROJECT_DIR, 'sql')



