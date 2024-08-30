# Função para calcular o valor com desconto
def calcular_valor_com_desconto(valor_original, percentual_desconto):
    desconto = (percentual_desconto / 100) * valor_original
    valor_com_desconto = valor_original - desconto
    return valor_com_desconto

# Função principal
def main():
    # Solicita ao usuário o valor original
    valor_original = float(input("Digite o valor original: R$ "))
    
    # Solicita ao usuário o percentual de desconto
    percentual_desconto = float(input("Digite o percentual de desconto: "))
    
    # Calcula o valor com desconto
    valor_final = calcular_valor_com_desconto(valor_original, percentual_desconto)
    
    # Exibe o resultado
    print(f"Valor original: R$ {valor_original:.2f}")
    print(f"Percentual de desconto: {percentual_desconto:.2f}%")
    print(f"Valor com desconto: R$ {valor_final:.2f}")

# Executa a função principal
if __name__ == "__main__":
    main()
