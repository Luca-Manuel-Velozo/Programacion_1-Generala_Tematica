import json
import Paquetes.Funciones_CSV as Fcsv

def guardar_json_partida():
    datos = Fcsv.csv_a_diccionario()

    partida = {
        "categorias": {k: v for k, v in datos.items() if k != "nombre"}
    }

    with open("partida.json", "w", encoding="utf-8") as archivo:
        json.dump(partida, archivo, indent=4)

    print("Partida guardada en JSON correctamente.")






