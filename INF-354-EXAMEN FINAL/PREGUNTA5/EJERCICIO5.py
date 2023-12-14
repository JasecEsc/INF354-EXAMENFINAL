#PREGUNTA 5  QUEENS
import random

def generar_tablero(n):
    """Genera un tablero aleatorio."""
    return [random.randint(1, n) for _ in range(n)]

def calcular_ataques(tablero):
    """Calcula el número de ataques en el tablero."""
    n = len(tablero)
    ataques = 0
    for i in range(n):
        for j in range(i+1, n):
            # Verificar ataques en la misma fila o en diagonales
            if tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == j - i:
                ataques += 1
    return ataques

def cruzar_padres(padre1, padre2):
    """Realiza el cruce de dos padres para generar dos hijos."""
    punto_cruce = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

def mutar(individuo):
    """Realiza la mutación de un individuo."""
    indice_mutacion = random.randint(0, len(individuo) - 1)
    nuevo_valor = random.randint(1, len(individuo))
    individuo[indice_mutacion] = nuevo_valor
    return individuo

def seleccionar_padres(poblacion):
    """Selecciona dos padres mediante torneo."""
    torneo = random.sample(poblacion, min(3, len(poblacion)))
    torneo.sort(key=lambda x: calcular_ataques(x))
    return torneo[0], torneo[1]

def algoritmo_genetico(tamano_poblacion, tamano_tablero, probabilidad_cruce, probabilidad_mutacion, generaciones):
    poblacion = [generar_tablero(tamano_tablero) for _ in range(tamano_poblacion)]

    for generacion in range(generaciones):
        poblacion.sort(key=lambda x: calcular_ataques(x))

        if calcular_ataques(poblacion[0]) == 0:
            print(f"Solución encontrada en la generación {generacion}!")
            return poblacion[0]

        nueva_poblacion = []

        for _ in range(tamano_poblacion // 2):
            padre1, padre2 = seleccionar_padres(poblacion)
            hijo1, hijo2 = cruzar_padres(padre1, padre2)

            if random.random() < probabilidad_mutacion:
                hijo1 = mutar(hijo1)
            if random.random() < probabilidad_mutacion:
                hijo2 = mutar(hijo2)

            nueva_poblacion.extend([hijo1, hijo2])

        poblacion = nueva_poblacion

    print("Solución no encontrada. Mejor individuo:")
    print(poblacion[0])
    print("Número de ataques:", calcular_ataques(poblacion[0]))
    return poblacion[0]

# Parámetros del problema
tamano_tablero = 8
tamano_poblacion = 100
probabilidad_cruce = 0.7
probabilidad_mutacion = 0.2
generaciones = 1000

solucion = algoritmo_genetico(tamano_poblacion, tamano_tablero, probabilidad_cruce, probabilidad_mutacion, generaciones)
print("Solución final:")
print(solucion)
print("Número de ataques:", calcular_ataques(solucion))