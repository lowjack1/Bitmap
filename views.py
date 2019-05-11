import tornado.ioloop
import tornado.web
import tornado.httpserver
import datetime
from settings import cursor

MaxImage = 12

# Home Page
class MainHandler(tornado.web.RequestHandler):
  low = 0
  high = MaxImage
  data = []

  def get(self):
    query = "SELECT * FROM gallery ORDER BY id"
    cursor.execute(query)
    MainHandler.data = cursor.fetchall()

    MainHandler.low = 0
    MainHandler.high = MaxImage
    new_data = MainHandler.data[MainHandler.low : MainHandler.high]
    self.render("home.html", pics = new_data)

# More Images
class MoreHandler(tornado.web.RequestHandler):
  def get(self):
    MainHandler.low = MainHandler.high
    MainHandler.high = min(len(MainHandler.data), MainHandler.high + 12)
    new_data = MainHandler.data[MainHandler.low : MainHandler.high]
    self.render("response.html", pics = new_data)

# Searchbar
class SearchHandler(tornado.web.RequestHandler):
  def get(self):
    title = self.get_argument('search')
    title = title[0:min(len(title), 3)].capitalize()

    query = "SELECT * FROM gallery WHERE title LIKE \'" + title + "%\'"
    cursor.execute(query)
    MainHandler.data = cursor.fetchall()
    MainHandler.low = 0
    MainHandler.high = min(MaxImage, len(MainHandler.data))
    new_data = MainHandler.data[MainHandler.low : MainHandler.high]
    self.render("response.html", pics = new_data)

# Contact Page
class ContactHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("contact.html")

  def post(self):
    name = self.get_argument('name')
    email = self.get_argument('email')
    subject = self.get_argument('subject')
    message = self.get_argument('message')
    created_on = datetime.datetime.now()
    
    query = "INSERT INTO Feedback (name, subject, email, message, created_on) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, subject, email, message, created_on,))
    connection.commit()
    self.redirect('contact')

# Aboutus Page
class AboutusHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("aboutus.html")