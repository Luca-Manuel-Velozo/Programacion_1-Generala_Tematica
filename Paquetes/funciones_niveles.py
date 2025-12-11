import json

def cargar_niveles():
    with open("niveles.json", "r", encoding="utf-8") as archivo:
        lista_niveles = json.load(archivo)
    return lista_niveles

def seleccionar_nivel():
    niveles = cargar_niveles()
    print("\n--- SELECCIÓN DE NIVEL ---")
    indice = 1
    for nivel in niveles:
        print(f"{indice}. {nivel['nombre']}")
        indice += 1
    
    
    while True:
        opcion = input("Elige un nivel: ")
        if opcion.isdigit():
            opcion_num = int(opcion)
            if 1 <= opcion_num <= len(niveles):
                return niveles[opcion_num - 1]
            else:
                print("debe ingresar un nivel por su indice")