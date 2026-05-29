from registro import buscar_aventurero
from datos import oros, nombres, ataques, defensas, vidas, niveles
from registro import guardar_aventureros

def entrenamiento_aventureros():
    nombre = input("Ingrese el nombre del aventureros: ")
    busqueda = buscar_aventurero(nombre)
    if busqueda == -1:
        print('No existe el aventurero')
        return

    print('-------OPCIONES DE ENTRENAMIENTO---------')
    print('Oro disponible: ', oros[busqueda])
    print('1: Entrenar ataque, +5 de ataque -10 de oro:')
    print('2: Entrenar defensa, +3 de defensa -10 de oro:')
    print('3: Entrenar vida, +20 vida -50 de oro:')
    print('4: Subir de nivel, +1 nivel -100 de oro')
    print('5: Salir de la tienda')
    opcionEntrenamineto = int(input("Ingrese el numero de opcion deseade: "))
    if opcionEntrenamineto == 1:
        if oros[busqueda] >= 10:
            ataques[busqueda] = ataques[busqueda] + 5
            oros[busqueda] = oros[busqueda] - 10
            print('Su oro ahora es: ', oros[busqueda])
            print('su nuevo ataque es: ', ataques[busqueda])
            guardar_aventureros()
        else:
            print('No tienes suficiente oro')
            return

    elif opcionEntrenamineto == 2:
        if oros[busqueda] >= 10:
            defensas[busqueda] = defensas[busqueda] + 3
            oros[busqueda] = oros[busqueda] - 10
            print('Su oro ahora es: ', oros[busqueda])
            print('su nueva defensa es: ', ataques[busqueda])
            guardar_aventureros()
        else:
            print('No tienes suficiente oro')
            return
    elif opcionEntrenamineto == 3:
        if oros[busqueda] >= 20:
            vidas[busqueda] = vidas[busqueda] + 20
            oros[busqueda] = oros[busqueda] - 10
            print('Su oro ahora es: ', oros[busqueda])
            print('su nueva vida es: ', ataques[busqueda])
            guardar_aventureros()
        else:
            print('No tienes suficiente oro')
            return
    elif opcionEntrenamineto == 4:
        if oros[busqueda] >= 100:
            defensas[busqueda] = defensas[busqueda] *1,10
            ataques[busqueda] = ataques[busqueda] *1,10
            vidas[busqueda] = vidas[busqueda] * 1,20
            niveles[busqueda] = niveles[busqueda] + 1
            oros[busqueda] = oros[busqueda] - 100
            guardar_aventureros()
            print('Su oro ahora es: ', oros[busqueda])
            print('su nuevo nivel es: ', niveles[busqueda])
            print('su ataque y defensa subieron en 10%')
            print('Su vida subio u 20%')
        else:
            print('No tienes suficiente oro')
            return
    elif opcionEntrenamineto == 5:
        print('saliendo')
        return
