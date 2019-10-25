from http.server import BaseHTTPRequestHandler, HTTPServer
import base64
import time
import hashlib

usernames = ["admin", "chris", "greg", "john", "test"]
passwords = ["12345qwert", "ncc1701d", "zxcvbn", "1qaz2wsx", "ncc1701d"]
hash_passwords=[
'4f58b8c57d068b133c6c7308248dbb8dcf76405311fbd3591243c3840bba906a',
'43c405a9b48588fde67c2a0d89439c0f7b013efa6f2c8aa3e705b07633a09b5c',
'2e0e630297236bab0cb85333aab77e2d4f85a58566aaff03e7e2e42ca0b4bba1',
'287e9b1c43b8d963a70a1956887fab8126c829b4ef76ab49b2bb1b0db02a0957',
'43c405a9b48588fde67c2a0d89439c0f7b013efa6f2c8aa3e705b07633a09b5c'
]
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
        raw_data=base64.b64decode(data[6:]).decode('UTF-8')
        username=raw_data.split(':')[0]
        password=hashlib.sha3_256(raw_data.split(':')[1].encode('utf-8')).hexdigest()
        global login_tries
        global start
        login_tries += 1
        print(start)
        if(start==0 or (time.time()-start>lockout_length)):
            start=0
            if (login_tries<max_login_retries):
                print(password)
                print(passwords[usernames.index(username)])
                if hash_passwords[usernames.index(username)]==password:
                        print(username+' has logged in!')
                        return True
                return False
            else:
                print("Incorrect password")
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
