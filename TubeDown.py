# -*- coding: utf-8 -*-
# Python 3
# Windows
#
#████████╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗
#╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔═══██╗██║    ██║████╗  ██║
#   ██║   ██║   ██║██████╔╝█████╗  ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
#   ██║   ██║   ██║██╔══██╗██╔══╝  ██║  ██║██║   ██║██║███╗██║██║╚██╗██║
#   ██║   ╚██████╔╝██████╔╝███████╗██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║
#   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝
#                                                         By: LawlietJH
#																v1.3.2

import urllib.request
import urllib.error
import msvcrt
import time
import sys
import os
import re



Autor = "LawlietJH"
Version = "v1.3.2"



BTD = r"""
    ████████╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗
    ╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔═══██╗██║    ██║████╗  ██║
       ██║   ██║   ██║██████╔╝█████╗  ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
       ██║   ██║   ██║██╔══██╗██╔══╝  ██║  ██║██║   ██║██║███╗██║██║╚██╗██║
       ██║   ╚██████╔╝██████╔╝███████╗██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║
       ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝  """
#~ Fuente: ANSI Shadow, Página: http://patorjk.com/software/taag



BA = r"""
                            ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐╦╦ ╦
                            ║  ├─┤││││  │├┤  │ ║╠═╣
                            ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴╚╝╩ ╩"""
#~ Fuente: Calvin S, Página: http://patorjk.com/software/taag



#=======================================================================



def Dat(Quiet=False):		# Muestra La Información Del Script: Autor, Versión y Nombre.
		
	Nombre = BTD
	Autor = BA
	Ver = "\n\n{:^80}".format(Version)
	print(Nombre, "\n\n", Autor, Ver)
	
	if Quiet: pass
	else:
		try:
			Sleep(3)
		except KeyboardInterrupt:
			Dat()



#=======================================================================



def PressON(Cadena=""):		# Permite Capturar 1 Caracter Que se Escriba en Pantalla,
							# Como un Input() pero de 1 solo caracter.
	
	Imp()
	
	print(Cadena, end="")
	Resp = msvcrt.getch()
	print(Resp)
	
	return Resp



def Imp():	# Limpia El Buffer (Flush)
    
    try:
        
        import msvcrt
        
        while msvcrt.kbhit(): msvcrt.getch()
            
    except ImportError:
		
        import sys, termios
        
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)



def Pause(Quiet=True):		# Hace Una Pausa.
	
	if Quiet: os.system("Pause > Nul")		# No muestra Nada En Pantalla.
	
	else: os.system("Pause")		# Muestra En Pantalla: Presione una tecla para continuar...



def Clear():		# Limpia Pantalla.
	
	os.system("Cls")



def Salir(Num=0):
	
	HiddenCursor("Show")
	Clear()
	Dat()
	
	exit(Num)



def Sleep(Num=1.5):
	
	time.sleep(Num)



def Ctrl_C():
	
	try:
		print("\n\n\n\n\t\t [!] Cancelado...")
		os.system("title Cancelando... && timeout /nobreak 03 > Nul")
		return
		
	except KeyboardInterrupt:
		
		Ctrl_C()



#=======================================================================



#~ Función Que Permite Esconder El Cursor de la Pantalla (La rayita que parpadea xD).
def HiddenCursor(imp="Hide"):
	
	#~ imp = imp.title()		#Devuelve la cadena solo con la primera letra de cada palabra en mayuscula
	imp = imp.capitalize()		#Devuelve la cadena solo con la primera letra de la primer palabra en mayuscula

	if os.name == 'nt':
		import msvcrt
		import ctypes

		class _CursorInfo(ctypes.Structure):
			_fields_ = [("size", ctypes.c_int),
						("visible", ctypes.c_byte)]
	
	def hide_cursor():
		if os.name == 'nt':
			ci = _CursorInfo()
			handle = ctypes.windll.kernel32.GetStdHandle(-11)
			ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
			ci.visible = False
			ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
		elif os.name == 'posix':
			sys.stdout.write("\033[?25l")
			sys.stdout.flush()

	def show_cursor():
		if os.name == 'nt':
			ci = _CursorInfo()
			handle = ctypes.windll.kernel32.GetStdHandle(-11)
			ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
			ci.visible = True
			ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
		elif os.name == 'posix':
			sys.stdout.write("\033[?25h")
			sys.stdout.flush()
			
	if imp == "Hide":
		hide_cursor()
	elif imp =="Show":
		show_cursor()
	else:
		pass



#=======================================================================



def Chk_Dep():
	
	try:
		import pytube
		
	except ImportError:
		print("\n\n\t[!] Instalando Dependencias...\n\n\t\t")
		x = os.popen("title Instalando PyTube && py -m pip install pytube > Nul && cls").read()
		
		if x == "":
			Clear()
			print("\n\n\t [!] Se Necesita Tener Instalado\n\n\t     El Administrador de Paquetes de Python: Pip\n\n\t Instalalo.")
			Pause(), Salir(1)
			
	except Exception as ex:
		print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.



Chk_Dep()				#~ Se instala el módulo pytube si esta no esta instalada.
try:
	from pytube import *	# Se Importa El Módulo.
except:					# Si Hay Algún Error Significa Que No Se Instaló Correctamente.
	print("\n\n   No se pudo instalar correctamente el Módulo 'pytube'.")
	print("\n   Revise Su Conexión o Instale El Módulo Manualmente Desde Consola Con:")
	print("\n\t 'pip install pytube'   o   ' pip3 install pytube'")
	
	try: Pause
	except KeyboardInterrupt: pass
	
	Salir(0)



#=======================================================================



def Modo_de_Uso():
	
	os.system("cls && title TubeDown.py            by: LawlietJH")
	Dat(True)
	
	Uso = """   Modo De Uso:\n\n TubeDown.py [-l URList.ext][-nr] | [-v|-h] | [URL] | [-lr URListaRep][Ruta]
	\n\n\t -l,  --list \t\t Se coloca el nombre del archivo\n\t\t\t\t para obtener la lista de URLs.
	\n\t -nr, --norepetir \t Se añade este argumento después\n\t\t\t\t de seleccionar el archivo de URLs.\n\t\t\t\t Evita Repetir Videos.
	\n\t -lr, --listrep \t Se añade este argumento y después se escribe \n\t\t\t\t la URL de la lista de Reproducción de Youtube.
	\t\t\t Se le puede añadir ruta de Descargar.
	\n\t -v,  --version \t Muestra la versión y autor del Script.
	\n\n\t -h,  --help \t\t Muestra el Modo De Uso.
	\n\n https://www.youtube.com/...\t Se añade la URL como argumento y \n\t\t\t\t sólo se descargará ese video.
	\n\n   Ejemplos De Uso:\n\n\t   TubeDown.py  -l  xD.zion  -nr
	\n\t   TubeDown.py  https://www.youtube.com/video_etc...
	\n\t   TubeDown.py  -lr https://www.youtube.com/Lista_De_Reproducción...
	"""
	
	print(Uso)
	Pause()


#=======================================================================



def Ruta_Descargas():
	
	Ruta = os.getcwd()							#~ Se Obtiene La Ruta Actual Del Script
	
	if not os.path.exists(Ruta+"\Descargas"):	#~ Comprobamos si existe la Carpeta de Descargas.
		os.mkdir(Ruta+"\Descargas")				#~ Creamos La Carpeta de descargas si No existe.
	
	os.chdir("Descargas")						#~ Nos Situamos En La Carpeta De Descargas 
	
	Ruta = os.getcwd()							#~ Guardamos La Ruta.
	
	return Ruta



def Ruta_txt():
	
	Ruta = os.getcwd()			#~ Se Obtiene La Ruta Actual Del Script
	
	os.chdir("..")				#~ Nos Situamos En La Carpeta Del Script 
	
	Ruta = os.getcwd()			#~ Guardamos La Ruta.
	
	return Ruta
	


def Chk_txt(x):		# Comprueba si Existe un Archivo.
	
	Ruta_txt()
	
	if not os.path.exists(x):
		print("\n\n\t\t [!] No Existe El Archivo: "+x)
		os.system('Timeout /nobreak 03 > Nul')
		Salir(0)
	else:
		return True
	


def Chk_URL():		# Comprueba La URL.
	
	while xD:
		
		global Cont
		Cont = 0
		
		try:
			
			Download()			#~ Método para descargar videos.
			
		except ValueError:								#~ Por si se escribe algo que no sea una URL
			print("\n\n\n\t\t [!] No es una URL...")
			
		except IndexError:								#~ Por si no se escribe nada.
			print("\n\n\n\t\t [!] Escribe una URL...")	
			
		except KeyboardInterrupt:						#~ Por si cancela la operación con "Ctrl + C".
			Ctrl_C()
			Salir(0)
			
		except AttributeError:
			print("\n\n\n\t\t [!] El URL no es válido...\n\n")
			Salir(0)
			
		except Exception as ex:
			
			if type(ex).__name__ == "HTTPError":			#~ Si el tipo de error es HTTPError imprimirá algo en pantalla.
				print("\n\n\n\t\t [!] El URL no es válido...\n\n")
				Salir(0)
				
			elif type(ex).__name__ == "URLError":			#~ Si el tipo de error es URLError imprimirá algo en pantalla.
				print("\n\n\n\t\t [!] El URL no es válido... o Quizá No Hay Conexión...\n\n")
				
				if URLEnArgv == True: Salir(0)
				
			elif type(ex).__name__ == "AgeRestricted":		#~ Si el tipo de error es AgeRestricted imprimirá algo en pantalla.
				print("\n\n\n\t [!] Restricción de Edad.")
				
				resp = input("\n\n\n\t [¡] Quizá la URL es una Lista de Reproducción de Youtube [S/N]: ")
				
				if resp == "S" or resp == "s" or resp == "Si" or resp == "si" or resp == "SI" or resp == "sI":
					Modo_de_Uso()
					Salir(0)
				else:
					Salir(0)
			else:
				print("\n\n\n\t\t",type(ex).__name__)	#Si ocurre un error nuevo mostrara el nombre y no cerrará el programa.



def Chk_URL_Lista():
	
	for URL in VideosList:
		
		global Cont
		Cont = 0
		
		try:
			
			Download_Lista(URL)			#~ Método para descargar videos.
			
		except ValueError:								#~ Por si se escribe algo que no sea una URL
			print("\n\n\n\t\t [!] No es una URL...")
			
		except IndexError:								#~ Por si no se escribe nada.
			print("\n\n\n\t\t [!] Escribe una URL...")	
			
		except KeyboardInterrupt:						#~ Por si cancela la operación con "Ctrl + C".
			Ctrl_C()
			Salir(0)
		
		#~ except NameError:
			#~ Salir(0)
			
		except Exception as ex:
			
			if type(ex).__name__ == "URLError":			#~ Si el tipo de error es URLError imprimirá algo en pantalla.
				print("\n\n\n\t\t [!] El URL no es válido... o Quizá No Hay Conexión...")
			else:
				print("\n\n\n\t\t",type(ex).__name__)	#Si ocurre un error nuevo mostrara el nombre y no cerrará el programa.



#=======================================================================



def Open_txt(X):		# Abre un Archivo de Texto.
	
	global VideosList
	global VidTotal
	
	Archivo = open(X,"r")	#~ Se abre el archivo.
	
	for linea in Archivo:
		VideosList.append(linea)	#~ Se añade cada URL del archivo a la lista .
		VidTotal += 1
		
	Archivo.close()



#=======================================================================



def Download():		# Hace La Descarga De URL Individual.
	
	global Cont
	
	if URLEnArgv == True:				#~ Si se paso la URL en los argumentos se descargará solo ese video.
		URLVid = sys.argv[1]
	else:
		
		URLVid = input("\n\n\n\t [+] URL: ")		#~ Escribimos la URL del Video a Descargar.	
		
		if URLVid.startswith("-lr") or URLVid.startswith("-lr"):
			
			print("\n\n\t Lista De Reproducción.")
			
			#~ Descarga una lista de Reproducción de Youtube
			URL = URLVid.split(" ")
			URL = URL[1]
				
			if not URL.startswith("https://"):
				URL = 'https://' + URL
				
			playlist_page_content = getPageHtml(URL)
			vid_urls_in_playlist = getPlaylistVideoUrls(playlist_page_content, URL)
			
			LR = True
			
			# Descarga los Videos de La Lista de Reproducción.
			for Video_URL in vid_urls_in_playlist:
				Lista_Reproduccion(Ruta, Video_URL)
				Sleep(1)
		
		elif URLVid.startswith("https://"): pass
		else: print("\n\n\t [!] Error, URL no valida.")
	
	Video = YouTube(URLVid)					#~ Se Obtienen Todas Las Calidades Posibles De Ese Video.
	#~ VideoHD = Video.get('mp4', '720p')		#~ Obtenemos el video mp4 de 720p.
	#~ VideoHD = Video.filter('mp4')[-1]		#~ Obtenemos el video mp4 de mejor calidad posible.
	
	#=======================================================================
	
	Clear()
	
	print("\n\n\t [*] Por Defecto [.mp4]")
	z = input("\n\t [+] Seleccionar Calidad Y Formato Manualmente? [S/N]\n\n\t >>> ").lower()
	
	if z == "si" or z == "s":
	
		while True:
			
			Clear()
			Conty = 0
			Dic = {}
			
			print("\n\n\t  [*] Formatos Y Calidades Disponibles:\n")
			
			for _ in Video.get_videos():		# Permite Elegir el Formato y La Caidad Deseada de los videos.
				Conty += 1
				x = str(_)
				Formato = x.split(": ")[1].split(" - ")[0]
				Calidad = x.split(" - ")[1]
				
				Cadena = Formato + " - " + Calidad
				Dic[Conty] = Cadena
				
				print("\t [", Conty, "] ", Cadena)
			
			try:
				Ops = int(PressON("\n\t >>> "))
				
				if Ops < 1 or Ops > Conty:
					
					print("\n\n\t [!] Elige una Opción Valida!")
					Sleep()
					continue
				
				Dato = Dic[int(Ops)]
			
				Formato = Dato.split("(.")[1].split(")")[0]
				Calidad = Dato.split(" - ")[1]
				VideoHD = Video.get(Formato, Calidad)
				Nomb = Nombre = VideoHD.filename
				
				break
			
			except ValueError:
				
				print("\n\n\t [!] Elige un Número!")
				Sleep()
				
			except Exception as ex:
				print(type(ex).__name__)
				Dat()
				Salir()
	
	else:
		VideoHD = Video.filter('mp4')[-1]
		Nomb = Nombre = VideoHD.filename
	
	#=======================================================================
	
	while xD:
		
		try:
			os.system("cls && title Descargando:   " + Nombre)
			print("\n\n\n [+] Video: ", Video.filename, "\n\n")		#~ Se imprime el nombre del video.
			bar = BarraProgreso()
			VideoHD.download(r""+Ruta, on_progress=bar.Progreso, on_finish=bar.End)		#~ Descargamos el video seleccionado.
			
			if URLEnArgv == True:			#~ Si se paso la URL en los argumentos se descargará solo ese video.
				Salir(0)
			
			break
			
		except OSError:
			Cont += 1
			Video.set_filename(Nombre+" ("+str(Cont)+")")	#~ Se añade al nombre (#) un número para evitar repetición.
			
		except KeyboardInterrupt:						#~ Por si cancela la operación con "Ctrl + C".
			Ctrl_C()
			if URLEnArgv == True:			#~ Si se paso la URL en los argumentos y se cancela cerrará el Script.
				Data()
				Salir(0)
				
			break
		
		except Exception as ex:
			print(type(ex).__name__)	#Si ocurre un error nuevo mostrara el nombre y no cerrará el programa.
			system("Pause > Nul")
			


#=======================================================================



def Download_Lista(URLVid):
		
	global Conny
	global Cont
	
	Video = YouTube(URLVid)					#~ Se Obtienen Todas Las Calidades Posibles De Ese Video.
	#~ VideoHD = Video.get('mp4', '720p')		#~ Obtenemos el video mp4 de 720p.
	VideoHD = Video.filter('mp4')[-1]		#~ Obtenemos el video mp4 de mejor calidad posible.
	Nomb = Nombre = VideoHD.filename
	
	while xD:
		
		try:
			os.system("cls && title Descargando:   " + Nombre)
			print("\n\n\n [+] Video: ", Video.filename, "\n\n")		#~ Se imprime el nombre del video.
			bar = BarraProgreso()
			VideoHD.download(r""+Ruta, on_progress=bar.Progreso, on_finish=bar.End)		#~ Descargamos el video seleccionado.
			Sleep(1)
			break
			
		except OSError:
			if NoRepetir == True:
				Conny += 1
				print("\n\n\t\t [!] Video Repetido...")			#~ Usando 'TubeDown.py -l URList.ext -nr' (.ext significa extensión)
				print("\n\n\t\t\t", Conny," / ", VidTotal)	#~ Mostrara esto si el video esta repetido y no lo descargará.
				Sleep(1)
				break
			else:
				Cont += 1
				Video.set_filename(Nombre+" ("+str(Cont)+")")	#~ Se añade al nombre (#) un número para evitar repetición.
			
		except KeyboardInterrupt:						#~ Por si cancela la operación con "Ctrl + C".
			Ctrl_C()
			Salir(0)
		
		except Exception as ex:
			print(type(ex).__name__)	#Si ocurre un error nuevo mostrara el nombre y no cerrará el programa.
			Pause()
	

     
#~ Datos Para La Barra de Progreso
#~ =========================================================================================================================
#~ ======================================== INICIO =========================================================================
#~ =========================================================================================================================



class BarraProgreso:
	
	def __init__(self, barlength=20):
		self.barlength = barlength
		self.position = 0
		self.longest = 0
	
	def Progreso(self, cur, total, start):
		currentper = cur / total
		
		TamTotal = Bytes_Cadena(total)
		TamActual = Bytes_Cadena(cur)
		Porcent = int((cur*100) / total)
		
		elapsed = int(time.clock() - start) + 1
		curbar = int(currentper * self.barlength)
		
		bar = '\r {}%'.format(Porcent)
		bar += ' |' + '█'.join(['' for _ in range(curbar)])  # Imprimir Progreso
		#~ bar += '|'
		bar += ' '.join(['' for _ in range(int(self.barlength - curbar))]) + '|'  # Espacio Restante en Progreso
		bar += ' [' + TamActual			#~ Tamaño Descargado
		bar += '/' + TamTotal			#~ tamaño Total
		bar += '] [' + Bytes_Cadena(cur / elapsed) + '/s] ['  # Calcula la Velocidad de Descarga por Segundo
		bar += Tiempo((total - cur) * (elapsed / cur)) + ']    '  # Calcula El Tiempo Restante
		
		if len(bar) > self.longest:
			self.longest = len(bar)
			bar += ' '.join(['' for _ in range(self.longest - len(bar))])
			
		sys.stdout.write(bar)
	
	def End(self, *args):
			
		if LR == True:
			global Conny
			Conny += 1
			print("\n\n\n\n\t\t Descargado!\t", Conny, " / ", VidTotal)
		else:
			print("\n\n\n\n\t\t Descargado!")
		


def Tiempo(sec):
	if sec >= 3600:  # Convierte a Horas
		return '{0:d} hora(s)'.format(int(sec / 3600))
	elif sec >= 60:  # Convierte a Minutos
		return '{0:d} minuto(s)'.format(int(sec / 60))
	else:            # Sin Conversión
		return '{0:d} segundo(s)'.format(int(sec))



def Bytes_Cadena(bts):
	bts = float(bts)
	if bts >= 1024 ** 4:    # Convierte a Terabytes
		terabytes = bts / 1024 ** 4
		size = '{:.2f} Tb'.format(terabytes)
	elif bts >= 1024 ** 3:  # Convierte a Gigabytes
		gigabytes = bts / 1024 ** 3
		size = '{:.2f} Gb'.format(gigabytes)
	elif bts >= 1024 ** 2:  # Convierte a Megabytes
		megabytes = bts / 1024 ** 2
		size = '{:.2f} Mb'.format(megabytes)
	elif bts >= 1024:       # Convierte a Kilobytes
		kilobytes = bts / 1024
		size = '{:.0f} Kb'.format(kilobytes)
	else:                   # Sin Conversión
		size = '{:.0f} b'.format(bts)
	return size



#~ =========================================================================================================================
#~ ========================================= FIN ===========================================================================
#~ =========================================================================================================================



#~ Funciones Para descargar Listas de Reproducción De YouTube.
#~ =========================================================================================================================
#~ ======================================== INICIO =========================================================================
#~ =========================================================================================================================



def getPageHtml(url):
	try:
		yTUBE = urllib.request.urlopen(url).read()
		return str(yTUBE)
	except urllib.error.URLError as e:

		print("\n\n\t [!] URL No Valida.")
		Sleep(3)
		Modo_de_Uso()
		Salir(1)



def getPlaylistUrlID(url):
	if 'list=' in url:
		eq_idx = url.index('=') + 1
		pl_id = url[eq_idx:]
		if '&' in url:
			amp = url.index('&')
			pl_id = url[eq_idx:amp]
		return pl_id
	else:
		print(url, "\n\n [!] No es una Lista de Reproducción de Youtube.")
		Salir(1)



def getFinalVideoUrl(vid_urls):
	final_urls = []
	for vid_url in vid_urls:
		url_amp = len(vid_url)
		if '&' in vid_url:
			url_amp = vid_url.index('&')
		final_urls.append('http://www.youtube.com/' + vid_url[:url_amp])
	return final_urls



def getPlaylistVideoUrls(page_content, url):
	playlist_id = getPlaylistUrlID(url)
	
	vid_url_pat = re.compile(r'watch\?v=\S+?list=' + playlist_id)
	vid_url_matches = list(set(re.findall(vid_url_pat, page_content)))
	
	if vid_url_matches:
		final_vid_urls = getFinalVideoUrl(vid_url_matches)
		print("\n\n [*] Encontrados", len(final_vid_urls), "Videos en la Lista De Reproducción\n\n")
		ImprimirURLs(final_vid_urls)
		return final_vid_urls
	else:
		print('\n\n [!] Ningun Video Encontrado.')
		Salir(1)



#Función Añadida Para Obener Los Archivos de Audio a lo Largo de los Video de La Lista de Reproducción.
def Lista_Reproduccion(Ruta, vid_url):
	
	try:
		yt = YouTube(vid_url)
	except Exception as ex:
		print("\n\n\n\t Error:", str(ex), "- Saltandose Video con la URL '"+vid_url+"'.")
		print("\n\n\t Video:", yt.filename)
		return
	
	#~ video = yt.get('mp4', '720p')		#~ Obtenemos el video mp4 de 720p.
	video = yt.filter('mp4')[-1]
	
	os.system("title Descargando:   " + yt.filename)
	print("\n\n [+] Video:", yt.filename, "\n\n")
	try:
		bar = BarraProgreso()
		video.download(Ruta, on_progress=bar.Progreso, on_finish=bar.End)
		
	except OSError:
		global Conny
		Conny += 1
		print(" [!] Ya existe este Video! Saltando...")
		print("\n\n\t\t\t\t", Conny," / ", VidTotal)
		
	except KeyboardInterrupt:
		Ctrl_C()
		Salir(0)
	
	except Exception as ex:
		print("\n\n\t\t", type(ex).__name__)
		


def ImprimirURLs(vid_urls):
	global VidTotal
	VidTotal = 0
	for x, url in enumerate(vid_urls):
		print("\t", x+1, " - ", url)
		Sleep(0.04)
		VidTotal += 1



#~ =========================================================================================================================
#~ ========================================= FIN ===========================================================================
#~ =========================================================================================================================



xD = True
LR = False
NoRepetir = False
URLEnArgv = False
Cont = 0
Conny = 0
VidTotal = 0
VideosList = []
Ruta = Ruta_Descargas()		#~ Obtenemos La Ruta Para Descargar el o los Videos deseados.



def main():
	
	os.system("cls && title TubeDown.py                  by: LawlietJH" +\
			  "                  " + Version)
	
	global Ruta
	global LR
	global NoRepetir
	global URLEnArgv
	
	HiddenCursor("Hide")
	
	if len(sys.argv) == 4:
		
		if sys.argv[1] == "-l" or sys.argv[1] == "--list":
			Dato = sys.argv[2]
			
			if sys.argv[3] == "-nr" or sys.argv[3] == "--norepetir":
				
				LR = True
				NoRepetir = True
				Chk_txt(Dato)
				Open_txt(Dato)
				
				Chk_URL_Lista()
				
				Salir(0)
		
		#~ Descarga una lista de Reproducción de Yotube en la Ruta especificada.
		elif sys.argv[1] == "-lr" or sys.argv[1] == "--listrep":
			URL = sys.argv[2]
			
			Ruta = Ruta_txt()
			
			Ruta = sys.argv[3]
		
			# Crea el directorio si el especificado no existemake directory if dir specified doesn't exist
			try:
				os.makedirs(Ruta, exist_ok=True)
			except OSError as ex:
				print(ex.reason)
				Salir(1)
			
			if not URL.startswith("https://"):
				URL = 'https://' + URL
			
			playlist_page_content = getPageHtml(URL)
			vid_urls_in_playlist = getPlaylistVideoUrls(playlist_page_content, URL)
			
			LR = True
			
			# Descarga los Videos de La Lista de Reproducción.
			for Video_URL in vid_urls_in_playlist:
				Lista_Reproduccion(Ruta, Video_URL)
				Sleep(1)
		
		else:	Modo_de_Uso()
		
	elif len(sys.argv) == 3:
		
		if sys.argv[1] == "-l" or sys.argv[1] == "--list":
			Dato = sys.argv[2]
			
			LR = True
			Chk_txt(Dato)
			Open_txt(Dato)
			
			Chk_URL_Lista()
			
			Salir(0)
		
		#~ Descarga una lista de Reproducción de Yotube
		elif sys.argv[1] == "-lr" or sys.argv[1] == "--listrep":
			URL = sys.argv[2]
			
			if not URL.startswith("https://"):
				URL = 'https://' + URL
			
			playlist_page_content = getPageHtml(URL)
			vid_urls_in_playlist = getPlaylistVideoUrls(playlist_page_content, URL)
			
			LR = True
			
			# Descarga los Videos de La Lista de Reproducción.
			for Video_URL in vid_urls_in_playlist:
				Lista_Reproduccion(Ruta, Video_URL)
				Sleep(1)
			
		else:	Modo_de_Uso()
		
	elif len(sys.argv) == 2:
		
		if sys.argv[1] == "-h" or sys.argv[1] == "--help":
			Modo_de_Uso()
		elif sys.argv[1] == "-v" or sys.argv[1] =="--version":
			print("\n\n\n\n\n")
			Dat()
			os.system("title TubeDown.py            by: LawlietJH && Pause > Nul")
		elif "https://www.youtube.com/" in sys.argv[1]:
			URLEnArgv = True
			Chk_URL()
		
		else:	Modo_de_Uso()
	
	elif len(sys.argv) == 1:
		Chk_URL()
	
	else:	Modo_de_Uso()
		


if __name__ == "__main__":
	
	main()
	
	HiddenCursor("Show")


