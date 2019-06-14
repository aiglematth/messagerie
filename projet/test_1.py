""" Tests """
from netsocket import *
from threads import *

Serv = Serveur('192.168.43.59', 4444)
conn = Serv.serveur()
clientandinfo = Serv.open_serveur(conn)
client = clientandinfo[0]

Threcv = Threadrecv(client, 'Matthieu', '\a')
Threnv = Threadenv(client, 'Matthieu', Threcv)
Threcv.start()
Threnv.start()
Threcv.join()
Threnv.join()
