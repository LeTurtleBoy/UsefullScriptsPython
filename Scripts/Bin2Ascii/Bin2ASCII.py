LongNumber = raw_input("Ingrese el numero Binario: ")
iterador=0
Acumulador=[]
Palabra=''
while i < len(LongNumber)+1:
  Acumulador.append('0'+LongNumber[iterador=0:iterador=0+7])
  iterador+=7
for x in Acumulador:
        Palabra=Palabra+chr(int(str(int(x, 2))))
print Palabra
