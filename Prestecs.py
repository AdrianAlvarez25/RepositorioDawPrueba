llibreria = []
prestecs = []

while True:
    print("\n1. Afegir un nou llibre")
    print("2. Mostrar la llista de llibres")
    print("3. Gestionar préstecs")
    print("4. Sortir")

    opcio = input("Selecciona una opció: ")

    if opcio == "1":
        nou_llibre = input("Introdueix el nom del nou llibre: ")
        llibreria.append(nou_llibre)
        print("Llibre afegit amb èxit!")
    elif opcio == "2":
        print("Llista de llibres:")
        for index, llibre in enumerate(llibreria, 1):
            print(f"{index}. {llibre}")
    elif opcio == "3":
        print("\n1. Registrar un préstec")
        print("2. Mostrar llibres prestats")
        print("3. Gestionar devolució de llibres")
        opcio_prestecs = input("Selecciona una opció: ")
        
        if opcio_prestecs == "1":
            llibre_prestat = input("Introdueix el nom del llibre prestat: ")
            if llibre_prestat in llibreria:
                prestecs.append(llibre_prestat)
                print("Préstec registrat amb èxit!")
            else:
                print("Aquest llibre no està disponible a la llibreria.")
        elif opcio_prestecs == "2":
            if prestecs:
                print("Llibres prestats actualment:")
                for index, llibre in enumerate(prestecs, 1):
                    print(f"{index}. {llibre}")
            else:
                print("No hi ha llibres prestats en aquest moment.")
        elif opcio_prestecs == "3":
            if prestecs:
                print("Llibres prestats actualment:")
                for index, llibre in enumerate(prestecs, 1):
                    print(f"{index}. {llibre}")
                index_devolucio = int(input("Introdueix l'índex del llibre a retornar: "))
                if 0 < index_devolucio <= len(prestecs):
                    llibre_a_retornar = prestecs.pop(index_devolucio - 1)
                    print(f"Has retornat el llibre '{llibre_a_retornar}' amb èxit.")
                else:
                    print("Índex fora de límits. No s'ha processat cap devolució.")
            else:
                print("No hi ha llibres prestats en aquest moment.")
        else:
            print("Opció no vàlida. Si us plau, selecciona una opció correcta.")
    elif opcio == "4":
        print("Gràcies per utilitzar el nostre programa. Adeu!")
        break
    else:
        print("Opció no vàlida. Si us plau, selecciona una opció correcta.")