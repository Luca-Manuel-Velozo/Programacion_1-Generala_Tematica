import csv
import os
import Paquetes.Funciones_Juego as Fj

categorias_CSV = {
    "nombre:": None,
    "nivel:": None,
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
        
def cargar_nombre_y_nivel(nivel):
    with open("puntos.csv", "r", newline="") as archivo:
        lector = csv.DictReader(archivo)
        filas = list(lector)
    nombre = input("Ingrese su nombre: ").strip()
    while nombre == "":
        print("No puede dejar el campo vacío")
        nombre = input("Ingrese su nombre: ").strip()
    for fila in filas:
        if fila["categoria"] == "nombre:":
            fila["puntos"] = nombre
        if fila["categoria"] == "nivel:":
            fila["puntos"] = nivel  

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
        if fila["categoria"] == "total":
            continue
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


def puntos_ranking(jugador):
        return int(jugador["total"])

def act_ranking():
    nombre = None
    total = None

    with open("puntos.csv", "r", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["categoria"] == "nombre:":
                nombre = fila["puntos"]
            elif fila["categoria"] == "total":
                total = fila["puntos"]

    if nombre is None or total is None:
        print("Error: nombre o total no encontrados en puntos.csv")
        return

    total = int(total) 
    ranking = []
    jugador_existente = False

    if os.path.exists("Ranking.csv"):
        with open("Ranking.csv", "r", newline="") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                fila_total = int(fila["total"])

                if fila["nombre"] == nombre:
                    jugador_existente = True
                    fila_total = max(fila_total, total)

                ranking.append({
                    "nombre": fila["nombre"],
                    "total": fila_total
                })

    if not jugador_existente:
        ranking.append({"nombre": nombre, "total": total})

    ranking.sort(key=puntos_ranking,reverse=True)

    with open("Ranking.csv", "w", newline="") as archivo:
        campos = ["nombre", "total"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(ranking)

    print("Ranking actualizado correctamente.")

def leer_ranking():
    ranking = []
    contador = 0
    with open("Ranking.csv", "r", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            ranking.append(fila)
    
    ranking.sort(key=puntos_ranking,reverse=True)
    
    if not ranking:
        print("Ranking vacío, jugá para agregar entradas!")
    
    else:
        print("======== TOP 10 ========")
        for i in ranking:
            if contador == 10:
                break
            print(i)
            contador += 1
    input("=== PRESIONE ENTER PARA VOLVER AL MENÚ PRINCIPAL ===")
