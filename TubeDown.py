# Lista De Casos De Posibles Usos:
#~ print("\n\n", yt.get_videos())
#~ print("\n\n", yt.filename)
#~ yt.set_filename('Video 1 - Metasploit Framework') #~ Para renombrar el archivo de salida
#~ print("\n\n", yt.filename)
#~ print("\n\n", yt.filter('mp4'))
#~ print("\n\n", yt.filter('mp4')[-1])
#~ print("\n\n", yt.filter(resolution='720p'))
#~ print("\n\n", video)
#~ print("\n\n", yt.videos)
#~ video = yt.get('mp4')
#~ print("\n\n", VideoHD)

#~ ================================================================================================

import sys
import os


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
	
	Uso = """\n   Modo De Uso:\n\n\t\t TubeDown.py [-l URList.ext] | [-h]
	\n\n\t -l, --list \t\t Se coloca el nombre del archvo\n\t\t\t\t para obtener la lista de URLs.
	\n\t -h, --help \t\t Muestra el Modo De Uso.
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
			print("\n\n\n\t\t No es una URL...")
			
		except IndexError:								#~ Por si no se escribe nada.
			print("\n\n\n\t\t Escribe una URL...")	
			
		except KeyboardInterrupt:						#~ Por si cancela la operación con "Ctrl + C".
			Ctrl_C()
			exit(0)
			
		except Exception as ex:
			
			if type(ex).__name__ == "URLError":			#~ Si el tipo de error es URLError imprimirá algo en pantalla.
				print("\n\n\n\t\t El URL no es válido... o No Hay Conexión...")
			else:
				print("\n\n\n\t\t",type(ex).__name__)	#Si ocurre un error nuevo mostrara el nombre y no cerrará el programa.


def Chk_URL_Lista():
	
	for URL in Videos:
		
		global Cont
		Cont = 0
		
		try:
			
			Download_Lista(URL)			#~ Método para descargar videos.
			
		except ValueError:								#~ Por si se escribe algo que no sea una URL
			print("\n\n\n\t\t No es una URL...")
			
		except IndexError:								#~ Por si no se escribe nada.
			print("\n\n\n\t\t Escribe una URL...")	
			
		except KeyboardInterrupt:						#~ Por si cancela la operación con "Ctrl + C".
			Ctrl_C()
			exit(0)
			
		except Exception as ex:
			
			if type(ex).__name__ == "URLError":			#~ Si el tipo de error es URLError imprimirá algo en pantalla.
				print("\n\n\n\t\t El URL no es válido... o No Hay Conexión...")
			else:
				print("\n\n\n\t\t",type(ex).__name__)	#Si ocurre un error nuevo mostrara el nombre y no cerrará el programa.
				


def Ctrl_C():
	print("\n\n\t\t Cancelado...")
	try:
		os.system("timeout /nobreak 03 > Nul")
		return
	except KeyboardInterrupt:
		Ctrl_C()


def Open_txt(X):
	
	global Videos
	
	Archivo = open(X,"r")	#~ Se abre el archivo.
	
	for linea in Archivo:
		Videos.append(linea)	#~ Se añade cada URL del archivo a la lista .
	

def Download():
	
	global Cont
	
	URLVid = input("\n\n\n\t URL: ")		#~ Escribimos la URL del Video a Descargar.	
	Video = YouTube(URLVid)					#~ Se Obtienen Todas Las Calidades Posibles De Ese Video.
	#~ VideoHD = Video.get('mp4', '720p')		#~ Obtenemos el video mp4 de 720p.
	VideoHD = Video.filter('mp4')[-1]			#~ Obtenemos el video mp4 de mejor calidad posible.
	Nomb = Nombre = VideoHD.filename
	
	while xD:
		
		try:
			print("\n\n\n Video: ", Video.filename)		#~ Se imprime el nombre del video.
			VideoHD.download(r""+Ruta)					#~ Descargamos el video seleccionado.
			break
			
		except OSError:
			Cont += 1
			Video.set_filename(Nombre+" ("+str(Cont)+")")	#~ Se añade al nombre (#) un numero para evitar repetición.
			
		except KeyboardInterrupt:						#~ Por si cancela la operación con "Ctrl + C".
			Ctrl_C()
			break
		
		#~ except UnboundLocalError:
			#~ print("\n\n\t Video Repetido...\n")
			#~ break
		
		except Exception as ex:
			print(type(ex).__name__)	#Si ocurre un error nuevo mostrara el nombre y no cerrará el programa.
		
	print("\n\n\t\t Descargado!\n")


def Download_Lista(URLVid):
		
	global Cont
	
	Video = YouTube(URLVid)					#~ Se Obtienen Todas Las Calidades Posibles De Ese Video.
	#~ VideoHD = Video.get('mp4', '720p')		#~ Obtenemos el video mp4 de 720p.
	VideoHD = Video.filter('mp4')[-1]			#~ Obtenemos el video mp4 de mejor calidad posible.
	Nomb = Nombre = VideoHD.filename
	
	while xD:
		
		try:
			print("\n\n\n Video: ", Video.filename)		#~ Se imprime el nombre del video.
			VideoHD.download(r""+Ruta)					#~ Descargamos el video seleccionado.
			break
			
		except OSError:
			Cont += 1
			Video.set_filename(Nombre+" ("+str(Cont)+")")	#~ Se añade al nombre (#) un numero para evitar repetición.
			
		except KeyboardInterrupt:						#~ Por si cancela la operación con "Ctrl + C".
			Ctrl_C()
			break
		
		#~ except UnboundLocalError:
			#~ print("\n\n\t Video Repetido...\n")
			#~ break
		
		except Exception as ex:
			print(type(ex).__name__)	#Si ocurre un error nuevo mostrara el nombre y no cerrará el programa.
		
	print("\n\n\t\t Descargado!\n")
	


xD = True
Cont = 0
Videos = []
Ruta = Ruta_Descargas()		#~ Obtenemos La Ruta Para Descargar el o los Videos deseados.

	

def main():
	
	HiddenCursor("Hide")
	
	if len(sys.argv) == 3:
		
		if sys.argv[1] == "-l" or sys.argv[1] == "--list":
			Dato = sys.argv[2]
			
			Chk_txt(Dato)
			Open_txt(Dato)
			
			Chk_URL_Lista()
		
	elif len(sys.argv) == 2:
		
		if sys.argv[1] == "-h" or sys.argv[1] == "--help":
			Modo_de_Uso()
		else: 
			Modo_de_Uso()
	
	elif len(sys.argv) == 1:
		Chk_URL()
	
	else:
		Modo_de_Uso()

main()
HiddenCursor("Show")
