from datos import nombres, clases, niveles, vidas, ataques, defensas, oros, estados, inventarios
from datos import VIDA_GUERRERO, ATAQUE_GUERRERO, DEFENSA_GUERRERO
from datos import VIDA_MAGO, ATAQUE_MAGO, DEFENSA_MAGO
from datos import VIDA_ARQUERO, ATAQUE_ARQUERO, DEFENSA_ARQUERO
from datos import ORO_INICIAL, NIVEL_INICIAL

#def submenu_registro():
    #print ('-------Registro de aventureros---------')
    #print('Para registrar aventureros digite 1')
    #print('Para eliminar avent')





def registro_aventurero():
    print('-------Registro de aventureros---------')
    nombre = ""
    nombrev = 0
    while nombre == "" or nombrev != -1:
        nombre = input("Digite el nombre del aventurero:")
        nombre = nombre.strip()
        nombrev = consulte(nombre)
        if nombre == "":
            print("No se aceptan nombres vacíos.")
        elif nombrev != -1:
            print('El aventurero ya existe, por favor digite un nombre distinto')
    print('Las clases disponibles son:')
    print('Si desea escoger Guerrero digite 1:')
    print('Si desea escoger Mago digite 2:')
    print('Si desea escoger Arquero digite 3:')
    while True:
        try:
            clase_aventurero = int(input("Digite la clase deseada de su aventurero:"))
            if clase_aventurero == 1:
                clase = "Guerrero"
                vida = VIDA_GUERRERO
                ataque = ATAQUE_GUERRERO
                defensa = DEFENSA_GUERRERO
                oro = ORO_INICIAL
                break
            elif clase_aventurero == 2:
                clase = "Mago"
                vida = VIDA_MAGO
                ataque = ATAQUE_MAGO
                defensa = DEFENSA_MAGO
                oro = ORO_INICIAL
                break
            elif clase_aventurero == 3:
                clase = "Arquero"
                vida = VIDA_ARQUERO
                ataque = ATAQUE_ARQUERO
                defensa = DEFENSA_ARQUERO
                oro = ORO_INICIAL
                break
            print ('Digite una clase valida')
        except:
            print('No puede digitar texto, por favor digite una opción válida:')
    nombres.append(nombre)
    clases.append(clase)
    niveles.append(NIVEL_INICIAL)
    vidas.append(vida)
    ataques.append(ataque)
    defensas.append(defensa)
    oros.append(oro)
    estados.append("vivo")
    inventarios.append("")
    guardar_aventureros()
def guardar_aventureros():
    archivo = open('aventureros.txt', 'w')
    i = 0
    while i < len(nombres):
        linea = nombres[i] + ',' + clases[i] + ',' + str(niveles[i]) + ',' + str(vidas[i]) + "," + str(
            ataques[i]) + "," + str(defensas[i]) + "," + str(oros[i]) + "," + estados[i] + "," + inventarios[i] + "\n"
        archivo.write(linea)
        i += 1
    archivo.close()

def consulte(nombre):
    i = 0
    while i < len(nombres):
        if nombres[i] == nombre:
            return i
        i += 1
    return -1
def buscar_aventurero(nombre):
    i = 0
    while i < len(nombres):
        if nombres[i] == nombre:
            print('El nombre es: ', nombres[i])
            print('La clase es:', clases[i])
            print('El nivel es:', niveles[i])
            print('Su vida es:', vidas[i])
            print('Su ataque es:', ataques[i])
            print('Su defensa es:', defensas[i])
            print('Su oro es :', oros[i])
            print('Su estado es:', estados[i])
            print('Sus inventario es:', inventarios[i])
            print('Su posicion en la lista es', i + 1)
            return i
        i += 1
    print('El aventurero no existe')
    return -1

def ver_aventureros():
    if len(nombres) == 0:
        print('No existen aventureros')
    else:
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
def eliminar_aventurero():
    nombre = input("Digite el nombre del aventurero que desea eliminar:")
    aventurero = buscar_aventurero(nombre)
    if aventurero == -1:
        print("El  aventurero no existe")
        return
    else:
        nombres.pop(aventurero)
        clases.pop(aventurero)
        vidas.pop(aventurero)
        ataques.pop(aventurero)
        defensas.pop(aventurero)
        oros.pop(aventurero)
        estados.pop(aventurero)
        inventarios.pop(aventurero)
        niveles.pop(aventurero)
        guardar_aventureros()

# Felipe lo tiene que completar
# Tareas para Felipe:
# completar ver_aventureros
# completar buscar aventurero
# complet
