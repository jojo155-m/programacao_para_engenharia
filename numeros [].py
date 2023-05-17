numeros = []
numero = float(input("Digite um número: "))
while numero != -1:
    if numero >0:
        numeros.append(numero)
    numero = float(input("Digite um número: "))
if  len(numeros) > 0:
    soma = sum(numeros)
    media = soma / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    print(f"A soma é {soma}")
    print(f"media é {media}")
    print(f"minimo é {minimo}")
    print(f"maximo é {maximo}")
else:
    print("Número invalido")