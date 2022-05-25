from datetime import datetime
from ntpath import join
import os
from os import path,mkdir
import shutil

def iniciaRevision(target):
    if(verificaDir(target)):
        return os.listdir(target)
    return False

def verificaDir(target):
    if(path.exists(target)):
        if(path.isdir(target)):
            return True
    return False

def mueveArchivo(old,new):
    if(os.replace(old,new)):
        return True
    return False

def obtieneTipo(target):
    return path.splitext(target)[1]

def obtieneAño(target):
    fecha = os.path.getmtime(target)
    fecha = datetime.fromtimestamp(fecha)
    return fecha.strftime('%Y')

def iteraDir(targetDir,destino):
    target = iniciaRevision(targetDir)
    destinos = []
    for e in target:
        rutaTarget = path.join(targetDir,e)
        year = obtieneAño(rutaTarget)
        rutaYear = path.join(destino,year)
        if(not(verificaDir(rutaYear))):
            mkdir(rutaYear)
            destinos.append(rutaYear)
        destinoFinal = join(rutaYear,e)
        shutil.move(rutaTarget,rutaYear)
    return destinos

#/home/klithik/Imágenes/Capturas de pantalla
print('Elige direccion para organizar:')
direccion = input()
print('Elige donde poner los archivos ordenados por año:')
dirF = input()
if(verificaDir(direccion)):
    if(verificaDir(dirF)):
        tipos = iteraDir(direccion,dirF)
    else:
        print('Ruta invalida')
else:
    print('Ruta invalida')