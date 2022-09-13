from datetime import datetime
from time import sleep
cara = dict()
cara['nome'] = input('Nome:')
cara['ano_nasceu'] = int(input('Ano de nascimento:'))
cara['carteira_trabalho'] = int(input("Cartera de Trabalho( 0 não tem):"))
if cara['carteira_trabalho'] != 0 and  len(str(cara['carteira_trabalho'])) >= 5:
    cara['ano_contratação'] = int(input('Ano de contratação:'))
    cara['salario'] = int(input('Salario:'))
cara['idade'] = datetime.now().year - cara['ano_nasceu']
cara['oposentadoria'] = cara['idade'] + 40
print("$"*30)
for k, v in cara.items():
    print(f'{k} -> {v}')
    sleep(1)