import Paquetes.Funciones_Generales as Fg
import Paquetes.Funciones_Juego as Fj

def jugadas_1_6(NUM, dados_def):
    puntos = 0
    for i in dados_def:
        if NUM == i:
            puntos += NUM
    return puntos

def jugadas_posibles(dados_def):
    dados_def.sort()
    escalera1 = [1,2,3,4,5]
    escalera2 = [2,3,4,5,6]
    if dados_def == escalera1 or dados_def == escalera2:
        return 35
    elif dados_def[0]==dados_def[1] and dados_def[1]==dados_def[2] and dados_def[3] == dados_def[4]:
        return 40
    elif dados_def[0]==dados_def[1] and dados_def[2]==dados_def[3] and dados_def[3] == dados_def[4]:
        return 40
    elif dados_def[0]==dados_def[1] and dados_def[1]==dados_def[2] and dados_def[2] == dados_def[3]:
        return 45
    elif dados_def[1]==dados_def[2] and dados_def[2]==dados_def[3] and dados_def[3] == dados_def[4]:
        return 45
    
def comparacion_mano(dados_def):
    UNOS = jugadas_1_6(1, dados_def)
    DOSES = jugadas_1_6(2, dados_def)
    TRESES = jugadas_1_6(3, dados_def)
    CUATROS = jugadas_1_6(4,dados_def)
    CINCOS = jugadas_1_6(5, dados_def)
    SEISES = jugadas_1_6(6, dados_def)
    ESCALERA = jugadas_posibles(dados_def)
    FULL = jugadas_posibles(dados_def)
    POKER = jugadas_posibles(dados_def)
    GENERALA = jugadas_posibles()

#    categorias ={
#       "1": UNOS 
#        "2": 
#        "3": 
#        "4": 
#        "5": 
#        "6": 
#        "escalera" : jugadas_posibles(),
#        "full": jugadas_posibles(),
#        "poker": jugadas_posibles(),
#        "generala": jugadas_posibles(),
#    }
