import http.server
class HTTPParser(BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.requestline)
  
		