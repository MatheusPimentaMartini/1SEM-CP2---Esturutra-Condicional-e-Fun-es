lado_1 = float(input("Medida do lado do triângulo: "))
lado_2 = float(input("Medida do lado do triângulo: "))
lado_3 = float(input("Medida do lado do triângulo: "))


if lado_1 > lado_2 > lado_3:
    A = lado_1
    B = lado_2
    C = lado_3
elif lado_1 > lado_3 > lado_2:
    A = lado_1
    B = lado_3
    C = lado_2
elif lado_2 > lado_1 > lado_3:
    A = lado_2
    B = lado_1
    C = lado_3
elif lado_2 > lado_3 > lado_1:
    A = lado_2
    B = lado_3
    C = lado_1
elif lado_3 > lado_1 > lado_2:
    A = lado_3
    B = lado_1
    C = lado_2
elif lado_3 > lado_2 > lado_1:
    A = lado_3
    B = lado_2
    C = lado_1
elif lado_1 == lado_2 == lado_3 or (lado_3 == lado_2) < lado_1:
    A = lado_1
    B = lado_2
    C = lado_3
elif (lado_1 == lado_2) < lado_3 or (lado_1 == lado_3) > lado_2:
    A = lado_3
    B = lado_1
    C = lado_2
elif (lado_1 == lado_3) < lado_2 or (lado_1 == lado_2) > lado_3:
    A = lado_2
    B = lado_3
    C = lado_1
elif (lado_3 == lado_2) > lado_1:
    A = lado_3
    B = lado_2
    C = lado_1


print("Classificção do Triângulo com base nos ângulos")
if A >= (B + C):
    print("Os lados não formam um Triângulo\n")
elif A**2 == (B**2 + C**2):
    print("Os ângulos formam um Triângulo Retângulo\n")
elif A**2 > (B**2 + C**2):
    print("Os ângulos formam um Triângulo Obtusângulo\n")
elif A**2 < (B**2 + C**2):
    print("Os ângulos formam um Triângulo Acutângulo\n")
else:
    print("ERRO!")

print("Classificação do Triângulo com base nos lados")
if A == B == C:
    print("Os lados do Triângulo formam um Triângulo Equilatero")
elif A == B != C or A == C != B or B == C != A:
    print("Os lados do Triângulo formam um Triângulo Isosceles")
else:
    print("Não possui classificação com base nos lados")