import Paquetes.Funciones_Juego as Fj
import Paquetes.funciones_niveles as Fn
import Paquetes.Funciones_CSV as Fcsv

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
            nivel = Fn.seleccionar_nivel()
            Fj.jugar(nivel)

        elif opcion == "2":
            Fcsv.leer_ranking()
        elif opcion == "3":
            creditos()
        elif opcion == "4":
            print("Nos vemos!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.\n")
    
def creditos():
    print('''
        ====================================
            GENERALA TEMATICA
        ====================================
        Autores: -Velozo, Luca Manuel
                 -Vazquez, Santiago
        Fecha: Noviembre 2025
        Materia: Programación I
        Docentes: -Martin Alejando García
                  -Verónica Natalia Carnonari
        Carrera: Técnicatura Universitaria en Programación
        Contacto: -lucavelozo@live.com
                  -vazquezsantiago47606@gmail.com
        ====================================
        ''')
    
    