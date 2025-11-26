import random
def jugar():
    ronda = 0
    while ronda != 10:
        ronda += 1
        tiradas = 0
        dados_usables = 5 
        while tiradas != 3:
            dados_mano=[]
            lista_dados = tirar_dados(dados_usables)
            dados_usables , dados_mano = guardar_dados(lista_dados, dados_usables)
    pass
def tirar_dados(dados_usables):
    lista_dados=[]
    for i in range (dados_usables):
        lista_dados.append(random.randint(1, 6))
    print(lista_dados)
    return(lista_dados)




def guardar_dados(lista_dados, dados_usables):
    dados_mano=[]
    desea = ""
    while desea != "n" :
        desea= str(input("desea guardar dados?(s/n): ")).lower()
        if desea == "n":
            print(lista_dados)
            break
        print(lista_dados)
        posicion=int(input(f"elija un dado a guardar(1-{dados_usables} por su posicion): "))
        borrado = lista_dados[(posicion-1)]
        dados_mano.append(borrado)
        lista_dados.remove(borrado)
        dados_usables -=1
        print(lista_dados)    
        print(dados_mano)
    return(dados_usables, dados_mano)
