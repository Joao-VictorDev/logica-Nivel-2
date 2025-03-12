# Solicitar ao usuário a idade em anos, meses e dias
print("Informe sua idade:")
anos = int(input("Anos: "))
meses = int(input("Meses: "))
dias = int(input("Dias: "))

# Calcular a idade expressa apenas em dias
idade_em_dias = (anos * 365) + (meses * 30) + dias

# Exibir o resultado
print("Sua idade expressa em dias é:", idade_em_dias)
