cont = soma = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    soma += n
    cont += 1
print(f"A soma dos números digitados foi {soma}")
print(f"A quantidade de números digitados foi {cont}")
