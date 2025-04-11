valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    quantidade_notas = int(valor // nota)
    print(f"{quantidade_notas} nota(s) de R$ {nota:.2f}")
    valor -= quantidade_notas * nota

print("MOEDAS:")
for moeda in moedas:
    quantidade_moedas = int(round(valor / moeda, 2))
    print(f"{quantidade_moedas} moeda(s) de R$ {moeda:.2f}")
    valor = round(valor - quantidade_moedas * moeda, 2)
