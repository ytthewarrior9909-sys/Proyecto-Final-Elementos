from registro import registro_aventurero, guardar_aventureros
from datos import cargar_aventureros
opcion = -1
cargar_aventureros()
while opcion != 0:
    print("=========== PYTHONIA RPG ===========")
    print("1. Registrar aventurero")
    print("2. Ver aventureros")
    print("3. Buscar aventurero")
    print("4. Entrenar aventurero")
    print("5. Tienda")
    print("6. Inventario")
    print("7. Batallas")
    print("8. Estadísticas")
    print("9. Ranking")
    print("0. Salir")
    print('====================================')
    opcion = int(input('Digite la opcion deseada: '))
    if opcion == 1:
        registro_aventurero()
        guardar_aventureros()