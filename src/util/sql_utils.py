import os
import sqlite3
import csv
import psycopg2
import pandas as pd
from util.utils import DATABASE_DIR, DATA_DIR
from util.variables import logger
from util.config_utils import get_mysql_env, get_postgres_env
import mysql.connector as mysql


def connect_sqlite(data_base_name):
    database_file = os.path.join(DATABASE_DIR, data_base_name)
    connector = sqlite3.connect(database_file)
    return connector


def connector_mysql():
    host, user, password, database = get_mysql_env()
    connector = mysql.connect(host=host, user=user, passwd=password, database=database)
    return connector


def connect_postgres():
    host, user, password, database = get_postgres_env()
    connector = psycopg2.connect(host=host, database=database, user=user, password=password)
    return connector


def execute_query(connector, query_dir):
    # table_name = query_dir.split('\\')[-1]
    # logger.info(f'Creating Tables {table_name}')
    micursor = connector.cursor()
    with open(query_dir) as my_file:
        sql_query = my_file.read()
    logger.info(sql_query)
    try:
        micursor.execute(sql_query)
        connector.commit()
    except Exception as e:
        logger.error(str(e))
    connector.close()


def execute_insert_df(connector, df, table):
    logger.info(f'Inserting data in table: {table}')
    mycursor = connector.cursor()
    columns_names = df.columns
    table_name = table.split('.')[-1]
    csv_name = os.path.join(DATA_DIR, f'stg_{table_name}.csv')
    df.to_csv(csv_name)
    with open(csv_name, 'r', encoding="utf8") as fin:
        dr = csv.reader(fin)  # comma is default delimiter
        # Quitamos los nombres de las columnas
        next(dr)
        to_db = [tuple(row)[1:] for row in dr]
    os.remove(csv_name)
    object = ", %s"
    names = ', '.join(columns_names)
    query = f'INSERT INTO {table} ({names}) VALUES(%s{object*(len(columns_names)-1)})'
    try:
        mycursor.executemany(query, to_db)
        connector.commit()
    except Exception as e:
        logger.error(str(e))
    connector.close()
    return to_db


def execute_select_query(connector, query_dir):
    table_name = query_dir.split('\\')[-1]
    logger.info(f'Selecting Table {table_name}')
    cursor = connector.cursor()
    with open(query_dir) as my_file:
        sql_query = my_file.read()
    try:
        logger.info(sql_query)
        cursor.execute(sql_query)
        result = cursor.fetchall()
        column_names = [column[0] for column in cursor.description]
        df = pd.DataFrame(result, columns=column_names)
        logger.info(f'Query executed successfully. Rows retrieved: {df.shape[0]}')
    except Exception as e:
        logger.error(str(e))
        df = pd.DataFrame()
    connector.close()
    return df
