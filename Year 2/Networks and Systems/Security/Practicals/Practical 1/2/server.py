from http.server import BaseHTTPRequestHandler, HTTPServer
import base64
import time

usernames = ["admin", "chris", "greg", "john", "test"]
passwords = ["12345qwert", "ncc1701d", "zxcvbn", "1qaz2wsx", "ncc1701d"]
max_login_retries = 3
login_tries = 0
retry_period = 300.0
lockout_length=6000.0
start=0
class Handler(BaseHTTPRequestHandler):
    global login_tries
    global start
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        if self.headers['Authorization'] == None:
            self.do_AUTHHEAD()
            self.wfile.write(bytes('no auth header received', 'UTF-8'))
            pass
        elif self.verify(self.headers['Authorization']):
            self.do_HEAD()
            self.wfile.write(bytes('Welcome valid user!<br><br>Here is your secret bitcoin private key: KworuAjAtnxPhZARLzAadg9WTVKjY4kckS8pw38JrD33CeVYUuDm.<br><br>Happy spending!', 'UTF-8'))
            pass
        else:
            self.do_AUTHHEAD()
            self.wfile.write(bytes(self.headers['Authorization'], 'UTF-8'))
            self.wfile.write(bytes(' not authenticated', 'UTF-8'))
            print('.', end='', flush=True)
            pass

    def verify(self, data):
        global login_tries
        global start
        login_tries += 1
        print(start)
        if(start==0 or (time.time()-start>lockout_length)):
            start=0
            if (login_tries<max_login_retries):
                for i in range(len(usernames)):
                    if data == 'Basic '+base64.b64encode(bytes(usernames[i]+':'+passwords[i], 'UTF-8')).decode("utf-8"):
                        print(usernames[i]+' has logged in!')
                        return True
                return False
            else:
                start=time.time()
                return False



    def log_message(self, format, *args):
        return

def main():
   try:
      httpd = HTTPServer(('', 12345), Handler)
      print ('started httpd...')
      httpd.serve_forever()
   except KeyboardInterrupt:
      print ('^C received, shutting down server')
      httpd.socket.close()

if __name__ == '__main__':
    main()
