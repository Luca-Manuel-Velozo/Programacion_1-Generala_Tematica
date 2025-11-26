import Paquetes.Funciones_Juego as Fg
import Paquetes.Funciones_Juego as Fj
categorias = {
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
}
def jugadas_posibles(dados_mano):
    posibles=[]
    for i in range(1,7):
        if i == dados_mano(i):
            posibles.append(i)
    print(posibles)
    pass