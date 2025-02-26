#calcular la suma, resta ,multiplicacion y divicion de 2 numeros con un menu con while

def menu():
    print(" ")
    print("/--------------------------------/")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("/--------------------------------/")
    return int(input("Elija una opcion: "))

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: No se puede dividir por cero.")
        return None
    
while True:
    opcion = menu()
    
    if opcion == 5:
        break
    
    if opcion < 1 or opcion > 5:
        print("Error: Opcion invalida.")
        continue
    
    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))
    
    resultado = None
    
    if opcion == 1:
        resultado = sumar(numero1, numero2)
    elif opcion == 2:
        resultado = restar(numero1, numero2)
    elif opcion == 3:
        resultado = multiplicar(numero1, numero2)
    elif opcion == 4:
        resultado = dividir(numero1, numero2)
    
    if resultado is not None:
        print("/--------------------------------/")
        print("El resultado es:", resultado)
        print("/--------------------------------/")
