nombres = []
clases = []
niveles = []
vidas = []
ataques = []
defensas = []
oros = []
estados = []
inventarios = []
# Stats base por clase
VIDA_GUERRERO = 150
ATAQUE_GUERRERO = 20
DEFENSA_GUERRERO = 15

VIDA_MAGO = 80
ATAQUE_MAGO = 35
DEFENSA_MAGO = 5

VIDA_ARQUERO = 100
ATAQUE_ARQUERO = 25
DEFENSA_ARQUERO = 10

ORO_INICIAL = 100
NIVEL_INICIAL = 1
def cargar_aventureros():
    archivo = open("aventureros.txt", "r")
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        nombres.append(partes[0])
        clases.append(partes[1])
        niveles.append(int(partes[2]))
        vidas.append(int(partes[3]))
        ataques.append(int(partes[4]))
        defensas.append(int(partes[5]))
        oros.append(int(partes[6]))
        estados.append(partes[7])
        inventarios.append(partes[8])
    archivo.close()
