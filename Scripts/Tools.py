import os
import re

class tools():
	def __init__(self):
		pass


	def search(self, argv=None):
		try:
			len(argv)
		except:
			argv = [argv]
		print(len(argv))

		if (len(argv) == 4):
			Ruta = argv[0]
			Tipo= argv[1]
			Extension= argv[2]
			Palabra= argv[3]
			if Tipo == "1":
				for path, dirs, files in os.walk(Ruta):
					print(Ruta)
					for file in os.listdir(path):
						if file.endswith(Extension):
							Archivo  = open(path+"\\"+file,'r')
							Archivo = Archivo.read() 
							match = re.search(Palabra, Archivo)
							if match:
								print('\"',Palabra,'\"', " Encontrado en: ",path+"\\"+file," en la pos: ", match.start(), "\n")
				return()
			if Tipo == "2":
				for path, dirs, files in os.walk(Ruta):
					for file in os.listdir(path):
						if file.startswith(Extension):
							Archivo  = open(path+"\\"+file,'r')
							Archivo = Archivo.read() 
							match = re.search(Palabra, Archivo)
							if match:
								print('\"',Palabra,'\"', " Encontrado en: ",path+"\\"+file," en la pos: ", match.start(), "\n")
				return()
			else:
				print ("Mal Formato, Intente de Nuevo")
				return()
		if (len(argv) == 3):
				Ruta = argv[0]
				Tipo= argv[1]
				Extension= argv[2]	
				if Tipo == "3":
					for path, dirs, files in os.walk(Ruta):
						for file in os.listdir(path):
							if file.endswith(Extension):
								print (path+"\\"+file)
					return()
				if Tipo == "4":
					for path, dirs, files in os.walk(Ruta):
						for file in os.listdir(path):
							if file.startswith(Extension):
								print (path+"\\"+file)
					return()
				else:
					print ("Mal Formato, Intente de Nuevo 1")
					return()
		if argv == [None]:
			print ("Search Format: " + "OptionSearch, Main Folder, filename extension, Common Term")
			print("Argument 1:")
			print ("\t#: 1 - Search content that finish whit some name in all subfolders")
			print ("\t#: 2 - Buscar contenido de archivos que comiencen en una Palabra en todos los subdirectorios y contengan un Termino")
			print ("\t#: 3 - Buscar Archivos que Terminen en una Extension")
			print ("\t#: 4 - Buscar contenido de Comiencen con una palabra")

Tool = tools()

Ruta = "/"
Tipo = "2"
Extension = "py"
Palabra = ""
Tool.search([Ruta,Tipo,Extension,Palabra])