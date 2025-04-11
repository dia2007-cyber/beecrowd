inicio_hora, inicio_minuto, fim_hora, fim_minuto = map(int, input().split())

inicio_total_minutos = inicio_hora * 60 + inicio_minuto
fim_total_minutos = fim_hora * 60 + fim_minuto

if inicio_total_minutos < fim_total_minutos:
    duracao_total_minutos = fim_total_minutos - inicio_total_minutos
else:
    duracao_total_minutos = (24 * 60 - inicio_total_minutos) + fim_total_minutos

duracao_horas = duracao_total_minutos // 60
duracao_minutos = duracao_total_minutos % 60

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")