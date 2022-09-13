jogador = dict()
gols = 0

jogador['nome'] = str(input('Nome:')).capitalize()

jogador['jogos_jogados'] = int(input(f'Partidas Jogadas Por {jogador["nome"]}:'))

for i in range(1,jogador['jogos_jogados']+1):
    jogador[f'partida_{i}'] = int(input(f'Quantos Gols feitos na partida {i}?'))

print('-'*20)

print('-'*20)
print(f'O jogador {jogador["nome"]} jogou {jogador["jogos_jogados"]} partidas')
for k, v in jogador.items():
    if 'partida' in k:
        print(f'    +> Na {k}, foram feitos {v} gols.')
        gols += v

print(f'Foram realizados {gols} gols no total')