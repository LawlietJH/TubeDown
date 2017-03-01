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
		os.system("pip install pytube")# > Nul && cls")
		global PT
		PT = False
		return PT
		
	except Exception as ex:
		print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.

#~ os.system("pip uninstall pytube -y")# > Nul")

PT = True
Chk_Dep()
if PT: from pytube import *


def Ruta():
	
	Ruta = os.getcwd()
	
	if not os.path.exists(Ruta+"\Descargas"):
		os.mkdir(Ruta+"\Descargas")	
	
	os.chdir("Descargas")
	
	Ruta = os.getcwd()	
	
	return Ruta



xD = True

while xD:
	
	NomVid = input("URL: ")				#~ Escribimos la URL del Video a Descargar.

	Video = YouTube(NomVid)					#~ Se Obtienen Todas Las Calidades Posibles De Ese Video.

	#~ VideoHD = Video.get('mp4', '720p')		#Obtenemos el video mp4 de 720p.
	VideoHD = Video.filter('mp4')[-1]			#Obtenemos el video mp4 de mejor calidad posible.
	
	print("\n\n\n Video: ", VideoHD.filename)		#Se imprime el nombre del video.
	
	#~ VideoHD.download(r""+Ruta)				#Descargamos el video seleccionado.
	
	
