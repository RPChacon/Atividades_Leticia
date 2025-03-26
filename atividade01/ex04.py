km = int(input("Digite a distância em quilometros: "))
if km > 100:
    taxa = ((km - 100) * 12) + 90
print(f"O valor a ser pago é R$ {taxa}")
