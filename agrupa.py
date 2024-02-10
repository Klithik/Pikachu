from datetime import datetime
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
    print('Este directorio no es valido')
    return False

def mueveArchivo(old,new):
    if(os.replace(old,new)):
        return True
    return False

def obtieneTipo(target):
    return path.splitext(target)[1][1:]

def obtieneAño(target):
    fecha = os.path.getmtime(target)
    fecha = datetime.fromtimestamp(fecha)
    return fecha.strftime('%Y')

def obtieneMes(target):
    fecha = os.path.getmtime(target)
    fecha = datetime.fromtimestamp(fecha)
    return fecha.strftime('%m')

def ordena(targetDir,destino,Ra,Rm,Rt):
    target = iniciaRevision(targetDir)
    if(not(target)):
        print('Directorio vacio')
        exit()
    for e in target:
        rutaTarget = path.join(targetDir,e)
        if(Ra):
            año = obtieneAño(rutaTarget)
            rutaDestino = path.join(destino,año)
            if(not(verificaDir(rutaDestino))):
                mkdir(rutaDestino)
            if(Rm):
                mes = obtieneMes(rutaTarget)
                rutaDestino = path.join(rutaDestino,mes)
                if(not(verificaDir(rutaDestino))):
                    mkdir(rutaDestino)
                if(Rt):
                    if path.isfile(rutaTarget):
                        tipo = obtieneTipo(rutaTarget)
                        rutaDestino = path.join(rutaDestino,tipo)
                        if(not(verificaDir(rutaDestino))):
                            mkdir(rutaDestino)
                        shutil.move(rutaTarget,rutaDestino)
                else:
                    shutil.move(rutaTarget,rutaDestino)
            else:
                shutil.move(rutaTarget,rutaDestino)
        elif(Rt):
            if path.isfile(rutaTarget):
                tipo = obtieneTipo(rutaTarget)
                rutaDestino = path.join(destino,tipo)
                if(not(verificaDir(rutaDestino))):
                    mkdir(rutaDestino)
                shutil.move(rutaTarget,rutaDestino)
    print('Listo!')

def inicia():
    print('Quieres ordenar por año?:')
    año = preguntaOpcion()
    mes = False
    if(año):
        print('Quieres ordenar por mes?:')
        mes = preguntaOpcion()
    print('Quieres ordenar por tipo?:')
    tipo = preguntaOpcion()
    
    print('===Ingresa ruta de origen===')
    origen = verificaRuta()
    print('===Ingresa ruta de destino===')
    destino = verificaRuta()
    ordena(origen,destino,año,mes,tipo)

def verificaRuta():
    print('Respuesta...:')
    tmp = input()
    if(not(verificaDir(tmp))):
        print('Intentalo de nuevo')
        verificaRuta()
    return tmp

def preguntaOpcion():
    print('(s/n)')
    tmp = input()
    if(tmp=='s'):
        return True
    elif(tmp=='n'):
        return False
    else:
        print('Respuesta invalida')
        preguntaOpcion()
