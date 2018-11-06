#!/usr/bin/env python3

import sqlite3 as lite
import hashlib

def openDB(db_name):
    try:
        db_con = lite.connect(db_name)
    except Exception as e:
        raise e
        return None
    else:
        return db_con

def closeDB(db_con):
    db_con.commit()
    return db_con.close()

def createTable(db_con, table_name, table_schema):
    try:
        type_list = ['VARCHAR', 'TEXT', 'INT', 'DATE']
        attr = ''

        createStr = 'CREATE TABLE' + ' "' + table_name + '"'
        schema = '('
        for x,y,z in table_schema:
            if y.upper() in type_list:
                if z == 'p':
                    attr = 'PRIMARY KEY'
                if z == 'n':
                    attr = 'NOT NULL'
                if z == 'u':
                    attr = 'UNIQUE'
                schema += '"' + x + '" ' + y.upper() + ' ' + attr + ' ' + ','
        if schema[-1] == ',':
            schema = schema[:-1] + ')'
        else:
            raise Exception('Invalid table schema')

        db_cur = db_con.cursor()
        db_cur.execute(createStr + " " + schema)
    except Exception as e:
        raise e
        return None
    else:
        pass

def addRecord(db_con, table, data):
    db_cur = db_con.cursor()
    hashcalc = hashlib.sha256()

    insert_query = "INSERT INTO" + ' "' + table + '" ' + " VALUES "
    formatted_data = '('

    for datum in data:
        formatted_data += '"' + datum + '"' + ','

    if formatted_data[-1] == ',':
        formatted_data =  formatted_data[:-1] + ')'

    db_cur.execute(insert_query + formatted_data)

def getRecord(db_con, query):
    try:
        db_cur = db_con.cursor()
        db_cur.execute(query)
        db_data = db_cur.fetchall()
    except Exception as e:
        raise e
        return None
    else:
        return db_data
