import csv


categorias_CSV = {
    "1": None,
    "2": None,
    "3": None,
    "4": None,
    "5": None,
    "6": None,
    "escalera": None,
    "full": None,
    "poker": None,
    "generala": None
}

with open("puntos.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["categoria", "puntos"])
    for cate in categorias_CSV:
        escritor.writerow([cate, ""])

def sumar_puntos(categoria_elegida, puntos):
    
    with open("puntos.csv", "r", newline="") as archivo:
        lector = csv.DictReader(archivo)
        filas = list(lector)

    for fila in filas:
        if fila["categoria"] == categoria_elegida:
            if fila["puntos"] == "":
                fila["puntos"] = puntos    
#falta validacion de categorias ya elegidas

    with open("puntos.csv", "w", newline="") as archivo:
        campos = ["categoria", "puntos"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filas)


