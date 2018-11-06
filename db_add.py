#!/usr/bin/env python3

import db_ops
import json
import hashlib
import datetime

def parse_job_listing(job_post_file):
    # Parse document as JSON
    try:
        test_stream = open(job_post_file)
        data = test_stream.read().replace('\n', ' ')
        parsed_json = json.loads(data)

        list_post = []
        # Populate record for insertion to database
        for entry in parsed_json["listing"]:
            job_post = []

            # NOTE: Order of entries depends on schema
            job_post.append(entry['Company'])
            job_post.append(entry['Position'])
            job_post.append(entry['Area'])
            job_post.append(entry['Date of Post'])
            job_post.append(entry['Job Listing URL'])
            job_post.append(entry['Company Website'])
            job_post.append(entry['Location'])
            job_post.append(str(datetime.date.today()))

            # Compte hash based on first 4 fields
            hashcalc = hashlib.sha256()
            for ctr in range(0, 4):
                hashcalc.update(job_post[0].encode('utf-8'))
            job_post.append(hashcalc.digest().hex())

            list_post.append(job_post)
    except Exception as e:
        raise e
        return None
    else:
        return list_post

def parse_application_list(job_application_file):
    # Parse document as JSON
    try:
        test_stream = open(job_application_file)
        data = test_stream.read().replace('\n', ' ')
        parsed_json = json.loads(data)

        list_app = []
        # Populate record for insertion to database
        for entry in parsed_json["listing"]:
            job_post = []

            # NOTE: Order of entries depends on schema
            # NOTE: Job listing URL will be replaced by Job ID
            job_post.append(entry['Job Listing URL'])
            job_post.append(entry['Date of Application'])
            job_post.append(entry['Status'])
            job_post.append(entry['Referral'])
            job_post.append(entry['Confidence'])
            job_post.append(entry['Comment'])

            # Compte hash based on 2nd and 3rd fields
            hashcalc = hashlib.sha256()
            for ctr in range(1, 3):
                hashcalc.update(job_post[0].encode('utf-8'))
            job_post.append(hashcalc.digest().hex())

            list_app.append(job_post)
    except Exception as e:
        raise e
        return None
    else:
        return list_app

def get_job_ID(db_con, table_name, application_entry):
    job_post_url = application_entry[0]
    job_id_field = 'Job ID'
    search_field = 'Job Listing URL'

    table_name = 'Job Opening'
    job_id_query = 'Select ' + '"' + job_id_field + '" from '
    job_id_query += '"' + table_name + '" where ' + '"' + search_field + '" = '
    job_id_query += '"' + job_post_url + '"'
    job_id_record = db_ops.getRecord(db_con, job_id_query)
    application_entry[0] = job_id_record[0][0]

if __name__ == "__main__":
    # Open database
    db_con = db_ops.openDB('job.db')

    # Add data for job posting
    list_post = parse_job_listing('posting.list')
    table_name = 'Job Opening'
    for post in list_post:
        db_ops.addRecord(db_con, table_name, post)

    # Add data for job application
    app_list = parse_application_list('application.list')
    # TODO: Find an easier way to get Job ID; adding URL is prone to error
    table_name = 'Job Application'
    for app in app_list:
        get_job_ID(db_con, table_name, app)
        db_ops.addRecord(db_con, table_name, app)

    # Close database
    db_ops.closeDB(db_con)
