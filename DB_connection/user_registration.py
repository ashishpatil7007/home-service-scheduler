# Import module
import sqlite3
import pandas


def insert_user(name, phone_number, username, password, address,type,service_type):
    # Connecting to sqlite
    conn = sqlite3.connect('Home_service_schedular_DB.db')

    # Creating a cursor object using the
    # cursor() method
    cursor = conn.cursor()

    # Queries to INSERT records.
    cursor.execute('''INSERT INTO USER (NAME,PHONE_NUMBER,ADDRESS,PASSWORD,USERNAME,TYPE) VALUES (
  '{name}',
  '{phone_number}',
  '{address}',
  '{password}',
  '{username}',
  '{type}'
); '''.format(name=name, phone_number=phone_number, address=address, password=password, username=username,
              type=type))
    if type =="employee":
        cursor.execute('''INSERT INTO EMPLOYEE (EMPLOYEE_ID,SERVICE_TYPE) VALUES (
      '{employee_id}',
      '{service_type}'
    ); '''.format(employee_id=cursor.lastrowid,service_type=service_type))

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()

def validate_user(username,password):
    # Connecting to sqlite
    conn = sqlite3.connect('Home_service_schedular_DB.db')

    # Creating a cursor object using the
    # cursor() method
    cursor = conn.cursor()
    df= pandas.read_sql(f'''select * from USER where USERNAME='{username}' and PASSWORD='{password}' '''.format(username=username,password=password),conn)
    print(df)

    if df.empty:
        return False,"",""
    else:
        user_role= df.iloc[0]["TYPE"]
        user_id = int(df.iloc[0]["USER_ID"])
        print(user_role)

        return True,user_role,user_id
def get_employee_list():
    # Connecting to sqlite
    conn = sqlite3.connect('Home_service_schedular_DB.db')

    # Creating a cursor object using the
    # cursor() method
    cursor = conn.cursor()
    df= pandas.read_sql(f'''SELECT USER.NAME || " - "|| EMPLOYEE.SERVICE_TYPE AS EMPLOYEE_NAME,EMPLOYEE.EMPLOYEE_ID FROM USER INNER JOIN EMPLOYEE WHERE USER.USER_ID= EMPLOYEE.EMPLOYEE_ID''',conn)
    print(df)
    if df.empty:
        return []
    else:
        return df.to_dict("records")





