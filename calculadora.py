

def sumar_numeros(numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

def restar_numeros(a, b):
    return a - b

def multiplicar_numeros(numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

def dividir_numeros(a, b):
    return a / b

def calcular_factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

def calcular_potencia(base, exponente):
    resultado = 1
    for i in range(exponente):
        resultado *= base
    return resultado

def escribir_resultado(resultado):
    with open("resultados.txt", "a") as archivo:
        archivo.write(str(resultado) + "\n")

while True:
    print("Calculadora Python")
    print("Seleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Factorial")
    print("6. Potencia")
    print("7. Salir")
    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == "1":
        numeros = []
        while True:
            num = input("Ingrese el primer y segundo número ( después digite 'fin' para ver el resultado): ")
            if num == "fin":
                break
            numeros.append(float(num))
        resultado = sumar_numeros(numeros)
        print("El resultado es: ", resultado)
        escribir_resultado(resultado)

    elif opcion == "2":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = restar_numeros(a, b)
        print("El resultado es: ", resultado)
        escribir_resultado(resultado)

    elif opcion == "3":
        numeros = []
        while True:
            num = input("Ingrese el primer y segundo número, después ingrese 'fin' para ver el resultado): ")
            if num == "fin":
                break
            numeros.append(float(num))
        resultado = multiplicar_numeros(numeros)
        print("El resultado es: ", resultado)
        escribir_resultado(resultado)

    elif opcion == "4":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = dividir_numeros(a, b)
        print("El resultado es: ", resultado)
        escribir_resultado(resultado)

    elif opcion == "5":
        n = int(input("Ingrese el número para calcular su factorial: "))
        resultado = calcular_factorial(n)
        print("El resultado es: ", resultado)
        escribir_resultado(resultado)

    elif opcion == "6":
        base = float(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente: "))
        resultado = calcular_potencia(base, exponente)
        print("El resultado es: ", resultado)
        escribir_resultado(resultado)

    elif opcion == "7":
        print("Saliendo de la calculadora...")
        break

    else:
        print("Opción inválida, por favor ingrese un número del 1 al 7.")

print("Gracias por usar la calculadora.")


# 'sumar_numeros(numeros): Recibe una lista de números y devuelve la suma de todos ellos.
# 'restar_numeros(a, b): Recibe dos números y devuelve la resta de ambos.
# 'multiplicar_numeros(numeros): Recibe una lista de números y devuelve la multiplicación de todos ellos.
# 'dividir_numeros(a, b): Recibe dos números y devuelve el resultado de la división del primero por el segundo.
# 'calcular_factorial(n): Recibe un número y devuelve su factorial.
# 'calcular_potencia(base, exponente): Recibe dos números y devuelve el resultado de elevar el primero al segundo.
# La función 'escribir_resultado(resultado)' escribe el resultado de una operación en un archivo de texto llamado "resultados.txt" en el directorio principal de la aplicación.
# Tiene un bucle 'while True' que se ejecuta hasta que el usuario decide salir de la calculadora. 
# En cada iteración del bucle, se muestra un menú de opciones que permite al usuario seleccionar la operación que desea realizar. 
# La selección del usuario se guarda en la variable opcion.
# Luego, dependiendo de la opción seleccionada, se solicitan los números necesarios para realizar la operación y se llama a la función correspondiente para realizarla. 
# El resultado se muestra por pantalla y se escribe en el archivo "resultados.txt" llamando a la función 'escribir_resultado(resultado)'.
# Si el usuario selecciona la opción 7, se muestra un mensaje de salida y se rompe el bucle, terminando la ejecución de la calculadora.
