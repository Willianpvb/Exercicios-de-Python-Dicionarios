person = dict()
people = list()
media = 0
while True:
    person['nome'] = input('Seu nome:').capitalize()
    while True:
        sexo = input('Sexo:[M/F]')
        if sexo not in 'MmFf':
            print('Escolha entre > F < para feminino e > M < para masculino')
        else:
            person['sexo'] = sexo.capitalize()
            break
    person['idade'] = int(input('Qual sua idade?'))
    media += person['idade']

    people.append(person.copy())
    person.clear()

    while True:
        continuar = input('Quer continuar (S/N)?')
        if continuar not in 'SsNn':
            print('Escolha entre > S < para SIM e > N < para NÃO')
        else:
            break
    if continuar in 'Nn':
        break
    else:
        print('X-'*20)

print('\n'*3)
print(people)
print('<=<'*15)
print(f'A) Número de pessoas cadastradas: {len(people)}')

media = media // len(people)
print(f'B) A média de idade é {media}')

print('C) Lista com todas as mulheres')
for m in range(0,len(people)):
    if people[m]['sexo'] == 'F':
        print(people[m])

print('D) Lista com pessoas com a idade acima da media:')
for m in people:
    if m['idade'] > media:
        print(m)



