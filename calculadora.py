def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

num1 = 5
num2 = 3
operacion = "+"

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