
import math

potencia_lampada = float(input('Potência da lâmpada (W): '))
largura = float(input("Largura do cômodo (m): "))
comprimento = float(input("Comprimento do cômodo (m): "))

area = largura * comprimento
pt_necessaria = area * 3  # 3W por m quadrado
lampadas = math.ceil(pt_necessaria/potencia_lampada)
bocais = math.ceil(area/3) # 1 bocal a cada 3m2

print(f"Área do cômodo: {area:.2f} m²")
print(f"Potência necessária: {pt_necessaria:.0f} W")
print(f"Lâmpadas de {potencia_lampada:.0f} W necessárias: {lampadas}")
print(f"Bocais disponíveis no cômodo: {bocais}")

if lampadas > bocais:
    print('Faltam bocais; utilize lâmpadas mais potentes')
else:
    print('Tudo certo!')