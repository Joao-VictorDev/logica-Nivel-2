num_carros_vendidos = int(input("Digite o número de carros vendidos: "))
valor_total_vendas = float(input("Digite o valor total das vendas: "))
salario_fixo = float(input("Digite o salário fixo: "))
comissao_por_carro = 700  # Comissão fixa por carro
percentual_sobre_vendas = 0.05  # 5% do valor das vendas


salario_final = salario_fixo + (num_carros_vendidos * comissao_por_carro) + (valor_total_vendas * percentual_sobre_vendas)

print(f"O salário final do vendedor é: R$ {salario_final:.2f}")
