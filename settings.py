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

def createDbCursor():
  connection = psycopg2.connect(
    database = "bitmap", 
    user = "light", 
    password = "H@11542$9", 
    host = "localhost", 
    port = 5432
  )
  return connection.cursor()


dirname = os.path.dirname(__file__)
static_path = os.path.join(dirname, 'static')
template_path = os.path.join(dirname, 'templates')
port = openPort()
cursor = createDbCursor()


