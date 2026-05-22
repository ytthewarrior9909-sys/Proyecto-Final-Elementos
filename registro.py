from datos import nombres, clases, niveles, vidas, ataques, defensas, oros, estados, inventarios
from datos import VIDA_GUERRERO, ATAQUE_GUERRERO, DEFENSA_GUERRERO
from datos import VIDA_MAGO, ATAQUE_MAGO, DEFENSA_MAGO
from datos import VIDA_ARQUERO, ATAQUE_ARQUERO, DEFENSA_ARQUERO
from datos import ORO_INICIAL, NIVEL_INICIAL
def registro_aventurero():
    print('-------Registro de aventureros---------')
    nombre_aventurero1 = str(input("Digite el nombre del aventurero:"))
    print ('Si desea escoger Guerrero digite 1:')
    print ('Si desea escoger Mago digite 2:')
    print ('Si desea escoger Arquero digite 3:')
    clase_aventurero1 = int(input("Digite la clase deseada de su aventurero:"))
    if clase_aventurero1 == 1:
        clase = "Guerrero"
        vida = VIDA_GUERRERO
        ataque = ATAQUE_GUERRERO
        defensa = DEFENSA_GUERRERO
        oro = ORO_INICIAL
    elif clase_aventurero1 == 2:
        clase = "Mago"
        vida = VIDA_MAGO
        ataque = ATAQUE_MAGO
        defensa = DEFENSA_MAGO
        oro = ORO_INICIAL
    elif clase_aventurero1 == 3:
        clase = "Arquero"
        vida = VIDA_ARQUERO
        ataque = ATAQUE_ARQUERO
        defensa = DEFENSA_ARQUERO
        oro = ORO_INICIAL
    print(nombre_aventurero1)
    print('Su vida inicial es de', vida)
    print('Su ataque inicial es de', ataque)
    print('Su defensa inicial es de', defensa)
    print('Su oro inicial es de', oro)
registro_aventurero()
nombres.append(nombres)
clases.append(clases)
niveles.append(niveles)
vidas.append(vidas)
ataques.append(ataques)
defensas.append(defensas)
oros.append(oros)
estados.append('Vivo')
inventarios.append("")
guardar_aventureros() #PENDIENTE esto guarda el aventurero en TXT

