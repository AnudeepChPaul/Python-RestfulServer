from http.server import BaseHTTPRequestHandler, HTTPServer
from servers.RestfulServerHandler import RestfulServerHandler
from configs.ServerConfig import get_server_config

def start_server(port=None):
    server_config = get_server_config()
    HOST, PORT = server_config["HOST"], server_config["PORT"]

    httpd = HTTPServer((HOST, PORT), RestfulServerHandler)

    print('Starting httpd... info: host={host}, port={port}'.format(host=HOST, port=PORT))
    httpd.serve_forever()

if __name__ == "__main__":
    start_server()
