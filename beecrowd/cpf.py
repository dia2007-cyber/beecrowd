def calcular_digito(cpf, peso):
    soma = 0
    for i in range(len(cpf)):
        soma += int(cpf[i]) * peso
        peso -= 1
    digito = (soma * 10) % 11
    if digito >= 10:
        return 0
    return digito

def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')  # Remove pontos e traços

    if len(cpf) != 11 or not cpf.isdigit():  # Verifica se tem 11 dígitos
        return False

    primeiro_digito = calcular_digito(cpf[:-2], 10)
    segundo_digito = calcular_digito(cpf[:-1], 11)

    if cpf[-2] == str(primeiro_digito) and cpf[-1] == str(segundo_digito):
        return True
    return False

# Programa principal
cpf_input = input("Digite o CPF (apenas números): ")  # Entrada do usuário
if validar_cpf(cpf_input):
    print("CPF válido!")
else:
    print("CPF inválido!")