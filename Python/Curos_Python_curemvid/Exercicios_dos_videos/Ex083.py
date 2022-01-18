ex = str(input("Digite sua expressão: "))
pilha = []

for simbolo in ex:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Sua expressão está válida")
else:
    print("Sua expresão está errado")
