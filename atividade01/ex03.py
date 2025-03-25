valorTotal = float(input("Qual o valor total das compras que você fez? "))
if valorTotal > 500:
    valorTaxado = (0.5 * valorTotal) + valorTotal
print(f"O valor com a taxa é {valorTaxado}")
