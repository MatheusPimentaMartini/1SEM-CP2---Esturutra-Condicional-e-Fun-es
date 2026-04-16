CP1 = float(input("Colocar a nota do checkpoint 1 de 0 a 10: "))
CP2 = float(input("Colocar a nota do checkpoint 2 de 0 a 10: "))
CP3 = float(input("Colocar a nota do checkpoint 3 de 0 a 10: "))
SP1 = float(input("Colocar a nota da sprint 1 de 0 a 10: "))
SP2 = float(input("Colocar a nota da sprint 2 de 0 a 10: "))
GS = float(input("Colocar a nota da global solution de 0 a 10: "))

menor = 0


if CP1 < CP2 and CP1 < CP3:
    menor = CP1
elif CP2 < CP3 and CP2 < CP3:
    menor = CP2
else:
    menor = CP3

media = ((CP1 + CP2 + CP3 - menor + SP1 + SP2) / 4 ) * 0.4 + GS * 0.6
media_peso = media * 0.4

print(f"A média no semestre é: {media:.1f}")
print(f"A média no semestre com peso é: {media_peso:.1f}")