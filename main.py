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

def obtieneMes(target):
    fecha = os.path.getmtime(target)
    fecha = datetime.fromtimestamp(fecha)
    return fecha.strftime('%m')

def main(targetDir,destino,Ra,Rm,Rt):
    target = iniciaRevision(targetDir)
    for e in target:
        rutaTarget = path.join(targetDir,e)
        if(Rt):
            tipo = obtieneTipo(rutaTarget)
            rutaDestino = path.join(destino,tipo)
            if(not(verificaDir(rutaDestino))):
                mkdir(rutaDestino)
            if(Ra):
                año = obtieneAño(rutaTarget)
                rutaDestino = path.join(rutaDestino,año)
                if(not(verificaDir(rutaDestino))):
                    mkdir(rutaDestino)
                if(Rm):
                    mes = obtieneMes(rutaTarget)
                    rutaDestino = path.join(rutaDestino,mes)
                    if(not(verificaDir(rutaDestino))):
                        mkdir(rutaDestino)
                    shutil.move(rutaTarget,rutaDestino)
            else:
                shutil.move(rutaTarget,rutaDestino)
        elif(Ra):
            año = obtieneAño(rutaTarget)
            rutaDestino = path.join(destino,año)
            if(not(verificaDir(rutaDestino))):
                mkdir(rutaDestino)
            if(Rm):
                mes = obtieneMes(rutaTarget)
                rutaDestino = path.join(rutaDestino,mes)
                if(not(verificaDir(rutaDestino))):
                    mkdir(rutaDestino)
                shutil.move(rutaTarget,rutaDestino)
            else:
                shutil.move(rutaTarget,rutaDestino)
    print('Listo!')
    dibuja()

def dibuja():
    print('    _______________________¶¶¶¶___¶¶¶¶¶')
    print('_____________________¶¶____¶¶¶____¶¶__¶¶¶')
    print('___________________¶¶___¶¶¶____¶¶¶¶¶¶¶___¶¶')
    print('_________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶')
    print('______________¶¶¶¶¶__¶__________________________¶¶')
    print('___________¶¶¶¶__¶¶__¶___________________________¶')
    print('_________¶¶¶_¶¶__¶__¶¶¶__________________________¶')
    print('______¶¶¶_¶¶_¶¶¶_¶_¶¶_¶¶_________¶_______________¶')
    print('_____¶_¶¶__¶_¶_¶¶¶¶_¶¶¶__________¶¶______________¶')
    print('___¶¶¶_¶¶¶¶¶_¶¶¶¶¶¶_¶¶¶_________¶¶¶______________¶')
    print('_¶¶__¶¶¶¶¶¶¶¶_¶¶_¶¶____________¶¶¶¶¶_____________¶')
    print('¶_¶¶__¶__¶¶¶¶____¶¶___________¶¶¶¶¶¶¶____________¶')
    print('¶__¶¶¶¶¶¶¶¶¶¶____¶¶__________¶¶¶¶¶¶¶¶¶¶__________¶')
    print('_¶¶¶_¶_¶¶___¶¶___¶¶________¶¶¶¶¶¶¶¶¶¶¶¶¶_________¶')
    print('__¶¶_¶¶_¶___¶¶___¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶')
    print('___¶¶____¶___¶___¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶')
    print('____¶¶___¶¶__¶¶__¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶')
    print('_____¶¶___¶__¶¶__¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶')
    print('______¶¶___¶__¶__¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶')
    print('_______¶¶__¶¶_¶__¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶')
    print('________¶¶__¶_¶¶_¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶')
    print('_________¶¶__¶_¶_¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶')
    print('__________¶¶_¶¶¶_¶¶___¶¶¶¶¶¶¶¶¶__¶¶__¶¶¶¶¶¶¶¶¶___¶')
    print('____________¶_¶¶_¶¶_____¶¶¶¶¶____¶¶____¶¶¶¶¶_____¶')
    print('_____________¶_¶¶¶¶___________¶¶¶¶¶¶¶¶___________¶')
    print('______________¶¶¶¶¶__________¶¶¶¶¶¶¶¶¶¶______¶¶__¶')
    print('_______________¶¶¶____________¶¶¶¶¶¶¶¶_______¶¶¶_¶')
    print('________________¶¶__________________________¶¶_¶_¶')
    print('_________________¶¶__________________________¶¶__¶')
    print('_________________¶¶__________________________¶¶¶_¶')
    print('__________________¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶')
    print('__________________¶¶¶¶¶¶¶¶¶¶¶¶')
    print('_____________________¶¶¶¶¶¶')

def pregunta():
    año = False
    mes = False
    tipo = False
    año = preguntaAño()
    if(año):
        mes = preguntaMes()
    tipo = preguntaTipo()
    main(origen,destino,año,mes,tipo)
    print('Elige direccion para organizar:')
    direccion = input()
    print('Elige donde poner los archivos ordenados por año:')
    dirF = input()
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
    if(input()=='s'):
        OrgAño = True
        return True
    elif(input()=='n'):
        OrgAño = False
        return False
    else:
        print('Respuesta invalida')
        preguntaAño()

def preguntaMes():
    print('Quieres organizar los archivos por mes? (s/n)')
    if(input()=='s'):
        OrgMes = True
        return True
    elif(input()=='n'):
        OrgMes = False
        return False
    else:
        print('Respuesta invalida')
        preguntaMes()

def preguntaTipo():
    print('Quieres organizar los archivos por tipo? (s/n)')
    if(input()=='s'):
        OrgTipo = True
        return True
    elif(input()=='n'):
        OrgTipo = False
        return False
    else:
        print('Respuesta invalida')
        preguntaTipo()

#/home/klithik/Imágenes/Capturas de pantalla