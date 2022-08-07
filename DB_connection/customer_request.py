# Import module
import sqlite3
import pandas


def insert_request(employee_id,customer_id,is_complete,created_date,request_time,service_type):
    # Connecting to sqlite
    conn = sqlite3.connect('Home_service_schedular_DB.db')

    # Creating a cursor object using the
    # cursor() method
    cursor = conn.cursor()

    # Queries to INSERT records.
    cursor.execute('''INSERT INTO REQUEST (EMPLOYEE_ID,CUSTOMER_ID,IS_COMPLETE,CREATED_DATE,REQUEST_TIME,SERVICE_TYPE) VALUES (
  '{employee_id}',
  '{customer_id}',
  '{is_complete}',
  '{created_date}',
  '{request_time}',
  '{service_type}',
   ); 
'''.format(employee_id=employee_id,customer_id=customer_id,is_complete=is_complete, created_date=created_date,request_time=request_time,service_type=service_type))

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()

def get_request(customer_id):
    # Connecting to sqlite
    conn = sqlite3.connect('Home_service_schedular_DB.db')

    # Creating a cursor object using the
    # cursor() method
    cursor = conn.cursor()
    request_df=pandas.read_sql("SELECT * FROM REQUEST inner join USER ON REQUEST.customer_id= USER.USER_ID where REQUEST.customer_id={customer_id} ".format(customer_id=customer_id),con=conn)
    print(request_df)
    if request_df.empty:
        return []
    else:
        return request_df.to_dict("records")

def get_request_employee(employee_id):
    # Connecting to sqlite
    conn = sqlite3.connect('Home_service_schedular_DB.db')

    # Creating a cursor object using the
    # cursor() method
    cursor = conn.cursor()
    request_df=pandas.read_sql("SELECT * FROM REQUEST INNER JOIN USER ON REQUEST.EMPLOYEE_ID= USER.user_id WHERE REQUEST.employee_id={employee_id}".format(employee_id=employee_id),con=conn)
    print(request_df)
    if request_df.empty:
        return []
    else:
        return request_df.to_dict("records")

