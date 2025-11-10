def menu():
    print("\n===== Generala Mágica =====\n")

    while True: 
        print("\n===== Menú ======")
        print("1- JUGAR")
        print("2- ESTADISTICAS")
        print("3- CREDITOS")
        print("4- SALIR")

        opcion = input("---Seleccione una opción: ")
    
        if opcion == "1":
            asosd=3
        elif opcion == "2":
            contro=1

        elif opcion == "3":
            ekuf=2
        elif opcion == "4":
            print("Nos vemos!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.\n")