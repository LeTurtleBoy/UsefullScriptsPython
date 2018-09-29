Abecedario = "abcdefghijklmnopqrstuvwxyz" 
Abecedario2 = "abcdefghjklmnopqrstuvwxyz" 
coder = ("a4","14","1f","1d","cb","c2","cd","ab","c4","cf","ad","af","12","a2","3b","32","3d","34","3f","1b","eb","e2","ed","e4","ef")
Mensaje = raw_input("Ingresa el Mensaje a Cifrar: ").lower() 
Clave = "dfec"
Final = ""
Cifrado = ""
I = 0  
 
for x in Mensaje: 
    if x == " ":
        Final += " "
    else:
        if (x == "i"):
            x = "j"
        Mod_clave=I%len(Clave)
        Asignada=Clave[Mod_clave] 
        Sumando=Abecedario.find(x)+Abecedario.find(Asignada) 
        Modulo=(Sumando%25)
        Final=Final+Abecedario[Modulo] 
        I=I+1

print Final

for y in Final:
    if (y == " "):
        Cifrado += " "
    else:
        pos= Abecedario2.find(y)
        #print pos
        #print Abecedario[pos]
        Cifrado = Cifrado + coder[pos]
    
print Cifrado

        