import agrupa
import busca
import separa

opciones = {
    1:'1',
    2:'2',
    3:'3',
    4:'4'
}

def revisaRespuesta(r):
    tmp = opciones.get(r,True)
    print(tmp)
    if tmp:
        return tmp
    else:
        print(tmp)
        nueva_r = input()
        revisaRespuesta(nueva_r)

print('Bienvenido a Pikachu 3. ¿Que accion quieres realizar?')
print('[1] Ordenar archivos por fecha y/o tipo')
print('[2] Buscar un archivo o directorio')
print('[3] Sacar todos los archivos de una carpeta')
print('[4] Salir')
eleccion = input()
revisaRespuesta(eleccion)

while(True):
    if eleccion == '1':
        agrupa.inicia()
    elif eleccion == '2':
        busca.inicia()
    elif eleccion == '3':
        separa.inicio()
    elif eleccion == '4':
        exit()
