import json

ARCHIVO_TAREAS = "tareas.json"

def cargar_tareas():
    """Lee las tareas desde el archivo JSON. Si no existe o esta vacio, regresa una lista vacia."""
    try:
        with open(ARCHIVO_TAREAS, "r") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        # Si el archivo no existe O si esta vacio/corrupto, regresamos una lista vacia
        return []

def guardar_tareas(tareas):
    """Guarda la lista de tareas en el archivo JSON."""
    with open(ARCHIVO_TAREAS, "w") as archivo:
        json.dump(tareas, archivo, indent=4)

def mostrar_tareas(tareas):
    """Imprime las tareas numeradas en la consola."""
    if not tareas:
        print("\n No hay tareas registradas.")
        return

    print("\n--- LISTA DE TAREAS ---")
    for i, tarea in enumerate(tareas, 1):
        estado = "[✓]" if tarea["completada"] else "[ ]"
        print(f"{i}. {estado} {tarea['titulo']}")

def agregar_tarea(tareas):
    """Pide al usuario el nombre de una tarea y la agrega a la lista."""
    titulo = input("\nEscribe la descripción de la tarea: ").strip()
    if titulo:
        tareas.append({"titulo": titulo, "completada": False})
        guardar_tareas(tareas)
        print(f" Tarea '{titulo}' agregada con éxito.")
    else:
        print(" La tarea no puede estar vacía.")

def marcar_completada(tareas):
    """Cambia el estado de una tarea a completada."""
    mostrar_tareas(tareas)
    if not tareas:
        return

    try:
        num = int(input("\nIngresa el número de la tarea que completaste: "))
        if 1 <= num <= len(tareas):
            tareas[num - 1]["completada"] = True
            guardar_tareas(tareas)
            print(" ¡Tarea marcada como completada!")
        else:
            print(" Número de tarea inválido.")
    except ValueError:
        print(" Por favor ingresa un número válido.")

def menu_principal():
    """Bucle principal del programa."""
    tareas = cargar_tareas()

    while True:
        print("\n==============================")
        print("    GESTOR DE TAREAS CLI    ")
        print("==============================")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Salir")

        opcion = input("\nSelecciona una opción (1-4): ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            print("\n ¡Hasta luego!")
            break
        else:
            print(" Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()