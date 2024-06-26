import shutil
import os

def revisaDir(ruta):
    if not(os.path.exists(ruta)):
        print('Ruta no valida')
        return False
    if not(os.path.isdir(ruta)):
        print('Ruta no valida')
        return False
    return os.listdir(ruta)

def separa(origen,destino):
    lista = revisaDir(origen)
    if not(lista):
        print('Directorio vacio')
        exit()
    for e in lista:
        if os.path.isfile(e):
            source = os.path.join(origen,e)
            shutil.move(source,destino)
        else:
            source = os.path.join(origen,e)
            separa(source,destino)
            os.removedirs(source)

def preguntaRuta():
    ruta = input()
    if not(revisaDir(ruta)):
        print('Intentalo de nuevo')
        preguntaRuta()

def inicio():
    print('Que directorio quieres dividir?:')
    ruta = preguntaRuta()
    print('Donde quieres guardar los archivos?:')
    destino = preguntaRuta()
    print('==SEPARANDO==')
    separa(ruta,destino)
    print('==TERMINADO==')
