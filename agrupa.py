from datetime import datetime
import os
import shutil

def iniciaRevision(target):
    if not(os.path.exists(target)):
        return False
    if not(os.path.isdir(target)):
        return False
    return os.listdir(target)

def creaFaltante(target):
    if not(os.path.exists(target)):
        os.mkdir(target)

def obtieneTipo(target):
    return os.path.splitext(target)[1][1:]

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
    if not(target):
        print('Directorio vacio')
        exit()
    for e in target:
        rutaTarget = os.path.join(targetDir,e)
        if(Ra):
            año = obtieneAño(rutaTarget)
            rutaDestino = os.path.join(destino,año)
            creaFaltante(rutaDestino)
            if(Rm):
                mes = obtieneMes(rutaTarget)
                rutaDestino = os.path.join(rutaDestino,mes)
                creaFaltante(rutaDestino)
                if(Rt):
                    if os.path.isfile(rutaTarget):
                        tipo = obtieneTipo(rutaTarget)
                        rutaDestino = os.path.join(rutaDestino,tipo)
                        creaFaltante(rutaDestino)
        elif(Rt):
            if not(os.path.isfile(rutaTarget)):
                continue
            tipo = obtieneTipo(rutaTarget)
            rutaDestino = os.path.join(destino,tipo)
            creaFaltante(rutaDestino)
        # REVISA QUE AL MENOS UNA SELECCION
        # SEA VERDADERA ANTES DE INTENTAR MOVER EL ARCHIVO
        try:
            shutil.move(rutaTarget,rutaDestino)
        except NameError:
            break
    print('Listo!')

def mueve(origen,destino):
    shutil.move(origen,destino)

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
    if not(iniciaRevision(tmp)):
        print('Intentalo de nuevo')
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
