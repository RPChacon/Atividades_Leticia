segundos = int(input("Digite o valor em segundos: "))

dias = segundos // (24 * 3600)
horas = (segundos % (24 * 3600)) // 3600
minutos = (segundos % 3600) // 60

print(f"Esse tempo tem {dias} dias.")
print(f"Esse tempo tem {horas} horas.")
print(f"Esse tempo tem {minutos} minutos.")
