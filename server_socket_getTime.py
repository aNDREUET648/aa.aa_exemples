import socketserver

from datetime import datetime


class DateHandler(socketserver.StreamRequestHandler):
    def handle(self):
        date = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p\n")
        self.wfile.write(date.encode("utf-8"))



with socketserver.TCPServer(('', 5088), DateHandler) as server:  # file access structure in python a ver si puedo hacer algo con ello
    print('The date server is now running yet...')
    server.serve_forever()
