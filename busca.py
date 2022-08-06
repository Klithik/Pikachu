from operator import contains
import os

resultados = []

def revisaDir(lugar,target):
    lista = os.listdir(lugar)
    if contains(lista,target):
        respuesta = os.path.join(lugar,target)
        resultados.append(respuesta)
    else:
        for e in lista:
            ruta_tmp = os.path.join(lugar,e)
            if os.path.isdir(ruta_tmp):
                revisaDir(ruta_tmp)
    return resultados

def preguntaRuta():
    print('Desde que directorio de origen quieres buscar: ')
    ruta = input()
    if os.path.exists(ruta):
        if os.path.isdir(ruta):
            return ruta
    print('Ruta no valida')
    preguntaRuta()

def inicia():
    ruta = preguntaRuta()
    print('Nombre de archivo o carpeta a buscar: ')
    target = input()

    print('==BUSCANDO==')
    revisaDir(ruta,target)

    if resultados:
        print('RESULTADOS: ')
        for e in resultados:
            print(e)
    else:
        print('No encontrado :c')