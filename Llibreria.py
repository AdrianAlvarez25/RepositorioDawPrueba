llibreria = []

while True:
    print("\n1. Afegir un nou llibre")
    print("2. Mostrar la llista de llibres")
    print("3. Eliminar un llibre")
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
        print("Llista de llibres:")
        for index, llibre in enumerate(llibreria, 1):
            print(f"{index}. {llibre}")
        index_a_eliminar = int(input("Introdueix l'índex del llibre a eliminar: "))
        if 0 < index_a_eliminar <= len(llibreria):
            llibreria.pop(index_a_eliminar - 1)
            print("Llibre eliminat amb èxit!")
        else:
            print("Índex fora de límits. No s'ha eliminat cap llibre.")
    elif opcio == "4":
        print("Gràcies per utilitzar el nostre programa. Adeu!")
        break
    else:
        print("Opció no vàlida. Si us plau, selecciona una opció correcta.")