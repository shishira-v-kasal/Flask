import sqlite3

def insert_event_data(dataTable, company_name,job_role, event_name, due_date):
    connection = sqlite3.connect('./models/bullsDataBase.db')
    dbrequest = connection.cursor()
    dbrequest.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY,company_name, job_role, event_name, due_date)".format(dataTable))

    connection.commit()
    dbrequest.execute("INSERT INTO {} (company_name, job_role, event_name, due_date) \
                      VALUES (?, ?, ?, ?)".format(dataTable), (company_name, job_role, event_name, due_date))
    connection.commit()
    connection.close()

def get_event_data(dataTable):
   connection = sqlite3.connect('./models/bullsDataBase.db')
   dbrequest = connection.cursor()
   dbrequest.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY,company_name, job_role, event_name, due_date)".format(dataTable))
   connection.commit()
   dbrequest.execute("SELECT * FROM {} ORDER BY due_date".format(dataTable))
   displayData = [{'id': row[0], 'company_name': row[1], 'job_role': row[2], 'event_name': row[3], 'due_date': row[4]} for row in dbrequest.fetchall()]
   connection.close()
   return displayData

def insert_data(dataTable, company_name, job_role, applied_on, location, salary, job_status):
    connection = sqlite3.connect('./models/bullsDataBase.db')
    dbrequest = connection.cursor()
    dbrequest.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY,company_name TEXT,job_role TEXT,\
                      applied_on TEXT,location TEXT,salary NUMERIC,job_status TEXT)".format(dataTable))

    connection.commit()
    dbrequest.execute("INSERT INTO {} (company_name, job_role, applied_on, location, salary, job_status) \
                      VALUES (?, ?, ?, ?, ?, ?)".format(dataTable), (company_name, job_role, applied_on, location, salary, job_status))
    connection.commit()
    connection.close()

def get_data(dataTable):
    connection = sqlite3.connect('./models/bullsDataBase.db')
    dbrequest = connection.cursor()
    dbrequest.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY,company_name, job_role, event_name, due_date)".format(dataTable))
    connection.commit()
    dbrequest.execute("SELECT * FROM {} ORDER BY applied_on".format(dataTable))
    displayData = [{'id': row[0], 'company_name': row[1], 'job_role': row[2], 'applied_on': row[3], 'location': row[4], \
                    'salary': row[5], 'job_status': row[6]} for row in dbrequest.fetchall()]
    connection.close()
    return displayData

def delete_data(dataTable, id):
    connection = sqlite3.connect('./models/bullsDataBase.db')
    dbrequest = connection.cursor()
    dbrequest.execute("DELETE FROM {} WHERE id = ?".format(dataTable), (id,))
    connection.commit()
    connection.close()

def update_data(dataTable, id, dataTableTargetValue):
    if dataTableTargetValue == 'WISHLIST':
        dataTableTarget = "wishlistdata"
    if dataTableTargetValue == 'IN_PROCESS':
        dataTableTarget = "inprocessdata"
    if dataTableTargetValue == 'APPLIED':
        dataTableTarget = "applieddata"
    if dataTableTargetValue == 'OFFER':
        dataTableTarget = "offerdata"
    connection = sqlite3.connect('./models/bullsDataBase.db')
    dbrequest = connection.cursor()
    dbrequest.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY,company_name, job_role, event_name, due_date)".format(dataTable))
    connection.commit()
    dbrequest.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY,company_name TEXT,job_role TEXT,\
                      applied_on TEXT,location TEXT,salary NUMERIC,job_status TEXT)".format(dataTableTarget))

    connection.commit()
    dbrequest.execute("SELECT * FROM {} WHERE id = ?".format(dataTable), (id,))
    data = dbrequest.fetchone()

    if data:
        dbrequest.execute("INSERT INTO {} (company_name, job_role, applied_on, location, salary, job_status) \
                          VALUES (?, ?, ?, ?, ?, ?)".format(dataTableTarget), (data[1], data[2], data[3], data[4], data[5], dataTableTargetValue))
        connection.commit()


        dbrequest.execute("DELETE FROM {} WHERE id = ?".format(dataTable), (id,))
        connection.commit()

    connection.close()