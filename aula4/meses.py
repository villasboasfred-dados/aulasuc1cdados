# Associar um número de 1 a 12 a um mês.
mes = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
numero = int(input("Número: "))

if 1 <= numero <= 12:
    print(mes[numero - 1])
else:
    print("Inválido")

# match numero:
#     case 1:
#         print('Janeiro')
#     case 2:
#         print('Fevereiro')
#     case 3:
#         print('Março')
#     case 4:
#         print('Abril')
#     case 5:
#         print('Maio')
#     case 6:
#         print('Junho')
#     case 7:
#         print('Julho')
#     case 8:
#         print('Agosto')
#     case 9:
#         print('Setembro')
#     case 10:
#         print('Outubro')
#     case 11:
#         print('Novembro')
#     case 12:
#         print('Dezembro')
#     case _:
#         print ('Inválido')