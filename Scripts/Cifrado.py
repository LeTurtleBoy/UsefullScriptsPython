class Chipher():
	def __init__(self):
		self._abecedario = "abcdefghijklmnñopqrstuvwxyz"
		self._abecedario2= "abcdefghijklmnñopqrstuvwxyz"
		self._coder = ["a4","14","1f","1d","cb","c2","cd","ab","c4","cf","ad","af","12","a2","3b","32","3d","34","3f","1b","eb","e2","ed","e4","ef"]
		self._clave = "dfec"
		self.Final = ""

	def Chiph(self, message):
		Cifrado = ""
		I = 0
		for x in message: 
			if x == " ":
				self.Final += " "
			else:
				Mod_clave=I%len(self._clave)

				Asignada=self._clave[Mod_clave] 
				Sumando=self._abecedario.find(x)+self._abecedario.find(Asignada) 
				Modulo=(Sumando%25)
				self.Final=self.Final+self._abecedario[Modulo] 
				I=I+1
		for y in self.Final:
			if (y == " "):
				Cifrado += " "
			else:
				pos= self._abecedario2.find(y)
				Cifrado = Cifrado + self._coder[pos]
		return(Cifrado)

Message = "Hallo"

print(Chipher().Chiph(Message))
