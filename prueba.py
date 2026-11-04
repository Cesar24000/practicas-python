# Mi primer proyecto gestionado con Git y GitHub

def filtrar_y_duplicar(numeros):
    resultado = []
    for num in numeros:
        if num % 2 == 0:
            resultado.append(num * 2)
    return resultado

def contar_vocales(palabra):
    palabra = palabra.lower()
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador = 0

    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

def filtrar_palabras_largas(palabra, n):
    list = []
    for x in palabra:
        longitud = len(x)
        if longitud >= n:
            list.append(x)
    return list

ejemplo = ["python", "sol", "código", "ia"]
n = 4

print(filtrar_palabras_largas(ejemplo, n))