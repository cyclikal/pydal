# -*- coding: utf-8 -*-

DRIVERS = {}

try:
    from google.cloud import firestore
    from google.cloud.firestore_v1.base_query import FieldFilter

    DRIVERS["firestore"] = firestore
    psycopg2_adapt = None
    cx_Oracle = None
    pyodbc = None
    couchdb = None
    is_jdbc = False
except ImportError:
    pass

try:
    from pysqlite2 import dbapi2 as sqlite2

    DRIVERS["sqlite2"] = sqlite2
except ImportError:
    pass

try:
    from sqlite3 import dbapi2 as sqlite3

    DRIVERS["sqlite3"] = sqlite3
except ImportError:
    pass

try:
    import pymysql

    DRIVERS["pymysql"] = pymysql
except ImportError:
    pass

try:
    import snowflake.connector as snowflakeconnector

    DRIVERS["snowflakeconnector"] = snowflakeconnector

except ImportError:
    pass

try:
    import MySQLdb

    DRIVERS["MySQLdb"] = MySQLdb
except ImportError:
    pass

try:
    import mysql.connector as mysqlconnector

    DRIVERS["mysqlconnector"] = mysqlconnector
except ImportError:
    pass

try:
    import psycopg2
    from psycopg2.extensions import adapt as psycopg2_adapt

    DRIVERS["psycopg2"] = psycopg2
except ImportError:
    psycopg2_adapt = None

try:
    import cx_Oracle

    DRIVERS["cx_Oracle"] = cx_Oracle
except ImportError:
    cx_Oracle = None

try:
    import pyodbc

    DRIVERS["pyodbc"] = pyodbc
    # DRIVERS.append('DB2(pyodbc)')
    # DRIVERS.append('Teradata(pyodbc)')
    # DRIVERS.append('Ingres(pyodbc)')
except ImportError:
    try:
        import pypyodbc as pyodbc

        DRIVERS["pyodbc"] = pyodbc
    except ImportError:
        pyodbc = None

try:
    import ibm_db_dbi

    DRIVERS["ibm_db_dbi"] = ibm_db_dbi
except ImportError:
    pass
try:
    import Sybase

    DRIVERS["Sybase"] = Sybase
except ImportError:
    pass

try:
    import kinterbasdb

    DRIVERS["kinterbasdb"] = kinterbasdb
    # DRIVERS.append('Firebird(kinterbasdb)')
except ImportError:
    pass

try:
    import fdb

    DRIVERS["fdb"] = fdb
except ImportError:
    pass

try:
    import firebirdsql

    DRIVERS["firebirdsql"] = firebirdsql
except ImportError:
    pass

try:
    import informixdb

    # LOGGER.warning('Informix support is experimental')
    DRIVERS["informixdb"] = informixdb
except ImportError:
    pass

try:
    import sapdb

    DRIVERS["sapdb"] = sapdb
    # LOGGER.warning('SAPDB support is experimental')
except ImportError:
    pass

try:
    import cubriddb

    DRIVERS["cubriddb"] = cubriddb
    # LOGGER.warning('Cubrid support is experimental')
except ImportError:
    pass

try:
    import java.sql
    from com.ziclix.python.sql import zxJDBC

    # Try sqlite jdbc driver from http://www.zentus.com/sqlitejdbc/
    from org.sqlite import JDBC  # required by java.sql; ensure we have it

    zxJDBC_sqlite = java.sql.DriverManager
    DRIVERS["zxJDBC"] = zxJDBC
    # DRIVERS.append('SQLite(zxJDBC)')
    # LOGGER.warning('zxJDBC support is experimental')
    is_jdbc = True
except ImportError:
    is_jdbc = False

try:
    import couchdb

    DRIVERS["couchdb"] = couchdb
except ImportError:
    couchdb = None

try:
    import pymongo

    DRIVERS["pymongo"] = pymongo
except:
    pass

try:
    import imaplib

    DRIVERS["imaplib"] = imaplib
except:
    pass

try:
    import pytds

    DRIVERS["pytds"] = pytds
except:
    pass
