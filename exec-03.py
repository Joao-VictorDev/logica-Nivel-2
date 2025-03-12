# Versão 1
A1 = 10
B1 = 20
C1 = A1 + B1
A1 = B1
B1 = C1 - A1

# Versão 2
A2 = 10
B2 = 20
C2 = A2 + B2
B2 = C2 - A2
A2 = B2

print("Versão 1: A =", A1, "B =", B1, "C =", C1)
print("Versão 2: A =", A2, "B =", B2, "C =", C2)

# Comentário explicativo
# Caso os valores de A, B ou C sejam diferentes:
# A diferença ocorre devido à ordem de atribuições