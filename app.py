# app.py
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Respond with a 200 OK status
        self.send_response(200)
        # Set the content type of the response
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # Write the response body
        self.wfile.write(b'Hello, this is a simple Python API!')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    # Define the server address and port
    server_address = ('', 8080)  # Port 8080 inside the container
    httpd = server_class(server_address, handler_class)
    print('Starting HTTP server...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()