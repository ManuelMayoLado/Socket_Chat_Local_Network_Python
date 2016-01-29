# -*- coding: utf-8 -*-

import socket
import json
import os
import time
import sys
import locale

SO = "Linux" if os.name == "posix" else "Windows"

print u"*** Cliente Chat - Local ***"

SERVER = raw_input("IP do Servidor: ")
try:
	PORT = int(raw_input(u"Porto: "))
except:
	print u"ERROR - Número incorrecto ou demasiado grande"
	sys.exit(0)
	
ALIAS = raw_input("Alias: ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))
	
#CREAMOS O SOCKET ACTIVO
activo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#CONECTAMOS O SOCKET ACTIVO
activo.connect((SERVER, PORT))

#ENVIMOS A ID 0 PARA QUE O SERVIDOR NOS ASIGNE UNHA ID
#ID, ALIAS, KEY
msx = [0,ALIAS,0]
activo.send(json.dumps(msx))

#RECIVIMOS A CONTESTACIÓN DO SERVIDOR
data = activo.recv(256)

ID,ALIAS,KEY = json.loads(data)

if ID == 0 or ALIAS == "Rechazar":
	print u"Conexión rechazada polo servidor"
	sys.exit(0)

print u"Cliente conectado ao Servidor: ",[SERVER,PORT]
print u"-- ID: "+str(ID),u"Alias: "+ALIAS+" --"

#EXECUTAMOS O SCRIPT QUE MANEXA O SOCKET PASIVO
try:
	if SO == "Windows":
		os.system("start python "+"pasivo.py "+SERVER+" "+str(PORT)+" "+str(ID)+" "+str(KEY))
	else:
		os.system('gnome-terminal -e "'+'python '+'pasivo.py '+SERVER+' '+
					str(PORT)+' '+str(ID)+' '+str(KEY)+'"')
except:
	print u"Non se puido executar en outro terminal o script 'pasivo.py'"
	sys.exit(0)

print "Escriba as mensaxes e presione 'INTRO' para enviar\n"
	
while True:
	time.sleep(0.1)
	text = raw_input(">>> ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))
	if text.replace(" ",""):
		msx = [ID,text]
		try:
			activo.send(json.dumps(msx))
		except:
			print u"ERROR!"
			sys.exit(0)
	
	
	

