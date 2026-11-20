# Vários valores no mesmo case com o | (lê-se "ou") -------

# dia = int(input('Dia da semana (1 a 7): '))

# match dia:
#     case 1 | 7:
#         print("Fim de semana")
#     case 2 | 3 | 4 | 5 | 6:
#         print('Dia útil')
#     case _:
#         print('Dia inválido')


# Match com texto ---------

operacao = input("Operação (+, -, *, /)")
a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))

match operacao:
    case "+":
        print(f"Resultado: {a+b}")
    case "-":
        print(f"Resultado: {a-b}")
    case "*":
        print(f"Resultado: {a*b}")
    case "/":
        if b != 0:
            print(f"Resultado: {a/b}")
        else:
            print("Não é possível dividir por zero!")
    case _:
        print("Operação inválida.")