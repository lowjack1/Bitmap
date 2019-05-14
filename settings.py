import os
import socket
import psycopg2
import psycopg2.extras
import json
import sys

def portInUse(port):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    return sock.connect_ex(('localhost', port)) == 0

def openPort():
  for port in range(8000, 9000):
    if not portInUse(port):
      return port


def tableExist(tableName, cursor):
  query = "SELECT EXISTS(SELECT * FROM information_schema.tables where table_name=%s)"
  cursor.execute(query, (tableName,))
  return cursor.fetchone()[0]

def createDbCursor():
  if not os.path.exists('credentials.json') or len(sys.argv) > 1:
    info = {
      'database': input("enter database name: "),
      'username': input("username for database: "),
      'password': input("password: ")
    }
    with open("credentials.json", 'w') as file:
      json.dump(info, file, indent = 4)

  try:
    file = open('credentials.json', 'r')
    info = json.load(file)
    file.close() 
    connection = psycopg2.connect(
      database = info['database'], 
      user = info['username'], 
      password = info['password'], 
      host = "localhost", 
      port = 5432
    )
    cursor = connection.cursor()

    # Create table Gallery if does not exist
    if not tableExist('gallery', cursor):
      query = """CREATE TABLE gallery(
        id SERIAL PRIMARY KEY, 
        imgpath TEXT NOT NULL, 
        title VARCHAR(50) NOT NULL
      )"""
      cursor.execute(query)
      data = open('data/data.csv', 'r')      
      copy = "COPY gallery FROM STDIN WITH CSV HEADER DELIMITER AS ','"
      cursor.copy_expert(sql=copy, file=data)
      connection.commit()

    # Create table Feedback if does not exist
    if not tableExist('feedback', cursor):
      query = """CREATE TABLE feedback(
        id SERIAL PRIMARY KEY, 
        name VARCHAR(50) NOT NULL,
        subject Text NOT NULL,
        email VARCHAR(100) NOT NULL,
        message TEXT NOT NULL,
        created_on TimeStamp NOT NULL
      )"""
      cursor.execute(query)
      connection.commit()

    return cursor
  except json.decoder.JSONDecodeError as e:
    print("resync database, it might have incomplete information.")
    sys.exit(0)
  except psycopg2.OperationalError as e:
    print(str(e))
    sys.exit(0)

dirname = os.path.dirname(__file__)
static_path = os.path.join(dirname, 'static')
template_path = os.path.join(dirname, 'templates')
port = openPort()
cursor = createDbCursor()