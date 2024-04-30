# Crie uma função que receba altura e peso e retorne o IMC
def calc_IMC(height, weight):
    IMC = weight / height**2
    return IMC

height = float(input("Digite sua altura(m): "))
weight = float(input("Digite seu peso(kg): "))

result = calc_IMC(height, weight)
print(f"Seu IMC é {result:.2f}Kg/m²")