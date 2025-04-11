def calcular_lanche(codigo, quantidade):
  if codigo == 1:
    preco = 4.00
  elif codigo == 2:
    preco = 4.50
  elif codigo == 3:
    preco = 5.00
  elif codigo == 4:
    preco = 2.00
  elif codigo == 5:
    preco = 1.50
  else:
    return "Código inválido."

  total = preco * quantidade
  return f"Total: R$ {total:.2f}"

entrada = input().split()
codigo = int(entrada[0])
quantidade = int(entrada[1])

resultado = calcular_lanche(codigo, quantidade)
print(resultado)
