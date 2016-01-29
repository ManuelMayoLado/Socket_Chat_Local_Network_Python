# -*- coding: utf-8 -*-

import socket
import json
import time
import sys

SCRIPT,SERVER,PORT,ID,KEY = sys.argv

#CREAMOS O SOCKET
pasivo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#CONECTAMOS O SOCKET PASIVO
pasivo.connect((SERVER, int(PORT)))

#ENVIAMOS O NOVO ID
msx = [ID,u"Pasivo",KEY]
pasivo.send(json.dumps(msx))

#PARA QUE NON ESPERE A RECIVIR DATA DO SOCKET PASIVO
#pasivo.setblocking(0)

print u"*** Cliente Chat - Local ***"
print u"Aquí pode leer os mensaxes do chat\n"

while True:
	try:
		data = pasivo.recv(512)
		msx = json.loads(data)
		time.sleep(0.1)
		id,ip,alias,text = msx
		print "["+"("+str(id)+", "+ip+")"+" - "+alias+"] ",">>> "+text
	except socket.error:
		pass
		time.sleep(0.1)