#Pedir um número e associá-lo a um dia da semana.

# dia: str = ('Domingo', 'Segunda', "Terça", 'Quarta', 'Quinta', 'Sexta', 'Sábado')
numero = int(input("Número: "))

# if numero == 1:
#     print('Domingo')
# elif numero == 2:
#     print('Segunda')
# elif numero == 3:
#     print('Terça')
# elif numero == 4:
#     print('Quarta')
# elif numero == 5:
#     print('Quinta')
# elif numero == 6:
#     print('Sexta')
# elif numero == 7:
#     print('Sábado')
# else:
#     print('Inserir número de 1 a 7')

    #====================================================================

match numero:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sábado')
    case _:
        print('Inserir número de 1 a 7')