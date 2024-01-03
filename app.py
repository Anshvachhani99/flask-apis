import http.server
import socketserver

# Set the port you want to use
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, this is a custom endpoint!')
        else:
            # For any other requests, use the default handler
            super().do_GET()

# Set the port you want to use
PORT = 8080

# Create the server with the specified port and custom handler
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    # Start the server
    httpd.serve_forever()
