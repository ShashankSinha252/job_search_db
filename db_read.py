#!/usr/bin/env python3

import db_ops

def get_record_data(db_con, table_name):
    try:
        search_query = "SELECT * from " + '"' + table_name + '"'
        db_data = db_ops.getRecord(db_con, search_query)

        if db_data == None:
            print("No record found")
        else:
            for data in db_data:
                print(str(data))
    except Exception as e:
        raise e

if __name__ == "__main__":
    # Open database #
    db_con = db_ops.openDB('job.db')

    get_record_data(db_con, 'Job Opening')
    get_record_data(db_con, 'Job Application')
    # Fetch data #

    # Close database #
    db_ops.closeDB(db_con)
