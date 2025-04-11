nome=input()
salario_fixo=float(input())
total_vendas=float(input())
comissao=0.15*total_vendas
salario_total=salario_fixo+comissao
print(f"TOTAL = R$ {salario_total:.2f}")