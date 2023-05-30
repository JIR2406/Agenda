from datetime import datetime as dt
from time import time

def pintaMenu(arr,titulo:str) -> int:
    print("-----------{}-----------".format(titulo.upper()))
    for i in range(len(arr)):
        print("{}._ {}".format((i+1), arr[i].title()))

    opcion = input("Ingresa una opcion del menu: ")

    while not opcion.isnumeric():
        print("Caso inexistente")
        opcion = input("\nIngresa un numero entero positivo: ")

    return int(opcion)

def paresInfinitos(): # Evaluacion perezosa
    num = 0
    while True:
        if num % 2 == 0:
            yield num
            
        num += 1

def paresInfinitosNormal(x:int): # Demostracion sin la evaluacion perezosa
    cont = 0
    for i in range(0,100):
        if i % 2 == 0:
            print("El siguiente numero es: {}".format(i))
        else:
            cont+=1

        if cont == x:
            break
def insert(dic: dict, id: object) -> object:
    id = id + 1
    nombre:str = input("Ingresa el nombre: ")
    fecha = input("fecha de nacimiento en el formato DD-MM-YYYY \n")
    while not validaFecha(fecha):
        fecha = input("Ingresa una fecha valida en el formato DD-MM-YYYY \n")
    telefono = input("Ingresa el numero de telefono (10 digitos): ")
    while not telefono.isnumeric() or len(telefono) != 10:
        telefono = input("ingresa un numero de telefono valido de 10 digitos: ")
    correo = input("Ingresa el correo: ")
    while not "@" in correo or len(correo) < 15 or len(correo) > 30:
        correo = input("ingresa un correo que contenga el caracter '@' de entre 15 y 30 caracteres \n")

    dic[id] = [nombre, fecha, telefono, correo]
    return dic,id

def modificar(dic:dict, id):

    if id in dic:
        nombre: str = input("Ingresa el nombre: ")
        fecha = input("fecha de nacimiento en el formato DD-MM-YYY \n")
        while not validaFecha(fecha):
            fecha = input("Ingresa una fecha valida en el formato DD-MM-YYYY \n")
        telefono = input("Ingresa el numero de telefono (10 digitos): ")
        while not telefono.isnumeric() or len(telefono) != 10:
            telefono = input("ingresa un numero de telefono valido de 10 digitos: ")
        correo = input("Ingresa el correo: ")
        while not "@" in correo or len(correo) < 15 or len(correo) > 30:
            correo = input("ingresa un correo que contenga el caracter '@' de entre 15 y 30 caracteres \n")

        dic[id] = [nombre, fecha, telefono, correo]
        print("\ncontacto modificado...\n")

        return dic
    else:
        print("No se encontro este contacto en la agenda\n")
        return dic

def validaFecha(fecha):
    try:
        fecha_actual = dt.now().date() 
        fecha_ingresada = dt.strptime(fecha, "%d-%m-%Y").date() # Utilizamos el modulo date para validar la fecha

        if fecha_ingresada <= fecha_actual: # Comparamos si la fecha es menor a la fecha actual puesto que es fecha de nacimiento
            return True
        else:
            return False

    except ValueError:
        return False

def muestraAgenda(dic:dict):
    print("----------------------------")
    for id, datos in dic.items():
        print(f"ID: {id}")
        print(f"Nombre: {datos[0]}")
        print(f"Fecha: {datos[1]}")
        print(f"Teléfono: {datos[2]}")
        print(f"Correo: {datos[3]}")
        print("---------------------------\n")


if __name__ == '__main__':
    arrMenu = ["instertar","modificar","consultar","eliminar","otra","salir"]
    dic:dict = {}
    id:int = 0
    opcion:int = 0

    while opcion != len(arrMenu):
        opcion = pintaMenu(arrMenu, "menu")
        match opcion:
            case 1:
                dic,id = insert(dic, id)
                print("\ncontacto añadido...\n")
            case 2:
                auxId = input("\nIngresa el id del contacto a modificar(numerico): ")
                while not auxId.isnumeric():
                    auxId = input("\nerror, Ingresa un id valido del contacto a modificar(numerico): ")

                dic = modificar(dic,int(auxId))

            case 3:
                muestraAgenda(dic)

            case 4:
                auxId = input("\nIngresa el id del contacto a eliminar(numerico): ")
                while not auxId.isnumeric():
                    auxId = input("\nerror, Ingresa un id valido del contacto a modificar(numerico): ")
                if int(auxId) in dic.keys():
                    del dic[int(auxId)]
                    print("\ncontacto eliminado...\n")
                else:
                    print("No se encontro este contacto en la agenda\n")


            case 5:
                print("\nComo muestra de programa de evaluacion perezosa se hizo un programa que\n"
                      "genera numeros pares conforme es necesario, mientras que se solicite en el ciclo for ")
                lazy_func = paresInfinitos()

                tiempo_Ini=time()
                for i in range(1,10):
                    print("Siguiente numero: {}".format(next(lazy_func)))
                tiempo_Fin=time()
                tiempo_T=tiempo_Fin-tiempo_Ini

                print(f"Tiempo de ejecucion evaluacion perezosa: {tiempo_T}")
                print("\n-------- sin evaluacion perezos -----------")

                tiempo_ini = time() # Calculamos el tiempo de ejecucion de cada algoritmo
                paresInfinitosNormal(10) # Para poder compararlos
                tiempo_Fin = time()
                tiempo_T = tiempo_Fin - tiempo_Ini

                print(f"Tiempo de ejecucion sin evaluacion perezosa: {tiempo_T}")
                print("")

            case 6:
                print("\nSaliendo......")
                break
            case other:
                print("Por favor selecciona una opcion valida del menu\n")

