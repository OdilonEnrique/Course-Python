# Capture dois números do usuário
# Faça as 4 operações (+, -, *, /) e atribua a variavéis semânticas
# Imprima na tela o valor das variavéis com suas operações

num1 = int(input("Digite um número --> "))
num2 = int(input("Digite um número --> "))

add  = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

# print(f"Os números digitados foram {num1} e {num2}")
# print(f"O resultado da soma é: {add}")
# print(f"O resultado da subtração é: {sub}")
# print(f"O resultado da multiplicação é: {mult}")
# print(f"O resultado da divisão é: {div}")

print(f'''
    {num1} + {num2} = {add}
    {num1} - {num2} = {sub}
    {num1} * {num2} = {mult}
    {num1} / {num2} = {div:.2f}
''')