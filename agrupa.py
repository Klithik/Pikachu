import os
import shutil
from datetime import datetime

def iniciaRevision(target):
    if not (os.path.exists(target)):
        return False
    if not (os.path.isdir(target)):
        return False
    return os.listdir(target)

def creaFaltante(target):
    if not (os.path.exists(target)):
        os.mkdir(target)

def obtieneTipo(target):
    return os.path.splitext(target)[1][1:]

def obtieneAño(target):
    fecha = os.path.getmtime(target)
    fecha = datetime.fromtimestamp(fecha)
    return fecha.strftime("%Y")

def obtieneMes(target):
    fecha = os.path.getmtime(target)
    fecha = datetime.fromtimestamp(fecha)
    return fecha.strftime("%m")

def ordena(targetDir, destino, Ra, Rm, Rt):
    target = iniciaRevision(targetDir)
    if not (target):
        print("Directorio vacio")
        exit()
    for e in target:
        rutaTarget = os.path.join(targetDir, e)
        rutaDestino = destino
        if Ra:
            año = obtieneAño(rutaTarget)
            rutaDestino = os.path.join(rutaDestino, año)
            creaFaltante(rutaDestino)
        if Rt:
            if not (os.path.isfile(rutaTarget)):
                continue
            tipo = obtieneTipo(rutaTarget)
            rutaDestino = os.path.join(rutaDestino, tipo)
            creaFaltante(rutaDestino)
        if Rm:
            mes = obtieneMes(rutaTarget)
            rutaDestino = os.path.join(rutaDestino, mes)
            creaFaltante(rutaDestino)
        if rutaDestino != destino:
            shutil.move(rutaTarget, rutaDestino)

def mueve(origen, destino):
    shutil.move(origen, destino)

def inicia():
    print("Quieres ordenar por año?:")
    año = preguntaOpcion()
    mes = False
    if año:
        print("Quieres ordenar por mes?:")
        mes = preguntaOpcion()
    print("Quieres ordenar por tipo?:")
    tipo = preguntaOpcion()

    print("===Ingresa ruta de origen===")
    origen = verificaRuta()
    print("===Ingresa ruta de destino===")
    destino = verificaRuta()
    ordena(origen, destino, año, mes, tipo)

def verificaRuta():
    print("Respuesta...:")
    tmp = input()
    if not (iniciaRevision(tmp)):
        print("Intentalo de nuevo")
    return tmp

def preguntaOpcion():
    print("(s/n)")
    tmp = input()
    if tmp == "s":
        return True
    elif tmp == "n":
        return False
    else:
        print("Respuesta invalida")
        preguntaOpcion()
