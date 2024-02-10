import shutil
import os

def revisaDir(ruta):
    if os.path.exists(ruta):
        if os.path.isdir(ruta):
            return os.listdir(ruta)
    return False

def main(origen,destino):
    lista = revisaDir(origen)
    for e in lista:
        if os.path.isfile(e):
            source = os.path.join(origen,e)
            shutil.move(source,destino)
        else:
            source = os.path.join(origen,e)
            main(source,destino)

def preguntaRuta():
    print('Que directorio quieres separar: ')
    ruta = input()
    if not(revisaDir(ruta)):
        print('Ruta no valida')
        preguntaRuta()

def preguntaDestino():
    print('Donde quieres dejar los archivos: ')
    ruta = input()
    if not(revisaDir(ruta)):
        print('Ruta no valida')
        preguntaRuta()

def inicio():
    ruta = preguntaRuta()
    destino = preguntaDestino()
    print('==SEPARANDO==')
    main(ruta,destino)
    print('==TERMINADO==')
