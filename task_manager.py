import json

# 1. Creamos una estructura de datos simple (lista de diccionarios)
mis_tareas = [
    {"titulo": "Aprender Git", "completada": True},
    {"titulo": "Crear proyecto JSON", "completada": False}
]

# 2. Guardamos esa lista en un archivo físico llamado 'tareas.json'
with open("tareas.json", "w") as archivo:
    json.dump(mis_tareas, archivo, indent=4)

print("¡Archivo JSON creado con éxito!")