from os import system
system("cls")

while True:
    system("cls")
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))

    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        resultado = n1 + n2
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == "2":
        resultado = n1 - n2
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == "3":
        resultado = n1 * n2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == "4":
        if n2 != 0:
            resultado = n1 / n2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")