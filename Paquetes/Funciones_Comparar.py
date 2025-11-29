import Paquetes.Funciones_Generales as Fg
import Paquetes.Funciones_Juego as Fj

def jugadas_1_6(NUM, dados_def):
    puntos = 0
    for i in dados_def:
        if NUM == i:
            puntos += NUM
    return puntos

def jugadas_posibles(dados_mano):
    posibles=[]
    for i in range(1,7):
        if i == dados_mano(i):
            posibles.append(i)
    print(posibles)
    pass
dados_def = Fj.jugar()
categorias ={
    "1": jugadas_1_6(1, dados_def),
    "2": jugadas_1_6(2, dados_def),
    "3": jugadas_1_6(3, dados_def),
    "4": jugadas_1_6(4, dados_def),
    "5": jugadas_1_6(5, dados_def),
    "6": jugadas_1_6(6, dados_def),
    "escalera" : None,
    "full": None,
    "poker": None,
    "generala": None,
}