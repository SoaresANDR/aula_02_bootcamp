# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.


numero01 = int(input("Informe o primeiro número"))
numero02 = int(input("Informe o segundo número"))

soma_final = numero01 + numero02
print(f"O resultado do {numero01} e {numero02}é: ",soma_final)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

numero = int(input("Informe o número"))

resto_divisao = numero % 5
print("O resto da visião por 5 é: ",resto_divisao)


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

numero01 = int(input("Informe o primeiro número"))
numero02 = int(input("Informe o segundo número"))

multiplicação_final = numero01 * numero02
print(f"O resultado da multiplicação entre {numero01} e {numero02}é: ",soma_final)


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

'''numero_01 = int(input("Inserir um número inteiro: "))
numero_02 = int(input("Inserir um número inteiro: "))
resultado = numero_01 // numero_02

print(resultado)
'''



# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

numero_quadrado = float(input("Digite o número para ser calculado"))
quadrado = numero_quadrado ** 2




# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

num01 = float(input("Informe o primeiro número"))
num02 = float(input("Informe o segundo  número"))

adicao = num01 + num02
print("A soma dos números é: ",adicao)


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num01 = float(input("Informe o primeiro número"))
num02 = float(input("Informe o segundo  número"))

media = (num01 + num02) /2
print("A media dos números é: ",media)



# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Informe a base do número"))
expoente = float(input("Informe o expoente "))

potencia = base ** expoente

print("O resultado da Potencia é: ",potencia)
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em celcius"))

fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} é igual {fahrenheit}")




# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio = float(input("Informe o raio do círculo: "))
area = 3.14159 * raio **2

import math


'''raio_do_circulo = float(input("Digite o raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
print(area_do_circulo)
'''

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
nome_usuario = input("Olá Usuário, informe o seu nome: ")
nome_usuario_maisculo = nome_usuario.upper()
print("Texto em maísculo: ",nome_usuario_maisculo)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

usuario = input("Digite o seu nome")
usuario_letra_minusculo = usuario.lower()
print(f"{usuario} esta com as letras {usuario_letra_minusculo}")


# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
usuario = input("       Olá Usuário, digite uma frase:      ")
remove_espacos = usuario.strip()
print("O espaço do texto já foi removido do início ao fim: ",remove_espacos)


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

input("Insira uma data no formato dd/mm/aaaa: ")

'''data_do_usuario = "20/02/2024"
lista_de_dia_mes_ano = data_do_usuario.split("/")
print(f"O elemento 1 é o {lista_de_dia_mes_ano[0]}")
print(f"O elemento 2 é o {lista_de_dia_mes_ano[1]}")
print(f"O elemento 3 é o {lista_de_dia_mes_ano[2]}")
'''

'''numero = int(input("Insira um número"))

if isinstance(numero,int):
  print('A variávelé um inteiro')
else:
  print("A variaável não é um inteiro")
  '''

idade = 18

if idade < 18:
  print("Não pode dirigir")
elif idade == 18:
  print("Você pode dirigir e tirar a carteira")
else:
  print("Pode dirigir")

# #### Booleanos (`bool`)
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = True
valor2 = False 
resultado = valor1 and valor2
print("O resultado do AND Lógico é: ",resultado)



# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
valor1 = bool(input("Informe o primeiro valor: "))
valor2 = bool(input("Informe o segundo  valor: "))
resultado_or = valor1 or valor2
print("Resultado do operador lógico or é: ", resultado_or)






# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação


