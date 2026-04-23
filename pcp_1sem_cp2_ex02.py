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


# Classificação com base nos ângulos
print("\nClassificação do Triângulo com base nos ângulos:")
if A >= (B + C):
    print("NAO FORMA TRIANGULO")
elif A**2 == (B**2 + C**2):
    print("TRIANGULO RETANGULO")
elif A**2 > (B**2 + C**2):
    print("TRIANGULO OBTUSANGULO")
else:
    print("TRIANGULO ACUTANGULO")

# Classificação com base nos lados
print("\nClassificação do Triângulo com base nos lados:")
if A == B == C:
    print("TRIANGULO EQUILATERO")
elif A == B or B == C or A == C:
    print("TRIANGULO ISOSCELES")
else:
    print("TRIANGULO ESCALENO")