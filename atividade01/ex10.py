n = int(input("Digite um número inteiro maior que 1: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} não é primo.")
            break
    else:
        print(f"{n} é primo.")
else:
    print("O número deve ser maior que 1.")
