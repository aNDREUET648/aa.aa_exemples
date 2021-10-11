import socketserver
import threading

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
        daemon_threads = True
        allow_reuse_address = True
        
class CapitalizeHandler(socketserver.StreamRequestHandler):
        def handle(self):
            client = f'{self.client_address} on {threading.currentThread().getName()}'
            print(f'Connected: {client}')
            while True:
                data = self.rfile.readline()
                if not data:
                    break
                self.wfile.write(data.decode('utf-8').upper().encode('utf-8'))
            print(f'Closed: {client}')
            
with ThreadedTCPServer(('', 9999), CapitalizeHandler) as server:
    print(f'The capitalization server is running...')
    server.serve_forever()