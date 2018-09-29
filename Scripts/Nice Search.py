# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 17:16:25 2017

@author: chris
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
this program will search for any file "by his name or his extension" using a recursive search from a root directory, also can search for coincidences of terms into those files.

LTB
Hope you like.
'''
import os
import re
import sys

def main():
    if (len(sys.argv) == 5):
            Ruta = sys.argv[1]
            Tipo= sys.argv[2]
            Extension= sys.argv[3]
            Palabra= sys.argv[4]
            if Tipo == "1":
                for path, dirs, files in os.walk(Ruta):
                    for file in os.listdir(path):
                        if file.endswith(Extension):
                            Archivo  = open(path+"\\"+file,'r')
                            Archivo = Archivo.read() 
                            match = re.search(Palabra, Archivo)
                            if match:
                                print '\"',Palabra,'\"', " Encontrado en: ",path+"\\"+file," en la pos: ", match.start(), "\n"
                return()
            if Tipo == "2":
                for path, dirs, files in os.walk(Ruta):
                    for file in os.listdir(path):
                        if file.startswith(Extension):
                            Archivo  = open(path+"\\"+file,'r')
                            Archivo = Archivo.read() 
                            match = re.search(Palabra, Archivo)
                            if match:
                                print '\"',Palabra,'\"', " Encontrado en: ",path+"\\"+file," en la pos: ", match.start(), "\n"
                return()
            else:
                print "Mal Formato, Intente de Nuevo"
                return()
    if (len(sys.argv) == 4):
            Ruta = sys.argv[1]
            Tipo= sys.argv[2]
            Extension= sys.argv[3]    
            if Tipo == "3":
                for path, dirs, files in os.walk(Ruta):
                    for file in os.listdir(path):
                        if file.endswith(Extension):
                            print path+"\\"+file
                return()
            if Tipo == "4":
                for path, dirs, files in os.walk(Ruta):
                    for file in os.listdir(path):
                        if file.startswith(Extension):
                            print path+"\\"+file
                return()
            else:
                print "Mal Formato, Intente de Nuevo 1"
                return()
    else:
        print "Mal Formato, Intente de Nuevo 2"
        return()
    
if len(sys.argv) == 1:
    print "Formato: " + "Directorio-Carpeta-Madre # Extension  Termino-a-Buscar"
    print "#: 1 - Buscar contenido de archivos que terminen en una Palabra en todos los subdirectorios y contengan un Termino"
    print "#: 2 - Buscar contenido de archivos que comiencen en una Palabra en todos los subdirectorios y contengan un Termino"
    print "#: 3 - Buscar Archivos que Terminen en una Extension"
    print "#: 4 - Buscar contenido de Comiencen con una palabra"
else:
    if __name__ == "__main__":
        main()

