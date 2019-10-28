__author__ = "lowjack"

import views
import tornado.ioloop
import tornado.web
import tornado.httpserver
from settings import port, static_path, template_path 

class Application(tornado.web.Application):
  def __init__(self):
    urls = [
      (r"/", views.MainHandler),
      (r"/home", views.MainHandler),
      (r"/contact", views.ContactHandler),
      (r"/about", views.AboutusHandler),
      (r"/more", views.MoreHandler),
      (r"/search", views.SearchHandler),
    ]
    setting = {
      "template_path": template_path,
      "static_path": static_path,
      "xsrf_cookies": True
    }
    tornado.web.Application.__init__(self, urls, **setting)
    
def main():
  app = Application()
  http_server = tornado.httpserver.HTTPServer(app)
  http_server.listen(port)
  print("Starting development server at http://127.0.0.1:%d" %(port))
  print("Quit the server with CONTROL-C.")

  try:
    tornado.ioloop.IOLoop.instance().start()
  except KeyboardInterrupt:
    print(" Server Closed.")

if __name__ == "__main__":
  main()
