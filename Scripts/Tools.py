import os
import re

class Wintools():
	def __init__(self):
		pass

	def Help(self):
		print('functions of the class Wintools by LeTurtleBoy:')
		print('\tSearch(Folder ,Type ,Extension ,Word):')
		print("\t\tFolder: str")
		print("\t\t\tThis argument is the main folder to look at for those files, if is empty we have the local folder as main folder")
		print("\t\tType: int")
		print ("\t\t\t#: 1 - Search for files that have the word 'Word' in it, the extension equals to 'Extension' and that are located in the main folder")
		print ("\t\t\t#: 2 - Search for files that have the word 'Word' in it, the extension equals to 'Extension' and that are located in the main folder or any subfolder")
		print ("\t\t\t#: 3 - Search for files that have the extension equals to 'Extension' and that are located in the main folder")
		print ("\t\t\t#: 4 - Search for files that have the extension equals to 'Extension' and that are located in the main folder or any subfolder")
		print("\t\tExtension: str")
		print ("\t\t\tExtension to search")
		print("\t\tWord: str")
		print ("\t\t\tWord to search")
		print("\n\n")
		pass
		
	'''
	First lets build some nice control error functions
	'''
	#integrer
	def _set_Int(self, value):
		if not isinstance(value, int):
			raise TypeError("Type must be set to an integer")
		else:
			if ((value>4) | (value<1)):
				raise ValueError("Must be 1,2,3 or 4")
			else:
				return value

	#string
	def _set_Str(self, value):
		if (value == ""):
			value = os.getcwd()
		if not isinstance(value, str):
			print("Ruta: ", value)
			raise TypeError("Type must be set to an valid string")
		else:
			return value

	#Basic Term Search
	def _basicTermSearch(self,Folder,Extension,Word):
		try:
			for path, dirs, files in os.walk(Folder):
				del dirs, files
				for file in os.listdir(path):
					if file.endswith(Extension):
						Archivo  = open(path+"\\"+file,'r')
						Archivo = Archivo.read() 
						match = re.search(Word, Archivo)
						if match:
							print('\"',Word,'\"', " found in: \'",Folder+"\\"+file,"\' in the character: ", match.start(), "\n")
			return 1
		except:
			print("Error")
			return 0

	def search(self,Folder = os.getcwd(),Type = 1 ,Extension = '',Word = ''):
		self.Type = self._set_Int(Type)
		self.Folder = self._set_Str(Folder)
		self.Word = self._set_Str(Word)
		self.Extension = self._set_Str(Extension)

		if self.Word != '':
			if self.Type == 1:
				print("Searching for", Extension, "files, that contains ",Word)
				self._basicTermSearch(self.Folder,self.Extension,self.Word)

			if self.Type == 2:
				print("Searching for", self.Extension, "files, that contains ",self.Word, " in all the subfolders of", self.Folder)
				for path, dirs, files in os.walk(self.Folder):
					if dirs == []:
						dirs = '\\'
						self._basicTermSearch(path+dirs,self.Extension,self.Word)
					else: 
						self._basicTermSearch(path,self.Extension,self.Word)

		if self.Type == 3:
			print("Searching for", self.Extension, "files, in ", self.Folder)
			for path, dirs, files in os.walk(self.Folder):
				for file in files:
					if file.endswith(Extension):
						print (path+"\\"+file)
				return()
		if Type == 4:
			print("Searching for", self.Extension, "files, in ", self.Folder, 'and his subfolders')
			for path, dirs, files in os.walk(self.Folder):
				for file in files:
					if file.endswith(Extension):
						print (path+"\\"+file)
			return()

Tool = Wintools()
#Tool.Help()
Tool.search("",4,".py","Chris")