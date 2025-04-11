def josephus(n,k):
  pessoas = list(range(1, n + 1))  
  indice = 0  
  while len(pessoas) > 1:
    indice = (indice + k - 1) % len(pessoas)  
    pessoas.pop(indice)  
  return pessoas[0]


nc = int(input())

for i in range(1, nc + 1):
  n, k = map(int, input().split())
  resultado = josephus(n, k)
  print(f"Case {i}: {resultado}")