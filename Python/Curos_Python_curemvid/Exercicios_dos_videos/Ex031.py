km = float(input("Digite a quantidade de km da sua viagem: "))

if km < 200:
    print("A viagem custarĂ¡ R${}".format(km*0.5))
else:
    print("A viagem custarĂ¡ R${}".format(km*0.45))
