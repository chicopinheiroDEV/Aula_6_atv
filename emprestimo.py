def calcular_emprestimo_juros_simples(principal, taxa_juros, tempo):
    valor_total = principal * (1 + taxa_juros * tempo)
    return valor_total

valor_principal = float(input("Digite o valor principal do empréstimo: "))
taxa_juros = float(input("Digite a taxa de juros anual (em %): ")) / 100
tempo = float(input("Digite o tempo do empréstimo em anos: "))

valor_total = calcular_emprestimo_juros_simples(valor_principal, taxa_juros, tempo)

print(f"O valor total a ser pago após {tempo} anos é: R$ {valor_total:.2f}")
