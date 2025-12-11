import csv
import Paquetes.Funciones_Juego as Fj

categorias_CSV = {
    "nombre:":None,
    "1": None,
    "2": None,
    "3": None,
    "4": None,
    "5": None,
    "6": None,
    "escalera": None,
    "full": None,
    "poker": None,
    "generala": None,
    "total": None
}

def cargar_csv():
    with open("puntos.csv", "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["categoria", "puntos"])
        for cate in categorias_CSV:
            escritor.writerow([cate, None])
        
def cargar_nombre():
    with open("puntos.csv", "r", newline="") as archivo:
        lector = csv.DictReader(archivo)
        filas = list(lector)
    nombre = input("Ingrese su nombre: ").strip()
    for fila in filas:
        if fila["categoria"] == "nombre:":
            fila["puntos"] = nombre    

    with open("puntos.csv", "w", newline="") as archivo:
        campos = ["categoria", "puntos"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filas)



def csv_a_diccionario():
    datos = {}

    with open("puntos.csv", "r", newline="") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            categoria = fila["categoria"]
            puntos = fila["puntos"]

            
            if puntos.isdigit():
                puntos = int(puntos)

            datos[categoria] = puntos

    return datos

def total_puntos_csv():
    with open("puntos.csv", "r", newline="") as archivo:
        lector = csv.DictReader(archivo)
        filas = list(lector)

    total = 0

    for fila in filas:
        puntos = fila["puntos"]
        if puntos is None or puntos == "" or not puntos.isdigit():
            continue

        total += int(puntos)

    for fila in filas:
        if fila["categoria"].lower() == "total":
            fila["puntos"] = total
            break
 
    with open("puntos.csv", "w", newline="") as archivo:
        campos = ["categoria", "puntos"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filas)

    return total



def categoria_disponible(categoria):
    with open("puntos.csv", "r") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["categoria"] == categoria:
                return fila["puntos"] in ("", None)
    return False


def sumar_puntos(categoria_elegida, puntos):
    
    with open("puntos.csv", "r", newline="") as archivo:
        lector = csv.DictReader(archivo)
        filas = list(lector)

    for fila in filas:
        if fila["categoria"] == categoria_elegida:
            if fila["puntos"] == "":
                fila["puntos"] = puntos    

    with open("puntos.csv", "w", newline="") as archivo:
        campos = ["categoria", "puntos"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filas)


