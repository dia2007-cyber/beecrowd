codigo1, numero1, valor1 = input().split()
codigo2, numero2, valor2 = input().split()

total = (int(numero1) * float(valor1)) + (int(numero2) * float(valor2))

print("VALOR A PAGAR: R$ {:.2f}".format(total))