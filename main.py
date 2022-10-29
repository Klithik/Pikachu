import agrupa
import busca
import separa

opciones = {
    1:'1',
    2:'2',
    3:'3'
}

def revisaRespuesta(r):
    tmp = opciones.get(r,'Respuesta inválida, intenta otra vez')
    if tmp == r:
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
        agrupa.main()
    elif eleccion == '2':
        busca.inicia()
    elif eleccion == '3':
        separa.inicia()
    elif eleccion == '4':
        exit()
    
    print('¿Quieres hacer algo mas?')
    print('[1] Ordenar archivos por fecha y/o tipo')
    print('[2] Buscar un archivo o directorio')
    print('[3] Sacar todos los archivos de una carpeta')
    print('[4] Salir')
    eleccion = input()
    revisaRespuesta(eleccion)