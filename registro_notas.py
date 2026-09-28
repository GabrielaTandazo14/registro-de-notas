# ------------------ 1. CREAR LA COLECCIÓN ---------------
# Usamos un DICCIONARIO para relacionar nombre con notas
registro_notas = {}

# ------------------ 2. FUNCIÓN AGREGAR DATOS ------------
def agregar_estudiante(nombre, nota):
    """Agrega un estudiante y su nota al registro"""
    registro_notas[nombre] = nota
    print(f"Estudiante '{nombre}' agregado con nota: {nota}")

# ------------------ 3. FUNCIÓN MOSTRAR TODOS ------------
def mostrar_registro():
    """Muestra todos los estudiantes y sus notas"""
    print("\n=== REGISTRO DE NOTAS ===")
    if registro_notas:
        for nombre, nota in registro_notas.items():
            print(f"📌 {nombre} → Nota: {nota}")
    else:
        print(" El registro está vacío")
    print("=========================\n")

# ------------------ 4. FUNCIÓN BUSCAR ESTUDIANTE --------
def buscar_estudiante(nombre):
    """Busca la nota de un estudiante"""
    if nombre in registro_notas:
        print(f" {nombre} tiene nota: {registro_notas[nombre]}")
    else:
        print(f" '{nombre}' no está en el registro")

# ------------------ 5. FUNCIÓN ELIMINAR ESTUDIANTE ------
def eliminar_estudiante(nombre):
    """Elimina un estudiante del registro"""
    if nombre in registro_notas:
        eliminado = registro_notas.pop(nombre)
        print(f" Estudiante '{nombre}' eliminado. Nota era: {eliminado}")
    else:
        print(f" No se encontró a '{nombre}'")

# ------------------ 6. EJEMPLO DE USO -------------------
if __name__ == "__main__":
    # Agregar estudiantes
    agregar_estudiante("Ana", 16)
    agregar_estudiante("Luis", 14)
    agregar_estudiante("Gabriel", 18)

    # Mostrar todo
    mostrar_registro()

    # Buscar uno
    buscar_estudiante("Luis")

    # Eliminar uno
    eliminar_estudiante("Ana")

    # Mostrar después de eliminar
    mostrar_registro()