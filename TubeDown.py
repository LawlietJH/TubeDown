# -*- coding: utf-8 -*-
# Python 3
#
#████████╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗
#╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔═══██╗██║    ██║████╗  ██║
#   ██║   ██║   ██║██████╔╝█████╗  ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
#   ██║   ██║   ██║██╔══██╗██╔══╝  ██║  ██║██║   ██║██║███╗██║██║╚██╗██║
#   ██║   ╚██████╔╝██████╔╝███████╗██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║
#   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝
#                                                         By: LawlietJH
#																v1.2.6

import urllib.request
import urllib.error

import time
import sys
import os
import re

Autor = "LawlietJH"
Version = "v1.2.6"

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


def Dat():
	
	os.system("cls")
	
	Nombre = BTD
	Autor = BA
	Ver = "\n\n{:^80}".format(Version)
	print(Nombre, "\n\n", Autor, Ver)
	

def Salir(Num=0):
	
	HiddenCursor("Show")
	exit(Num)

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


def Chk_Dep():
	
	try:
		import pytube
		
	except ModuleNotFoundError:
		print("\n\n\t[!] Instalando Dependencias...\n\n\t\t")
		os.system("pip install pytube > Nul && cls")
		
	except Exception as ex:
		print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.


Chk_Dep()				#~ Se instala el módulo pytube si esta no esta instalada.
from pytube import *	#~ Se importa la módulo.


def Modo_de_Uso():
	
	Dat()
	
	Uso = """   Modo De Uso:\n\n TubeDown.py [-l URList.ext][-nr] | [-v|-h] | [URL] | [-lr URListaRep][Ruta]
	\n\n\t -l,  --list \t\t Se coloca el nombre del archivo\n\t\t\t\t para obtener la lista de URLs.
	\n\t -nr, --norepetir \t Se añade este argumento después\n\t\t\t\t de seleccionar el archivo de URLs.
	\n\t -lr, --listrep \t Se añade este argumento y después se escribe \n\t\t\t\t la URL de la lista de Reproducción de Youtube.
	\t\t\t Se le puede añadir ruta de Descargar.
	\n\t -v,  --version \t Muestra la versión y autor del Script.
	\n\n\t -h,  --help \t\t Muestra el Modo De Uso.
	\n\n https://www.youtube.com/...\t Se añade la URL como argumento y \n\t\t\t\t sólo se descargará ese video.
	\n\n   Ejemplos De Uso:\n\n\t   TubeDown.py  -l  xD.zion  -nr
	\n\t   TubeDown.py  http://www.youtube.com/video_etc...
	\n\t   TubeDown.py  -lr http://www.youtube.com/Lista_De_Reproducción...
	"""
	
	print(Uso)


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
	


def Chk_txt(x):
	
	Ruta_txt()
	
	if not os.path.exists(x):
		print("\n\n\t\t [!] No Existe El Archivo: "+x)
		os.system('Timeout /nobreak 03 > Nul')
		Salir(0)
	else:
		return True
	

def Chk_URL():
	
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
			
		except Exception as ex:
			
			if type(ex).__name__ == "URLError":			#~ Si el tipo de error es URLError imprimirá algo en pantalla.
				print("\n\n\n\t\t [!] El URL no es válido... o Quizá No Hay Conexión...")
			elif type(ex).__name__ == "AgeRestricted":
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
	
	for URL in Videos:
		
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
			
		except Exception as ex:
			
			if type(ex).__name__ == "URLError":			#~ Si el tipo de error es URLError imprimirá algo en pantalla.
				print("\n\n\n\t\t [!] El URL no es válido... o Quizá No Hay Conexión...")
			else:
				print("\n\n\n\t\t",type(ex).__name__)	#Si ocurre un error nuevo mostrara el nombre y no cerrará el programa.
				


def Ctrl_C():
	try:
		print("\n\n\n\n\t\t [!] Cancelado...")
		os.system("timeout /nobreak 03 > Nul")
		return
	except KeyboardInterrupt:
		Ctrl_C()


def Open_txt(X):
	
	global Videos
	
	Archivo = open(X,"r")	#~ Se abre el archivo.
	
	for linea in Archivo:
		Videos.append(linea)	#~ Se añade cada URL del archivo a la lista .
	
	Archivo.close()

def Download():
	
	global Cont
	
	if URLEnArgv == True:				#~ Si se paso la URL en los argumentos se descargará solo ese video.
		URLVid = sys.argv[1]
	else:
		URLVid = input("\n\n\n\t [+] URL: ")		#~ Escribimos la URL del Video a Descargar.	
	
	
	Video = YouTube(URLVid)					#~ Se Obtienen Todas Las Calidades Posibles De Ese Video.
	#~ VideoHD = Video.get('mp4', '720p')		#~ Obtenemos el video mp4 de 720p.
	VideoHD = Video.filter('mp4')[-1]			#~ Obtenemos el video mp4 de mejor calidad posible.
	Nomb = Nombre = VideoHD.filename
	
	while xD:
		
		try:
			os.system("cls")
			print("\n\n\n [+] Video: ", Video.filename, "\n\n")		#~ Se imprime el nombre del video.
			bar = BarraProgreso()
			VideoHD.download(r""+Ruta, on_progress=bar.Progreso, on_finish=bar.End)		#~ Descargamos el video seleccionado.
			
			if URLEnArgv == True:			#~ Si se paso la URL en los argumentos se descargará solo ese video.
				Salir(0)
			
			break
			
		except OSError:
			Cont += 1
			Video.set_filename(Nombre+" ("+str(Cont)+")")	#~ Se añade al nombre (#) un numero para evitar repetición.
			
		except KeyboardInterrupt:						#~ Por si cancela la operación con "Ctrl + C".
			Ctrl_C()
			break
		
		except Exception as ex:
			print(type(ex).__name__)	#Si ocurre un error nuevo mostrara el nombre y no cerrará el programa.
			system("Pause > Nul")
			


def Download_Lista(URLVid):
		
	global Cont
	
	Video = YouTube(URLVid)					#~ Se Obtienen Todas Las Calidades Posibles De Ese Video.
	#~ VideoHD = Video.get('mp4', '720p')		#~ Obtenemos el video mp4 de 720p.
	VideoHD = Video.filter('mp4')[-1]			#~ Obtenemos el video mp4 de mejor calidad posible.
	Nomb = Nombre = VideoHD.filename
	
	while xD:
		
		try:
			system("cls")
			print("\n\n\n [+] Video: ", Video.filename, "\n\n")		#~ Se imprime el nombre del video.
			bar = BarraProgreso()
			VideoHD.download(r""+Ruta, on_progress=bar.Progreso, on_finish=bar.End)		#~ Descargamos el video seleccionado.
			time.sleep(1)
			break
			
		except OSError:
			if NoRepetir == True:
				print("\n\n\t\t [!] Video Repetido...")		#~ Usando 'TubeDown.py -l URList.ext -nr' (.ext significa extensión)
				time.sleep(1)								#~ Mostrara esto si el video esta repetido y no lo descargará.
				break
			else:
				Cont += 1
				Video.set_filename(Nombre+" ("+str(Cont)+")")	#~ Se añade al nombre (#) un numero para evitar repetición.
			
		except KeyboardInterrupt:						#~ Por si cancela la operación con "Ctrl + C".
			Ctrl_C()
			Salir(0)
		
		except Exception as ex:
			print(type(ex).__name__)	#Si ocurre un error nuevo mostrara el nombre y no cerrará el programa.
			os.system("Pause > Nul")
	


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
		
		elapsed = int(time.clock() - start) + 1
		curbar = int(currentper * self.barlength)
		bar = '\r ' + TamActual			#~ Tamaño Descargado
		bar += ' / ' + TamTotal			#~ tamaño Total
		bar += '  [' + '='.join(['' for _ in range(curbar)])  # Imprimir Progreso
		bar += '>'
		bar += ' '.join(['' for _ in range(int(self.barlength - curbar))]) + ']  '  # Espacio Restante en Progreso
		bar += Bytes_Cadena(cur / elapsed) + '/s  '  # Calcula la Velocidad de Descarga por Segundo
		bar += Tiempo((total - cur) * (elapsed / cur)) + '    '  # Calcula El Tiempo Restante
		
		if len(bar) > self.longest:
			self.longest = len(bar)
			bar += ' '.join(['' for _ in range(self.longest - len(bar))])
			
		sys.stdout.write(bar)
	
	def End(self, *args):
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
		size = '{:.2f} Kb'.format(kilobytes)
	else:                   # Sin Conversión
		size = '{:.2f} b'.format(bts)
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
		time.sleep(3)
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
		printUrls(final_vid_urls)
		return final_vid_urls
	else:
		print('\n\n [!] Ningun Video Encontrado.')
		Salir(1)



#function added to get audio files along with the video files from the playlist

def Lista_Reproduccion(Ruta, vid_url):
	try:
		yt = YouTube(vid_url)
	except Exception as ex:
		print("\n\n\n\t Error:", str(ex), "- Saltandose Video con la URL '"+vid_url+"'.")
		print("\n\n\t Video:", yt.filename)
		return

	video = yt.filter('mp4')[-1]
	
	print("\n\n [+] Video:", yt.filename, "\n\n")
	try:
		bar = BarraProgreso()
		video.download(Ruta, on_progress=bar.Progreso, on_finish=bar.End)
		
	except OSError:
		print(" [!] Ya existe este Video! Saltando...")
		
	except KeyboardInterrupt:
		Ctrl_C()
		Salir(0)
	
	except Exception as ex:
		print("\n\n\t\t", type(ex).__name__)
		


def ImprimirURLs(vid_urls):
	for x, url in enumerate(vid_urls):
		print("\t", x+1, " - ", url)
		time.sleep(0.04)
		



#~ =========================================================================================================================
#~ ========================================= FIN ===========================================================================
#~ =========================================================================================================================



xD = True
NoRepetir = False
URLEnArgv = False
Cont = 0
Videos = []
Ruta = Ruta_Descargas()		#~ Obtenemos La Ruta Para Descargar el o los Videos deseados.



def main():
	
	os.system("cls")
	
	global Ruta
	global NoRepetir
	global URLEnArgv
	
	HiddenCursor("Hide")
	
	if len(sys.argv) == 4:
		
		if sys.argv[1] == "-l" or sys.argv[1] == "--list":
			Dato = sys.argv[2]
			
			if sys.argv[3] == "-nr" or sys.argv[3] == "--norepetir":
				
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
			except OSError as e:
				print(e.reason)
				Salir(1)
			
			if not URL.startswith("https://"):
				URL = 'https://' + URL
			
			playlist_page_content = getPageHtml(URL)
			vid_urls_in_playlist = getPlaylistVideoUrls(playlist_page_content, URL)

			# Descarga los Videos de La Lista de Reproducción.
			for Video_URL in vid_urls_in_playlist:
				download_Video(Ruta, Video_URL)
				time.sleep(1)
		
		else:	Modo_de_Uso()
		
	elif len(sys.argv) == 3:
		
		if sys.argv[1] == "-l" or sys.argv[1] == "--list":
			Dato = sys.argv[2]
			
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
			
			# Descarga los Videos de La Lista de Reproducción.
			for Video_URL in vid_urls_in_playlist:
				download_Video(Ruta, Video_URL)
				time.sleep(1)
			
		else:	Modo_de_Uso()
		
	elif len(sys.argv) == 2:
		
		if sys.argv[1] == "-h" or sys.argv[1] == "--help":
			Modo_de_Uso()
		elif sys.argv[1] == "-v" or sys.argv[1] =="--version":
			Dat()
		elif "https://www.youtube.com/" in sys.argv[1]:
			URLEnArgv = True
			Chk_URL()
		
		else:	Modo_de_Uso()
	
	elif len(sys.argv) == 1:
		Chk_URL()
	
	else:	Modo_de_Uso()
		


main()

HiddenCursor("Show")
