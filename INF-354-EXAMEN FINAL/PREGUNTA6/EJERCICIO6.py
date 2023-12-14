#EJERICIO 6
def calcular_diferencia(texto1, texto2):
    # Convertir ambas cadenas a minúsculas para hacer la comparación insensible a mayúsculas
    texto1 = texto1.lower()
    texto2 = texto2.lower()

    # Calcular la longitud mínima entre las dos cadenas
    longitud_minima = min(len(texto1), len(texto2))

    # Contar el número de caracteres diferentes
    diferencias = sum(c1 != c2 for c1, c2 in zip(texto1[:longitud_minima], texto2[:longitud_minima]))

    # Calcular la diferencia total tomando en cuenta la longitud de las cadenas
    diferencia_total = diferencias + abs(len(texto1) - len(texto2))

    # Normalizar la diferencia para obtener una puntuación entre 0 y 1 (0 indica similitud completa)
    similitud = 1 - diferencia_total / max(len(texto1), len(texto2), 1)

    return similitud

# Ejemplos de textos
texto_original = "Mabru se fue a la guerra"
texto_modificado = "MaNSSDDbru se fue aS la guerra"

# Calcular similitud
similitud = calcular_diferencia(texto_original, texto_modificado)

# Mostrar resultados
print(f"Texto original: {texto_original}")
print(f"Texto modificado: {texto_modificado}")
print(f"Similitud: {similitud}")
