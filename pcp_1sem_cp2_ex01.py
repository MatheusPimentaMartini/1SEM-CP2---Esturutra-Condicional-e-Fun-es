#Faça um programa que recebe:
#O código do estado de origem da carga de um caminhão, supondo que é um número inteiro de 1 a 5
#o peso da carga do caminhão em toneladas
#o código da carga, supondo que é um número inteiro de 10 a 40

#Código do estado de origem:
while True:
    codigo_origem = int(input("Escreva o codigo de origem de 1 a 5: "))

    if codigo_origem < 1 or codigo_origem > 5:
        print("Número inválido, tente novamente.\n")
    else:
        
        break

#Peso da carga do caminhão em toneladas
peso_toneladas = float(input("Digite o peso da sua carga em toneladas: "))

#código da carga
while True:
    codigo_carga = int(input("Digite o codigo da carga (10 a 40): "))

    if codigo_carga < 10 or codigo_carga > 40:
        print("Codigo invalido, digite novamente:\n")
    else:
        
        break
   
#SEU PROGRAMA DEVE CALCULAR:
#O PESO DA CARGA DO CAMINHÃO CONVERTIDO EM QUILOS 
#O PREÇO DA CARGA DO CAMINHÃO
#O VALOR DO IMPOSTO QUE E COBRADO COM BASE NO PREÇO DA CARGA E DO ESTADO DE ORIGEM
#O VALOR TOTAL TRANSPORTADO PELO CAMINHÃO (Carga + impostos)

#O PESO DA CARGA DO CAMINHÃO CONVERTIDO EM QUILOS
peso_quilos = peso_toneladas *1000

#O PREÇO DA CARGA DO CAMINHÃO

def preço_carga(codigo_carga, peso_quilos): 
    if codigo_carga >= 10 and codigo_carga <= 20: 
        preco = peso_quilos * 100
    elif codigo_carga >= 21 and codigo_carga <= 30: 
        preco = peso_quilos * 250
    else: 
        preco = peso_quilos * 340

    return preco


#O VALOR DO IMPOSTO QUE E COBRADO COM BASE NO PREÇO DA CARGA E DO ESTADO DE ORIGEM
def valor_imposto(codigo_origem, preco):
    if codigo_origem == 1:
        imposto = preco * 0.35
    elif codigo_origem == 2:
        imposto = preco * 0.25
    elif codigo_origem == 3:
        imposto = preco * 0.15
    elif codigo_origem == 4:
        imposto = preco * 0.05
    else:
        imposto = 0

    return imposto

# Cálculos
preco = preço_carga(codigo_carga, peso_quilos)
imposto = valor_imposto(codigo_origem, preco)
total = preco + imposto
print(f"\nPeso da carga em quilos: {peso_quilos:.2f} kg")
print(f"Preço da carga: R$ {preco:.2f}")
print(f"Valor do imposto: R$ {imposto:.2f}")
print(f"Valor total transportado (carga + impostos): R$ {total:.2f}")