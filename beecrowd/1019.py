N = int(input())

horas = N // 3600
resto_horas = N % 3600

minutos = resto_horas // 60
segundos = resto_horas % 60

print(f"{horas}:{minutos}:{segundos}")