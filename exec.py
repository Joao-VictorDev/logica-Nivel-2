custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

percentual_distribuidor = 28
percentual_impostos = 45

custo_distribuidor = custo_fabrica * (percentual_distribuidor / 100)
custo_impostos = custo_fabrica * (percentual_impostos / 100)

custo_final = custo_fabrica + custo_distribuidor + custo_impostos

print(f"O custo final ao consumidor é: R${custo_final:.2f}")
