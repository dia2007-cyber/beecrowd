def teste_de_selecao(a, b, c, d):
  if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    return "Valores aceitos"
  else:
    return "Valores nao aceitos"

entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])
d = int(entrada[3])

resultado = teste_de_selecao(a, b, c, d)
print(resultado)
