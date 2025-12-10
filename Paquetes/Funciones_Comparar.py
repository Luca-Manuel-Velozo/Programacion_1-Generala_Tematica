import Paquetes.Funciones_CSV as Fcsv
def jugadas_1_6(NUM, dados_def):
    puntos = 0
    for i in dados_def:
        if NUM == i:
            puntos += NUM
    return puntos

def jugadas_posibles(dados_def, jugada, nivel):
    dados_def.sort()
    escalera1 = [1,2,3,4,5]
    escalera2 = [2,3,4,5,6]
    if jugada == "escalera":
        if dados_def == escalera1 or dados_def == escalera2:
            return nivel["puntos"]["escalera"]
        else:
            return 0
    elif jugada == "full":
        if dados_def[0]==dados_def[1] and dados_def[1]==dados_def[2] and dados_def[3] == dados_def[4]:
            if dados_def[2] != dados_def[3]:
               return nivel["puntos"]["full"]
            else:
                return 0
        elif dados_def[0]==dados_def[1] and dados_def[2]==dados_def[3] and dados_def[3] == dados_def[4]:
            if dados_def[1] != dados_def[2]:
                return nivel["puntos"]["full"]
            else: 
                return 0
        else:
            return 0
    elif jugada == "poker":
        if dados_def[0]==dados_def[1] and dados_def[1]==dados_def[2] and dados_def[2] == dados_def[3]:
            return nivel["puntos"]["poker"]
        elif dados_def[1]==dados_def[2] and dados_def[2]==dados_def[3] and dados_def[3] == dados_def[4]:
            return nivel["puntos"]["poker"]
        else:
            return 0
    elif jugada == "generala":
        if dados_def[0]==dados_def[1] and dados_def[1]==dados_def[2] and dados_def[2] == dados_def[3] and dados_def[3] == dados_def[4]:
            return nivel["puntos"]["generala"]
        else: return 0

def comparacion_mano(dados_def, nivel):
    UNOS = jugadas_1_6(1, dados_def)
    DOSES = jugadas_1_6(2, dados_def)
    TRESES = jugadas_1_6(3, dados_def)
    CUATROS = jugadas_1_6(4,dados_def)
    CINCOS = jugadas_1_6(5, dados_def)
    SEISES = jugadas_1_6(6, dados_def)
    ESCALERA = jugadas_posibles(dados_def, "escalera", nivel)
    FULL = jugadas_posibles(dados_def, "full", nivel )
    POKER = jugadas_posibles(dados_def, "poker", nivel)
    GENERALA = jugadas_posibles(dados_def, "generala", nivel)

    categorias ={
        "1": UNOS, 
        "2": DOSES,
        "3": TRESES,
        "4": CUATROS,
        "5": CINCOS,
        "6": SEISES,
        "escalera" : ESCALERA,
        "full": FULL,
        "poker": POKER,
        "generala": GENERALA,   
    }
    enumerar = 1
    for clave, valor in categorias.items():
        print(f"[{enumerar}] {clave}: {valor}")
        enumerar +=1
    check = False
    while check == False:
        while True: 
            categoria = str(input("ELIJA EL NÚMERO DE LA CATEGORÍA A GUARDAR: "))
            if categoria == "7":
                categoria = "escalera"
            elif categoria == "8":
                categoria = "full"
            elif categoria == "9":
                categoria = "poker"
            elif categoria == "10":
                categoria = "generala"
            if Fcsv.categoria_disponible(categoria):
                break
            print("Esa categoría ya fue usada.")

        
        puntos = categorias[categoria]
        Fcsv.sumar_puntos(categoria, puntos)
        check = True