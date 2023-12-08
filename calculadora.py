def calculadora(number1, number2, operador):
    resultado = 0
    match operador:
        case "+":
            resultado = number1 + number2
        case "-":
            resultado = number1 - number2
        case "*":
            resultado = number1 * number2
        case "/":
            resultado = number1 / number2
        case _:
            "operador não identificado"
    return resultado
number1 = int(input('Digite o primeiro numero: '))
number2 = int(input('Digite o segundo numero: '))
operador = input('Digite o operador: ')

result = calculadora(number1, number2, operador)
print(result)