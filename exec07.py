totalDeEleitores = int(input("total de eleitores de um município"))

votosEmBranco = int(input("Qual a quantidade de votos em branco?:"))

votosEmNulo = int(input("Qual a quantidade de votos nulo?:"))

votosEmValido = int(input("Qual a quantidade de votos validos?:"))

if totalDeEleitores + votosEmBranco + votosEmValido > votosEmNulo:
    print("Erro: A soma dos votos excede o número total de eleitores.")
else:
    percentual_brancos = (votosEmBranco / totalDeEleitores) * 100
    percentual_nulos = (votosEmNulo / totalDeEleitores) * 100
    percentual_validos = (votosEmValido / totalDeEleitores) * 100

    print(f"\nPercentual de votos brancos: {percentual_brancos:.2f}%")
    print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
    print(f"Percentual de votos válidos: {percentual_validos:.2f}%")
