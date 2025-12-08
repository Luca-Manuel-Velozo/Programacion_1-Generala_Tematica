import random
import Paquetes.Funciones_Comparar as Fc
import Paquetes.Funciones_CSV as Fcsv
import Paquetes.Funciones_json as Fjson


def jugar(nivel_seleccionado):
    Fcsv.cargar_csv()
    nombre_archivo = Fcsv.cargar_nombre()
    ronda = 0
    
    while ronda != 10:
        ronda += 1
        tiradas = 0
        dados_usables = 5 
        dados_mano=[]
        dados_def=[]
        while tiradas != 3:
            tiradas += 1
            print(f"RONDA N°{ronda}")
            print(f"tirada numero |{tiradas}|")
            print(f"PUNTOS |{Fcsv.total_puntos_csv()}|")
            print(f"dados en mano |{dados_mano}|")
            lista_dados = tirar_dados(dados_usables)
            dados_usables , dados_mano, lista_dados = guardar_dados(lista_dados, dados_usables, dados_mano)
            print(dados_def)
            dados_def = lista_dados + dados_mano
            tiradas = opciones_ronda(tiradas, dados_def, nivel_seleccionado)
            print(f"\n=== FIN TIRADA N°{tiradas} ===")

        print(f"\n=== FIN RONDA N°{ronda} ===")
    Fjson.guardar_json_partida()
    Fjson.guardar_datos()
   
            
def tirar_dados(dados_usables):
    lista_dados=[]
    for i in range (dados_usables):
        lista_dados.append(random.randint(1, 6))
    print("\n=== DADOS ===")
    print(lista_dados)
    print("\n=============")
    return(lista_dados)




def guardar_dados(lista_dados, dados_usables, dados_mano):
    desea = ""
    while desea != "n":
        
        if dados_usables == 0:
            print("ya usaste todos tus dados")
            desea = "n"
            return dados_usables, dados_mano, lista_dados 
        
        desea = str(input("desea guardar dados?(s/n): ")).lower()

        if desea == "n":
            return dados_usables, dados_mano, lista_dados
        
        elif desea == "s":
            indices_borrar = []
            entrada_valida = False
            
            while not entrada_valida:
                entrada = input(f"elija los dados a guardar por su posicion separados por coma (1-{dados_usables}): ")
                partes = entrada.split(',')
                indices_temporales = []
                error_encontrado = False

                for parte in partes:
                    parte = parte.strip()
                    if parte.isdigit():
                        pos = int(parte)

                        if 1 <= pos <= len(lista_dados):
                            pos_final = pos - 1
                            if pos_final not in indices_temporales:
                                indices_temporales.append(pos_final)
                            else:
                                print(f"Error: La posición {pos} ya fue elegida.")
                                error_encontrado = True
                                break
                        else:

                            print(f"Error: La posición {pos} no existe.")
                            error_encontrado = True
                            break
                    else:
                        
                        print(f"Error: '{parte}' no es un número válido.")
                        error_encontrado = True
                        break
                
                
                if not error_encontrado and len(indices_temporales) > 0:
                    indices_a_borrar = indices_temporales
                    entrada_valida = True

            n = len(indices_a_borrar)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if indices_a_borrar[j] < indices_a_borrar[j + 1]:
                        aux = indices_a_borrar[j]
                        indices_a_borrar[j] = indices_a_borrar[j + 1]
                        indices_a_borrar[j + 1] = aux

            for pos_final in indices_a_borrar:
                dado_movido = lista_dados.pop(pos_final)
                dados_mano.append(dado_movido)
                dados_usables -= 1

            print(f"Dados restantes: {lista_dados}")    
            print(f"Tu mano: {dados_mano}")
            
            desea = "n"
            
        else: 
            print("ingrese s para si y n para no")

    return dados_usables, dados_mano, lista_dados

def opciones_ronda(tiradas, dados_def, nivel_seleccionado):
    if tiradas == 0:
        print('''
        =======================================
          eliga una opción:
          1-TIRAR
        =======================================''')
    elif tiradas < 3 and tiradas >=1:
        print('''
            =======================================
             eliga una opción:
              1-anotar puntos
              2-siguiente tirada
            =======================================''')
    else:
        print('''
        =======================================
          eliga una opción:
          1-anotar puntos
        =======================================''')
    opciones = int(0)
    exit = False
    while exit == False:
        opciones = int(input("==="))
        if opciones == 1:
            Fc.comparacion_mano(dados_def, nivel_seleccionado)
            tiradas = 3
            exit = True
            return tiradas
        elif opciones == 2:
            exit = True
            return tiradas
        else:
            print("ingrese un valor válido")


