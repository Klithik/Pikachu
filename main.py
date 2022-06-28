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

def obtieneMes(target):
    fecha = os.path.getmtime(target)
    fecha = datetime.fromtimestamp(fecha)
    return fecha.strftime('%m')

def main(targetDir,destino,Ra,Rm,Rt):
    target = iniciaRevision(targetDir)
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

def pregunta():
    año = preguntaAño()
    mes = False
    if(año):
        mes = preguntaMes()
    tipo = preguntaTipo()

    origen = preguntaOrigen()
    destino = preguntaDestino()
    main(origen,destino,año,mes,tipo)

def preguntaOrigen():
    print('Elige el directorio a organizar')
    tmp = input()
    if(verificaDir(tmp)):
        return tmp
    else:
        print('Ruta invalida')
        preguntaOrigen()

def preguntaDestino():
    print('Elige el directorio a donde mover los archivos')
    tmp = input()
    if(verificaDir(tmp)):
        return tmp
    else:
        print('Ruta invalida')
        preguntaDestino()

def preguntaAño():
    print('Quieres organizar los archivos por año? (s/n)')
    tmp = input()
    if(tmp=='s'):
        return True
    elif(tmp=='n'):
        return False
    else:
        print('Respuesta invalida')
        preguntaAño()

def preguntaMes():
    print('Quieres organizar los archivos por mes? (s/n)')
    tmp = input()
    if(tmp=='s'):
        return True
    elif(tmp=='n'):
        return False
    else:
        print('Respuesta invalida')
        preguntaMes()

def preguntaTipo():
    print('Quieres organizar los archivos por tipo? (s/n)')
    tmp = input()
    if(tmp=='s'):
        return True
    elif(tmp=='n'):
        return False
    else:
        print('Respuesta invalida')
        preguntaTipo()

pregunta()