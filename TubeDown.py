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
	
	NomVid = input("URL: ")

	Video = YouTube(NomVid)

	VideoHD = Video.get('mp4', '720p')

	VideoHD.download(r""+Ruta)
	
	
