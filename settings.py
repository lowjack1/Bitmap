import os
import socket
import psycopg2
import psycopg2.extras

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
  if not os.path.exists('db_credentials.txt') or os.stat('db_credentials.txt').st_size == 0:
    file = open('db_credentials.txt', 'w')
    db_name = input("enter database name: ")
    user = input("username for database: ")
    password = input("password: ")
    file.write(db_name + " " + user + " " + password);
    file.close()

  file = open('db_credentials.txt', 'r')
  db_credns = list(file.readline().strip().split())
  file.close() 
  connection = psycopg2.connect(
    database = db_credns[0], 
    user = db_credns[1], 
    password = db_credns[2], 
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
    cursor.copy_from(data, 'gallery', columns=('id', 'imgpath', 'title'), sep = ',')
    connection.commit()

  # Create table Feedback if does not exist
  if not tableExist('feedback', cursor):
    query = """CREATE TABLE feedback(
      id SERIAL PRIMARY KEY, 
      name VARCHAR(50) NOT NULL,
      subject Text NOT NULL,
      email VARCHAR(100) NOT NULL,
      messaeg TEXT NOT NULL,
      created_on TimeStamp NOT NULL
    )"""
    cursor.execute(query)
    connection.commit()

  return cursor

dirname = os.path.dirname(__file__)
static_path = os.path.join(dirname, 'static')
template_path = os.path.join(dirname, 'templates')
port = openPort()
cursor = createDbCursor()


