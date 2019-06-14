""" Tests """
from netsocket import *
from constantes import *
from tkinter import *
import socket
import tkinter.scrolledtext as st
from shlex import split
import threading
from time import sleep
import sys
from interface_g import *

client = Client('localhost', 4444)
conn = client.client()
client.connect_client(conn)

t = Interface_chat
thfen = ThrGUI(conn, t)
th = Threcv(conn)
th.start()
thfen.start()
