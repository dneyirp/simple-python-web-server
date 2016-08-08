# Simple Python Web Server

## Synopsis
Very simple Python web server which accepts GET, POST and HEAD

## Usage
`python simple-web-server.py [<port>]`

## Motivation
Needed a simple way to test sending POST data to a webserver that could process the data and provide a custom response

## Installation
No special installation is needed. The only requirement is Python 2.7 or greater.
Simply clone the project and run using python, see Usage section above.

## Testing
Send a GET request:
  - `curl http://localhost`
  
Send a HEAD request:
  - `curl -I http://localhost`
  
Send a POST request:
  - `curl -d "foo=bar&bin=baz" http://localhost`
  - `curl -d "{\"foo\":\"bar\",\"bin\":\"baz\",\"number\":123}" http://localhost`

## Contributors
- Creator : Priyend Somaroo, c/o Vardaan Enterprises, http://www.vardaan.com

## License
Basically an MIT Licence. See the LICENCE file for information on licensing.

## References
Base project file was cloned from https://gist.github.com/2219997.git
