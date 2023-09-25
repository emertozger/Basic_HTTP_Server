from http.server import HTTPServer, BaseHTTPRequestHandler
from http.client import HTTPConnection

HOST = "192.168.0.31"
PORT = 1234

class mertHttp(BaseHTTPRequestHandler):

    def do_GET(self): #get request'e nasil cevap verecegimizi tanimlayan fonksiyon
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Erdem Mert Ozger!</h1></body></html>","utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(bytes("This is a POST request..","utf-8"))


server = HTTPServer((HOST,PORT),mertHttp)
print("Server is running..")

server.serve_forever()
server.server_close()
print("Server is closed..")

