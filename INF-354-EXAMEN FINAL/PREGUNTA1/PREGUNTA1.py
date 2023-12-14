archivo = r"C:\Users\Desktop\Desktop\EXAMEN354\Life_Expectancy_00_15.csv"
sumas = {}
contadores = {}

columnas_especificadas = [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
for i in columnas_especificadas:
    sumas[i] = 0
    contadores[i] = 0

with open(archivo, 'r') as f:
    next(f)

    for linea in f:
        campos = linea.strip().split(',')

        for i in columnas_especificadas:
            valor = float(campos[i])
            sumas[i] += valor
            contadores[i] += 1

for i in columnas_especificadas:
    if contadores[i] > 0:
        media = sumas[i] / contadores[i]
        print(f"La media de la columna {i} es:", media)
    else:
        print(f"No se encontraron datos en la columna {i}.")

modas = {}

columnas_especificadas = [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
for i in columnas_especificadas:
    modas[i] = None

valores_columna = {}
for i in columnas_especificadas:
    valores_columna[i] = []

with open(archivo, 'r') as f:
    next(f)

    for linea in f:
        campos = linea.strip().split(',')

        for i in columnas_especificadas:
            valor = float(campos[i])
            valores_columna[i].append(valor)

for i in columnas_especificadas:
    if valores_columna[i]:
        valores = valores_columna[i]
        moda = max(valores, key=valores.count)
        modas[i] = moda
        print(f"La moda de la columna {i} es:", moda)
    else:
        print(f"No se encontraron datos en la columna {i}.")

def calcular_cuantil(datos, p):
    n = len(datos)
    datos_ordenados = sorted(datos)
    posicion = (n - 1) * p
    parte_entera = int(posicion)
    fraccion = posicion - parte_entera
    if parte_entera == n - 1:
        return datos_ordenados[parte_entera]
    else:
        return datos_ordenados[parte_entera] + fraccion * (datos_ordenados[parte_entera + 1] - datos_ordenados[parte_entera])

percentiles = [25, 50, 75]

for i in columnas_especificadas:
    if valores_columna[i]:
        datos = valores_columna[i]
        cuantiles = [calcular_cuantil(datos, p / 100) for p in percentiles]
        print(f"Cuartiles y percentiles de la columna {i} son:")
        for p, q in zip(percentiles, cuantiles):
            print(f"{p}th percentil: {q}")
    else:
        print(f"No se encontraron datos en la columna {i}.")
