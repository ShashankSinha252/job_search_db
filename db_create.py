#!/usr/bin/env python3

import db_ops

# Open database #
db_con = db_ops.openDB('job.db')

# Create required table #
db_cur = db_con.cursor()

schema_opening = [('Company', 'VARCHAR', 'n'),
                  ('Position', 'VARCHAR', 'n'),
                  ('Area', 'TEXT', 'n'),
                  ('Date of Posting', 'DATE', 'n'),
                  ('Job Listing URL', 'VARCHAR', None),
                  ('Company Website', 'VARCHAR', None),
                  ('Location', 'VARCHAR', None),
                  ('Date of Entry', 'DATE', 'n'),
                  ('Job ID', 'VARCHAR', 'p')]

schema_application = [('Job ID', 'VARCHAR', 'p'),
                      ('Date of Application', 'DATE', 'n'),
                      ('Status', 'TEXT', 'n'),
                      ('Referral', 'VARCHAR', None),
                      ('Confidence', 'VARCHAR', None),
                      ('Comment', 'VARCHAR', None),
                      ('Application ID', 'VARCHAR', 'n')]

# TODO: Create schema for all tables
tables = [('Job Opening', schema_opening),
          ('Job Application', schema_application)]

#table_name = [('Job Opening', schema_opening),
#              ('Job Application', schema_application),
#              ('Job Offer', schema_offer)]

for name, schema in tables:
    db_ops.createTable(db_con, name, schema)

# Close database #
db_ops.closeDB(db_con)
