n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

if ( n1 > n2 and n1 > n3):
  print(f"O maior número digitado foi {n1}")
elif n2 > n1 and n2 > n3:
  print(f"O maior número digitado foi {n2}")
else:
  print(f"O maior número digitado foi {n3}")
if (n1 < n2 and n1 < n3):
  print(f"O menor número digitado foi {n1}")
elif n2 < n1 and n2 < n3:
  print(f"O menor número digitado foi {n2}")
else:
  print(f"O menor número digitado foi {n3}")
