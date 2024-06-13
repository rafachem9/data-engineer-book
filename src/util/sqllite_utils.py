import os
import sqlite3
import csv
import pandas as pd
from util.utils import DATABASE_DIR, DATA_DIR
from util.variables import logger
from util.config_utils import get_mysql_env
import mysql.connector as mysql


def connect_sqlite(data_base_name):
    database_file = os.path.join(DATABASE_DIR, data_base_name)
    connector = sqlite3.connect(database_file)
    return connector


def connector_mysql():
    host, user, password, database = get_mysql_env()
    connector = mysql.connect(host=host, user=user, passwd=password, database=database)
    return connector


def execute_query(dabase_name, query_dir):
    # table_name = query_dir.split('\\')[-1]
    # logger.info(f'Creating Tables {table_name}')
    connector = connect_sqlite(dabase_name)
    micursor = connector.cursor()
    with open(query_dir) as my_file:
        sql_query = my_file.read()
    try:
        micursor.execute(sql_query)
        connector.commit()
    except Exception as e:
        logger.error(str(e))
    connector.close()


def execute_insert_df(df, dabase_name, table):
    logger.info(f'Inserting data in table: {table}')
    connector = connect_sqlite(dabase_name)
    mycursor = connector.cursor()
    columns_names = df.columns
    csv_name = os.path.join(DATA_DIR, f'{table}.csv')
    df.to_csv(csv_name)
    with open(csv_name, 'r', encoding="utf8") as fin:
        dr = csv.reader(fin)  # comma is default delimiter
        # Quitamos los nombres de las columnas
        next(dr)
        to_db = [tuple(row) for row in dr]
    object = ", ?"
    query = f"INSERT INTO {table} VALUES(?{object*(len(columns_names))}, datetime('now', 'localtime'), datetime('now', 'localtime'))"
    try:
        mycursor.executemany(query, to_db)
        connector.commit()
    except Exception as e:
        logger.error(str(e))
    connector.close()
    return to_db


def execute_select_query(dabase_name, query_dir):
    table_name = query_dir.split('\\')[-1]
    logger.info(f'Selecting Table {table_name}')
    connector = connect_sqlite(dabase_name)
    micursor = connector.cursor()
    with open(query_dir) as my_file:
        sql_query = my_file.read()
    try:
        table = micursor.execute(sql_query)
        result = micursor.fetchall()
    except Exception as e:
        logger.error(str(e))
        result = None
        table = None
    connector.close()
    column_names = [column[0] for column in table.description]
    return pd.DataFrame(result, columns=column_names)
