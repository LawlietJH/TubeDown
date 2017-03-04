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
#																v1.1.7

import urllib.request
import urllib.error

import time
import sys
import os
import re

Autor = "LawlietJH"
Version = "v1.1.7"

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
	
	Uso = """\n   Modo De Uso:\n\n\t\t TubeDown.py [-l URList.ext][-nr] | [-v] | [-h] | [URL]
	\n\n\t -l,  --list \t\t Se coloca el nombre del archivo\n\t\t\t\t para obtener la lista de URLs.
	\n\t -nr, --norepetir \t Se añade este argumento después\n\t\t\t\t de seleccionar el archivo de URLs.
	\n\t -v,  --version \t Muestra la versión y autor del Script.
	\n\n\t -h,  --help \t\t Muestra el Modo De Uso.
	\n\n https://www.youtube.com/...\t Se añade la URL como argumento y \n\t\t\t\t sólo se descargará ese video.
	\n\n\n   Ejemplos De Uso:\n\n\t\t   TubeDown.py  -l  xD.zion  -nr
	\n\n\t\t   TubeDown.py  http://www.youtube.com/video_etc...
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
		exit(0)
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
			exit(0)
			
		except Exception as ex:
			
			if type(ex).__name__ == "URLError":			#~ Si el tipo de error es URLError imprimirá algo en pantalla.
				print("\n\n\n\t\t [!] El URL no es válido... o Quizá No Hay Conexión...")
			elif type(ex).__name__ == "AgeRestricted":
				print("\n\n\n\t [!] Restricción de Edad.")
				
				resp = input("\n\n\n\t [¡] Quizá la URL es una Lista de Reproducción de Youtube [S/N]: ")
				
				if resp == "S" or resp == "s" or resp == "Si" or resp == "si" or resp == "SI" or resp == "sI":
					Modo_de_Uso()
					exit(0)
				else:
					exit(0)
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
			exit(0)
			
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
				exit(0)
			
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
			print("\n\n\n [+] Video: ", Video.filename, "\n\n")		#~ Se imprime el nombre del video.
			bar = BarraProgreso()
			VideoHD.download(r""+Ruta, on_progress=bar.Progreso, on_finish=bar.End)		#~ Descargamos el video seleccionado.
			os.system("Pause > Nul")
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
			exit(0)
			break
		
		except Exception as ex:
			print(type(ex).__name__)	#Si ocurre un error nuevo mostrara el nombre y no cerrará el programa.
			os.system("Pause > Nul")
	


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
#~ ============================================= FIN =======================================================================
#~ =========================================================================================================================





xD = True
NoRepetir = False
URLEnArgv = False
Cont = 0
Videos = []
Ruta = Ruta_Descargas()		#~ Obtenemos La Ruta Para Descargar el o los Videos deseados.

	

def main():
	
	os.system("cls")
	
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
				
				exit(0)
	
	elif len(sys.argv) == 3:
		
		if sys.argv[1] == "-l" or sys.argv[1] == "--list":
			Dato = sys.argv[2]
			
			Chk_txt(Dato)
			Open_txt(Dato)
			
			Chk_URL_Lista()
			
			exit(0)
		
	elif len(sys.argv) == 2:
		
		if sys.argv[1] == "-h" or sys.argv[1] == "--help":
			Modo_de_Uso()
		elif sys.argv[1] == "-v" or sys.argv[1] =="--version":
			Dat()
		elif "https://www.youtube.com/" in sys.argv[1]:
			URLEnArgv = True
			Chk_URL()
		else: 
			Modo_de_Uso()
	
	elif len(sys.argv) == 1:
		Chk_URL()
	
	else:
		Modo_de_Uso()

main()
HiddenCursor("Show")
