n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

media1 = (n1 + n2 + n3)/3
media2 = ((n1 * 2) + (n2 * 2) + (n3 * 3))/7
media3 = ((n1 * 1) + (n2 * 1) + (n3 * 2))/4

print(f"A média aritmética desses números é: {media1}")
print(f"A média ponderada, considerando os pesos 2, 2 e 3, desses números é: {media2}")
print(f"A média ponderada, considerando os pesos 1, 1 e 2, desses números é: {media3}")
