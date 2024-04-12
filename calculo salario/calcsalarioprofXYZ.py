"""

Descrição: Este programa calcula salário bruto, líquido e o total dos descontos do professor da Universidade XYZ
Autor: Maurício Silveira
DATA:12/04/2024
Versão 0.0.1
"""


# Alocação de memoria

horas_trabalhadas: int = 0

x = horas_trabalhadas

# Entrada de dados

x = int(input("Quantas horas você trabalha?"))

# Processamento de dados

Salario_Bruto = x*40

Salario_Liquido = Salario_Bruto*0.70

Descontos = Salario_Bruto*0.30

#Saida de dados

print(f'\nO seu salário bruto é de {Salario_Bruto} reais')

print(f'\nO seu salário líquido é de {Salario_Liquido} reais')

print(f'\nO total de descontos é de {Descontos} reais')