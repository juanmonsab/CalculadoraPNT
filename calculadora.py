def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "No se puede dividir por cero"

num1 = 5
num2 = 3
operacion = "/"

# Realizar la operación y mostrar el resultado
if operacion == "+":
    resultado = sumar(num1, num2)
    print("El resultado es:", resultado)
elif operacion == "-":
    resultado = restar(num1, num2)
    print("El resultado es:", resultado)
elif operacion == "*":
    resultado = multiplicar(num1, num2)
    print("El resultado es:", resultado)
elif operacion == "/":
    resultado = dividir(num1, num2)
    print("El resultado es:", resultado)