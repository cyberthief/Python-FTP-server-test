from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()

authorizer.add_user("user", "12345", "/home/kronos", perm="elradfmw")
authorizer.add_user("backdoor", "xaker1337", "/home/xaker", perm="elradfmw")


handler = FTPHandler
handler.authorizer = authorizer

# Pentes_Host1_Flag4:Aero{d0nt_sh4r3_y0u_h4cks}

server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
