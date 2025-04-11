# -*- coding: utf-8 -*-
x = int(input())
y = int(input())

soma_impares = 0

if x > y:
    inicio = y + 1
    fim = x
else:
    inicio = x + 1
    fim = y

for i in range(inicio, fim):
    if i % 2 != 0:
        soma_impares += i

print(soma_impares)
