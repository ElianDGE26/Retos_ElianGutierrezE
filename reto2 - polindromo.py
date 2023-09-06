while (True):
    print("\nVERIFICACION")
    opc = int(input("\n1 - Verificar si la palabra es un polindromo"
                + "\n2 - Salir" + "\nSeleccione una opcion: "))
    if (opc == 1):
        
        palabra = input("Digite la palabra: ")
        palabra = palabra.lower().replace(" ","")
        
        palabra2 = palabra[::-1]
        ##pal = [palabra]
        if (palabra == palabra2):
            print("La palabra es un polindromo")
        else:
            print("\nLa palabra no es un polindromo")
    else: 
        break

