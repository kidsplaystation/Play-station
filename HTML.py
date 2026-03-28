from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse
import os

# ----- CONFIG -----
PORT = 8000
# Folder where your HTML, CSS, JS files are stored
DIRECTORY = os.path.join(os.path.dirname(__file__), "www")

# ----- CUSTOM HANDLER -----
class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        parsed_path = urlparse(self.path)

        # ----- API ENDPOINT -----
        if parsed_path.path == "/api/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {
                "name": "Amarn",
                "assignment": 20,
                "status": "success",
                "tasks": [
                    "Play games",
                    "Check calendar",
                    "Complete your to-do list"
                ]
            }
            self.wfile.write(json.dumps(response).encode("utf-8"))

        # ----- SERVE STATIC FILES -----
        else:
            super().do_GET()

# ----- RUN SERVER -----
if __name__ == "__main__":
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, CustomHandler)
    print(f"✅ Server running at http://localhost:{PORT}")
    print(f"📁 Serving files from: {DIRECTORY}")
    httpd.serve_forever()