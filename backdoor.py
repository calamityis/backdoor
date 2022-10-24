import os
import SocketServer
import sys

host, port = '0.0.0.0', 33336
path = ""
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def readfile(self):
        f = open(path,"rb").read()
        self.request.sendall(f)
    def handle(self):
        self.request.settimeout(120)        
        self.readfile()



def main():
	server = ThreadedTCPServer((host, port), ThreadedTCPRequestHandler)
	server_thread = threading.Thread(target=server.serve_forever)
	server_thread.daemon = True
	server_thread.start()
	print "Server loop running in thread:", server_thread.name
	server_thread.join()

if __name__=='__main__':
    main()
