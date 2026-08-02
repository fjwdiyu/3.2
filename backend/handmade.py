from http.server import BaseHTTPRequestHandler, HTTPServer
import json

profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"{self.command} {self.path} from {self.client_address[0]}")
        if self.path == "/api/profile":
            body = json.dumps(profile, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

print("后端已启动：http://localhost:8000/api/profile")
HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
