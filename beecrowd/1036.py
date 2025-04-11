import math

valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

if a == 0:
    print("Impossivel calcular")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Impossivel calcular")
    else:
        raiz_delta = math.sqrt(delta)
        r1 = (-b + raiz_delta) / (2*a)
        r2 = (-b - raiz_delta) / (2*a)
        print(f"R1 = {r1:.5f}")
        print(f"R2 = {r2:.5f}")