import os
import subprocess
import shutil
import tkinter as tk
from tkinter import filedialog

GUÍAS_PATH = "Guías"

def inicializar_repositorio():
   
    if not os.path.exists(GUÍAS_PATH):
        os.makedirs(GUÍAS_PATH)

def listar_guias():

    print("Guías disponibles:")
    guias = os.listdir(GUÍAS_PATH)
    for i, guia in enumerate(guias, start=1):
        print(f"{i}. {guia}")

def abrir_guia(nombre_guia):

    if nombre_guia in os.listdir(GUÍAS_PATH):
        ruta_guia = os.path.join(GUÍAS_PATH, nombre_guia)
        try:
            subprocess.Popen([ruta_guia], shell=True)
        except Exception as e:
            print(f"No se pudo abrir la guía '{nombre_guia}': {e}")
    else:
        print(f"La guía '{nombre_guia}' no existe en el repositorio.")

def descargar_guia(nombre_guia):
    
    if nombre_guia in os.listdir(GUÍAS_PATH):
        ruta_guia = os.path.join(GUÍAS_PATH, nombre_guia)
        root = tk.Tk()
        root.withdraw()  
        ruta_destino = filedialog.asksaveasfilename(
            initialfile=nombre_guia,
            defaultextension=".pdf",
            filetypes=[("Todos los archivos", "*.*")],
            title="Guardar Guía como..."
        )
def subir_guias(rutas_archivos):
    for ruta_archivo in rutas_archivos:
      
        nombre_archivo = os.path.basename(ruta_archivo)
       
        if nombre_archivo in os.listdir(GUÍAS_PATH):
            print(f"Ya existe una guía con el nombre '{nombre_archivo}'.")
        else:
            
            destino = os.path.join(GUÍAS_PATH, nombre_archivo)
            try:
                shutil.copyfile(ruta_archivo, destino)
                print(f"Guía '{nombre_archivo}' subida correctamente.")
            except FileNotFoundError:
                print(f"El archivo '{ruta_archivo}' no existe.")
def eliminar_guia(nombre_guia):

    if nombre_guia in os.listdir(GUÍAS_PATH):
        ruta_guia = os.path.join(GUÍAS_PATH, nombre_guia)
        try:
            os.remove(ruta_guia)
            print(f"Guía '{nombre_guia}' eliminada correctamente.")
        except Exception as e:
            print(f"No se pudo eliminar la guía '{nombre_guia}': {e}")
    else:
        print(f"La guía '{nombre_guia}' no existe en el repositorio.")

def main():
    print("Bienvenido al visualizador de guías para estudiantes.")
    while True:
        print("\nOpciones disponibles:")
        print("1. Listar guías disponibles")
        print("2. Subir guías")
        print("3. Abrir una guía")
        print("4. Descargar una guía")
        print("5. Eliminar una guía")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            listar_guias()
        elif opcion == '2':
            rutas = input("Ingrese las rutas de los archivos que desea subir (separadas por comas): ")
            rutas_archivos = [ruta.strip() for ruta in rutas.split(',')]
            subir_guias(rutas_archivos)
        elif opcion == '3':
            nombre_guia = input("Ingrese el nombre de la guía que desea abrir: ")
            abrir_guia(nombre_guia)
        elif opcion == '4':
            nombre_guia = input("Ingrese el nombre de la guía que desea descargar: ")
            descargar_guia(nombre_guia)
        elif opcion == '5':
            nombre_guia = input("Ingrese el nombre de la guía que desea eliminar: ")
            eliminar_guia(nombre_guia)
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    inicializar_repositorio()
    main()


