import random
import Paquetes.Funciones_Comparar as Fc
def jugar():
    ronda = 0
    while ronda != 10:
        ronda += 1
        tiradas = 0
        dados_usables = 5 
        dados_mano=[]
        dados_def=[]
        while tiradas != 3:
            nuevos=[]
            tiradas += 1
            print(f"RONDA N°{ronda}")
            print(f"tirada numero |{tiradas}|")
            print(f"dados en mano |{dados_mano}|")
            lista_dados = tirar_dados(dados_usables)
            dados_usables , nuevos  = guardar_dados(lista_dados, dados_usables)
            dados_def.extend(nuevos)
            print(Fc.categorias(dados_def))
            print(f"dados en mano: {dados_def}")
            print(f"\n=== FIN TIRADA N°{tiradas} ===")
            return dados_def
        print(f"\n=== FIN RONDA N°{ronda} ===")
   
            
    
    pass
def tirar_dados(dados_usables):
    lista_dados=[]
    for i in range (dados_usables):
        lista_dados.append(random.randint(1, 6))
    print("\n=== DADOS ===")
    print(lista_dados)
    print("\n=============")
    return(lista_dados)




def guardar_dados(lista_dados, dados_usables):
    dados_mano=[]
    desea = ""
    while desea != "n" :
        desea= str(input("desea guardar dados?(s/n): ")).lower()
        if desea == "n":
            return dados_usables, dados_mano
        elif desea == "s":
            print(lista_dados)
            check = False
            while check == False:
                posicion=int(input(f"elija un dado a guardar(1-{dados_usables} por su posicion): "))
                if posicion > dados_usables or posicion <= 0:
                    print("ingrese un número de posición dentro del rango indicado")
                else:
                    check = True
            borrado = lista_dados[(posicion-1)]
            dados_mano.append(borrado)
            lista_dados.remove(borrado)
            dados_usables -=1
            print(lista_dados)    
            print(dados_mano)
        else:
            print("ingrese una opción válida")
    return(dados_usables, dados_mano)


