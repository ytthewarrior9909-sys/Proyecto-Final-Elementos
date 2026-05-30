# Proyecto Final – Introducción a la Programación en Python

# Sistema de Gestión de Aventureros RPG (Consola)

## Restricciones Generales

### NO utiliza:
- Interfaces gráficas
- Bases de datos
- Librerías avanzadas
- Librerías externas

### Solo se permite utilizar:
- Variables
- Condicionales (`if`)
- Ciclos (`while`, `for`)
- Listas
- Funciones
- Archivos `.txt`
- Todo lo visto en clase

---

# Objetivo General

Crear un sistema en consola donde el usuario pueda administrar héroes de un videojuego RPG.

El programa debe funcionar mediante un menú principal que se repita indefinidamente hasta que el usuario presione `0`.

---

# Contexto del Proyecto

El reino de **Pythonia** necesita un sistema para administrar aventureros.

Cada aventurero tendrá:

- Nombre
- Clase
- Nivel
- Vida
- Ataque
- Defensa
- Oro
- Inventario
- Estado (Vivo o Derrotado)

El usuario podrá:

- Crear personajes
- Ver personajes
- Eliminar personajes
- Entrenarlos
- Hacer batallas
- Comprar objetos
- Administrar inventarios
- Ver rankings
- Generar estadísticas

---

# Requisitos Técnicos Obligatorios

El proyecto debe utilizar:

- `while`
- `for`
- `if`
- Listas
- Funciones
- Menús
- Submenús
- Validaciones
- Archivos `.txt`

### Almacenamiento de datos

Todos los datos utilizados por el sistema deben:

- Guardarse en archivos `.txt`
- Leerse desde archivos `.txt`

---

# Restricciones

No se permite utilizar:

- tkinter
- pygame
- Interfaces gráficas
- Bases de datos
- Librerías externas

Todo debe realizarse únicamente mediante consola.

---

# Estructura General del Sistema

## Menú Principal

```text
=========== PYTHONIA RPG ===========

1. Registrar aventurero
2. Ver aventureros
3. Buscar aventurero
4. Entrenar aventurero
5. Tienda
6. Inventario
7. Batallas
8. Estadísticas
9. Ranking
0. Salir

====================================
```

El menú debe repetirse utilizando un ciclo `while`.

---

# Módulo 1 – Registrar Aventurero

Permite registrar nuevos héroes.

## Datos requeridos

- Nombre
- Clase
  - Guerrero
  - Mago
  - Arquero

## Valores iniciales

- Nivel = 1
- Vida según clase
- Ataque según clase
- Defensa según clase
- Oro inicial

---

## Estadísticas base por clase

### Guerrero

| Atributo | Valor |
|-----------|--------|
| Vida | 150 |
| Ataque | 20 |
| Defensa | 15 |

### Mago

| Atributo | Valor |
|-----------|--------|
| Vida | 80 |
| Ataque | 35 |
| Defensa | 5 |

### Arquero

| Atributo | Valor |
|-----------|--------|
| Vida | 100 |
| Ataque | 25 |
| Defensa | 10 |

---

## Validaciones

- No permitir nombres vacíos.
- No permitir nombres repetidos.
- Validar opciones del menú.
- Validar números negativos.

---

# Módulo 2 – Ver Aventureros

Mostrar todos los personajes registrados.

## Información mostrada

- Nombre
- Clase
- Nivel
- Vida
- Ataque
- Defensa
- Oro
- Estado

## Si no existen aventureros

```text
No hay aventureros registrados.
```

---

# Módulo 3 – Buscar Aventurero

Buscar un aventurero por nombre.

## Opciones

- Mostrar información completa.
- Mostrar si existe o no.
- Mostrar posición en la lista.

---

# Módulo 4 – Entrenamiento

Permite mejorar las estadísticas de un aventurero.

## Opciones

### Entrenar Ataque

Costo:

```text
10 oro
```

Beneficio:

```text
+5 ataque
```

---

### Entrenar Defensa

Costo:

```text
10 oro
```

Beneficio:

```text
+3 defensa
```

---

### Entrenar Vida

Costo:

```text
50 oro
```

Beneficio:

```text
+20 vida
```

---

### Subir Nivel

Costo:

```text
100 oro
```

Beneficio:

```text
+1 nivel
```

---

## Restricción

Si el aventurero no posee suficiente oro:

```text
Oro insuficiente
```

---

# Módulo 5 – Tienda

Permite comprar objetos.

Los efectos son permanentes.

## Objetos disponibles

| Objeto | Precio | Efecto |
|----------|----------|----------|
| Poción pequeña | 10 | +20 vida |
| Poción grande | 25 | +50 vida |
| Espada | 50 | +10 ataque |
| Escudo | 40 | +8 defensa |

---

## Requisitos

- Validar oro disponible.
- Restar el oro correspondiente.
- Agregar el objeto al inventario.

---

# Módulo 6 – Inventario

Cada personaje posee su propio inventario.

## Opciones

- Ver inventario
- Usar objeto
- Eliminar objeto

---

## Uso de objetos

Cuando un objeto es utilizado:

1. Se aplica el efecto.
2. Se elimina del inventario.

---

# Módulo 7 – Batallas

Permite enfrentar dos aventureros.

---

## Cálculo de daño

```text
Daño = Ataque - Defensa
```

Si el resultado es menor que 1:

```text
Daño = 1
```

---

## Sistema de combate

- Turnos alternos.
- Gana quien reduzca la vida del rival a 0.

---

## Ejemplo

```text
Turno 1

Carlos ataca a Ana

Daño realizado: 12

Vida restante Ana: 88
```

---

## Recompensas

El ganador obtiene:

- Oro
- Experiencia
- Subida de nivel opcional

---

# Módulo 8 – Estadísticas

El sistema debe mostrar:

- Total de aventureros
- Promedio de niveles
- Aventurero con más ataque
- Aventurero con más defensa
- Aventurero con más oro
- Cantidad de guerreros
- Cantidad de magos
- Cantidad de arqueros

---

# Módulo 9 – Ranking

Mostrar el Top 3 de aventureros por:

- Mayor nivel
- Mayor ataque
- Mayor oro

---

# Requisitos Técnicos Avanzados

El proyecto debe:

- Utilizar funciones.
- Evitar repetir código.
- Utilizar ciclos correctamente.
- Realizar búsquedas en listas.
- Aplicar validaciones adecuadas.

---

# Organización Recomendada (4 Semanas)

## Semana 1

- Menú principal
- Registro de aventureros
- Mostrar aventureros
- Validaciones

---

## Semana 2

- Entrenamiento
- Tienda
- Inventario

---

## Semana 3

- Batallas
- Rankings
- Estadísticas

---

## Semana 4

- Corrección de errores
- Mejoras
- Extras
- Preparación de la presentación final

---

# Entregables

## 1. Código Fuente

Archivo:

```text
proyecto_final.py
```

---

## 2. Video Explicativo

Debe explicar:

- Funciones utilizadas
- Estructuras utilizadas
- Problemas encontrados
- Soluciones implementadas

---

# Rúbrica de Evaluación

| Criterio | Valor |
|-----------|---------|
| Menús funcionales | 15% |
| Uso correcto de ciclos | 15% |
| Uso correcto de listas | 15% |
| Validaciones | 15% |
| Modularización con funciones | 15% |
| Batallas funcionales | 10% |
| Estadísticas y rankings | 10% |
| Orden y legibilidad | 5% |

---

# Nombre sugerido del proyecto

**Pythonia RPG – Sistema de Gestión de Aventureros**
