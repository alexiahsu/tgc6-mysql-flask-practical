# repeated steps to connect python programme to mysql database

import pymysql
import os
from dotenv import load_dotenv

# load in the environment variables
load_dotenv()

# create the database connection


def get_conn(host, user, password, database):
    conn = pymysql.connect(host=host,
                           user=user,
                           password=password,
                           database=database)
    return conn

# Create the cursor


def get_cursor(conn):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return cursor
