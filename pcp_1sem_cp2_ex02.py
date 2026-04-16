valor1 = int(input("Digite um numero:\n"))
valor2 = int(input("Digite um numero:\n"))
valor3 = int(input("Digite um numero:\n"))

valores = [valor1,valor2,valor3]

valores.sort(reverse=True)

a = valores[0]
b = valores[1]
c = valores[2]

print(f"O valor de A é: {a}")
print(f"O valor de B é: {b}")
print(f"O valor de C é: {c}")

#Angulo:

if a**2 == (b**2 + c**2):
    print("O triangulo formado é um triangulo retangulo")
elif a**2 > (b**2 + c**2):
    print("O triangulo formado é um triangulo obtusangulo")
elif a**2 < (b**2 + c**2):
    print("O triangulo formado é um triangulo acutangulo")

#Lados:

if a == b == c:
    print("O triangulo formado é um triangulo equilatero")
elif a == b or b == c or c == a:
    print("O triangulo formado é um tringulo isosceles")
elif a >= b+c:
    print("Triangulo não formado")