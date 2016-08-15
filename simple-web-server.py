#!/usr/bin/env python
#
# Written by Priyend Somaroo, 08 Aug 2016
#
# Simple Webserver using minimal Python libraries.
# Will accept POST data and if it is in JSON format will display it as formatted data.
#
# Usage:
#    ./simple-web-server.py [<port>]
#
# Send a GET request:
#    curl http://localhost
#
# Send a HEAD request:
#    curl -I http://localhost
#
# Send a POST request:
#    curl -d "foo=bar&bin=baz" http://localhost
#    curl -d "{\"foo\":\"bar\",\"bin\":\"baz\",\"Number\":123}" http://localhost
#
# References : 
#   - Base is cloned from https://gist.github.com/2219997.git
#   - http://stackoverflow.com/questions/17193008/python-read-multiline-post-data
#   - http://stackoverflow.com/a/20725965
#   - http://stackoverflow.com/questions/5508509/how-do-i-check-if-a-string-is-valid-json-in-python
#   - https://wiki.python.org/moin/HandlingExceptions
#   - https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/
#  
#  Rev 1.0, 08 Aug 2016:
#  - First revision
#  
#  Rev 2.0, 15 Aug 2016:
#  - Added retrieving of path in GET and POST requests


from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        path = self.path
        result = "<html><body><h1>Hooray it works!</h1><p>Path = {}</p></body></html>".format(path)
        self.wfile.write(result)

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Display sent data to console
        
        path = self.path
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Check if it is JSON data
        isJson = False
        try:
            dataDict = json.loads(post_data)
            isJson = True
        except ValueError:
            isJson = False
        
        # Format differently if JSON data detected
        if isJson:
            s = json.dumps(dataDict,indent=4, sort_keys=True)
        else:
            s = "Not Json data:\n"+post_data
        print s
        
        self._set_headers()
        
        # Replace line feeds with <br> breaks for web HTML display
        webData = "<html><body><h1>POST!</h1><p>Path = {}</p>".format(path)
        s = s.replace("\n","<br>")
        webData += "<div>" + s + "</div>"
        webData += "</body></html>"
        
        self.wfile.write(webData)
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd on port {}...'.format(port)
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
