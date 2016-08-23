from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()

authorizer.add_user("user", "12345", "/home/aero", perm="elradfmw")
authorizer.add_user("backdoor", "xaker1337", "/home/xaker", perm="elradfmw")
authorizer.add_anonymous("/home/nobody")

handler = FTPHandler
handler.authorizer = authorizer

# FTP_1_flag : Aero{d0nt_sh4r3_y0u_h4cks!!}

server = FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()