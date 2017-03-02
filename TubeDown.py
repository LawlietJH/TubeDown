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
import os


def Chk_Dep():
	
	try:
		import pytube
		
	except ModuleNotFoundError:
		print("\n\n\t[!] Instalando Dependencias...\n\n\t\t")
		os.system("pip install pytube > Nul && cls")
		
	except Exception as ex:
		print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.

#~ os.system("pip uninstall pytube -y")# > Nul")


Chk_Dep()
from pytube import *
#~ from pprint import pprint

#~ print(dir(YouTube.filter))

def Ruta():
	
	Ruta = os.getcwd()							#~ Se Obtiene La Ruta Actual Del Script
	
	if not os.path.exists(Ruta+"\Descargas"):	#~ Comprobamos si existe la Carpeta de Descargas.
		os.mkdir(Ruta+"\Descargas")				#~ Creamos La Carpeta de descargas si No existe.
	
	os.chdir("Descargas")						#~ Nos Situamos En La Carpeta De Descargas 
	
	Ruta = os.getcwd()							#~ Guardamos La Ruta.
	
	return Ruta



xD = True

Ruta = Ruta()			#~ Obtenemos La Ruta Para Descargar el o los Videos deseados.

while xD:
	
	Cont = 0
	try:
		URLVid = input("\n\n\n\t URL: ")		#~ Escribimos la URL del Video a Descargar.
		Video = YouTube(URLVid)					#~ Se Obtienen Todas Las Calidades Posibles De Ese Video.
		#~ VideoHD = Video.get('mp4', '720p')		#~ Obtenemos el video mp4 de 720p.
		VideoHD = Video.filter('mp4')[-1]			#~ Obtenemos el video mp4 de mejor calidad posible.
		Nomb = Nombre = VideoHD.filename
		
		while xD:
			
			try:
				#~ if not os.path.exists(Video.filename):
					
				print("\n\n\n Video: ", Video.filename)	#~ Se imprime el nombre del video.
				VideoHD.download(r""+Ruta)				#~ Descargamos el video seleccionado.
				break
					
				#~ VideoHD.download(r""+Ruta)					#~ Si ya existe el video se provoca el error para que aumente el contador.
				
			except OSError:
				Cont += 1
				Video.set_filename(Nombre+" ("+str(Cont)+")")	#~ Se añade al nombre (#) un numero para evitar repetición.
			
			except Exception as ex:
				print(type(ex).__name__)	#Si ocurre un error nuevo mostrara el nombre y no cerrará el programa.
	
		print("\n\n Descargado!\n")
		
	except ValueError:
		print("\n\n\n\t\t No es una URL...")
		
	except IndexError:
		print("\n\n\n\t\t Escribe una URL...")	
		
	except Exception as ex:
		
		if type(ex).__name__ == "URLError":			#~ Si el tipo de error es URLError imprimirá algo en pantalla.
			print("\n\n\n\t\t URL no válido...")
		else:
			print("\n\n\n\t\t",type(ex).__name__)	#Si ocurre un error nuevo mostrara el nombre y no cerrará el programa.
	
	
