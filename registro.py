from datos import nombres, clases, niveles, vidas, ataques, defensas, oros, estados, inventarios
from datos import VIDA_GUERRERO, ATAQUE_GUERRERO, DEFENSA_GUERRERO
from datos import VIDA_MAGO, ATAQUE_MAGO, DEFENSA_MAGO
from datos import VIDA_ARQUERO, ATAQUE_ARQUERO, DEFENSA_ARQUERO
from datos import ORO_INICIAL, NIVEL_INICIAL


def registro_aventurero():
    print('-------Registro de aventureros---------')
    nombre_aventurero1 = str(input("Digite el nombre del aventurero:"))
    print('Las clases disponibles son:')
    print('Si desea escoger Guerrero digite 1:')
    print('Si desea escoger Mago digite 2:')
    print('Si desea escoger Arquero digite 3:')
    clase_aventurero1 = int(input("Digite la clase deseada de su aventurero:"))
    if clase_aventurero1 == 1:
        clase = "Guerrero"
        vida = VIDA_GUERRERO
        ataque = ATAQUE_GUERRERO
        defensa = DEFENSA_GUERRERO
    elif clase_aventurero1 == 2:
        clase = "Mago"
        vida = VIDA_MAGO
        ataque = ATAQUE_MAGO
        defensa = DEFENSA_MAGO
    elif clase_aventurero1 == 3:
        clase = "Arquero"
        vida = VIDA_ARQUERO
        ataque = ATAQUE_ARQUERO
        defensa = DEFENSA_ARQUERO
    oro = ORO_INICIAL
    nombres.append(nombre_aventurero1)
    clases.append(clase)
    niveles.append(NIVEL_INICIAL)
    vidas.append(vida)
    ataques.append(ataque)
    defensas.append(defensa)
    oros.append(oro)
    estados.append("vivo")
    inventarios.append("")
    # print(nombres)
    # print('Su clase es', clases)
    # print(nombre_aventurero1)
    # print('Su vida inicial es de', vida)
    # print('Su ataque inicial es de', ataque)
    # print('Su defensa inicial es de', defensa)
    # print('Su oro inicial es de', oro)


def guardar_aventureros():
    archivo = open('aventureros.txt', 'w')
    i = 0
    while i < len(nombres):
        linea = nombres[i] + ',' + clases[i] + ',' + str(niveles[i]) + ',' + str(vidas[i]) + "," + str(
            ataques[i]) + "," + str(defensas[i]) + "," + str(oros[i]) + "," + estados[i] + "," + inventarios[i] + "\n"
        archivo.write(linea)
        i += 1
    archivo.close()

def buscar_aventureros():
    i = 0
    while i < len(nombres):
        if nombres[i] == nombre:
            return i
        i += 1
    return -1


def ver_aventureros():
    i = 0
    while i < len(nombres):
        print("Nombre: ", nombres[i])
        print("clase: ", clases[i])
        print("Nivel: ", niveles[i])
        print("vidas: ", vidas[i])
        print("Ataque: ", ataques[i])
        print("Defensa: ", defensas[i])
        print("Oro: ", oros[i])
        print("Estado: ", estados[i])
        print("---------------------------------")
        i += 1
def eliminar_aventureros():
    nombre = input("Digite el nombre del aventurero que desea eliminar:")
    buscar_aventureros()
    if nombre == -1:
        print("El  aventurero no existe")
        return
    else:
        nombres.pop(po)
        clases.pop(clase)
        vidas.pop(vidas)
        ataques.pop(ataques)
        defensas.pop(defensas)
        oros.pop(oros)
        estados.pop(estados)
        inventarios.pop(inventarios)
# Felipe lo tiene que completar
# Tareas para Felipe:
# completar ver_aventureros
# completar buscar aventurero
# complet
