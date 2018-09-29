def string_decode(input, length=8):
 	input_l = [input[i:i+length] for i in range(0,len(input),length)]
 	return ''.join([chr(int(c,base=2)) for c in input_l])

def Decode(Data):
 	cnt = 0
 	actual = ""
 	vector = []
 	solucion = ""
 	for elemento in Data:
 	 	for i in elemento:
 	 	 	if i == "0":
 	 	 	 	actual = "0"
 	 	 	if i == "1":
 	 	 	 	actual = "1" 	  
 	 	 	if i == "!":
 	 	 	 	cnt +=1
 	 	 	if i == "@":
 	 	 	 	vector = [actual]*cnt
 	 	 	 	vector = ''.join(str(i) for i in vector)
 	 	solucion = solucion + str(vector)
 	 	cnt = 0
 	return string_decode(solucion)

Archivo = open("informacion.txt")
Info = Archivo.read()
print("Informacion Original")
print(Info)
Data = Info.replace("KEK","0")
Data = Data.replace("TOP","1")
Data = Data.replace(" ","@ ")
Data = Data.split(" ")
print ("-------------------------------------------")
Sol1 = Decode(Data)
print(Sol1)
print("-------------------------------------------")
Data2 = Info.replace("KEK","1")
Data2 = Data2.replace("TOP","0")
Data2 = Data2.replace(" ","@ ")
Data2 = Data2.split(" ")
Sol2 = Decode(Data2)
print(Sol2)

