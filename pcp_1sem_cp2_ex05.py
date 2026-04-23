#1. O programa deve solicitar:
nome = input("Digite o nome do cliente: \n")
idade = int(input("Digite a idade do cliente: \n"))
renda = float(input("Digite a renda mensal do cliente: \n"))
valor = float(input("Digite o valor desejado do emprestimo: \n"))
parcelas = int(input("Digite o numero de parcelas de 3 até 24: \n"))

#2. Regras para aprovação:
def pode_aprovar(idade, renda, valor):
    if idade < 18:
    
        return ("Empréstimo negado: cliente menor de idade.")
    elif valor > 20 * renda:

        return ("Empréstimo negado: valor acima do limite permitido.")
    else:
        return True


#Taxa de juros:
def definir_taxa(parcelas):
    if parcelas < 7:
        taxa = 0.05
    elif parcelas > 7 and parcelas < 13:
        taxa = 0.08
    else:
        taxa = 0.1
    return taxa

#Cálculo do financiamento (parcelas fixas):
def calcular_parcela(valor, taxa, parcelas):
    valor_da_parcela = valor * (taxa *(1 + taxa)**parcelas) / ((1 + taxa)**parcelas - 1)
    return valor_da_parcela

#Total pago
def calcular_total(parcela, parcelas):
    total = parcela * parcelas
    return total

#Juros pagos
def calcular_juros(total, valor):
    juros = total - valor
    return juros


#O sistema deve informar
resultado = pode_aprovar(idade, renda, valor)
if resultado == True:
    taxa = definir_taxa(parcelas)
    parcela = calcular_parcela(valor, taxa, parcelas)
    total = calcular_total(parcela, parcelas)
    juros = calcular_juros(total, valor)

    print("Emprestimo aprovado")
    print(f"nome do cliente:\n{nome}")
    print(f"O valor do emprestimo é de:\n{valor}")
    print(f"A taxa de juros do seu emprestimo é de:\n{taxa}")
    print(f"O valor de cada parcela ficou em:\n{parcela:.2f}")
    print(f"O total pago sera de:\n{total:.2f}")
    print(f"Os juros pagos serao de:\n{juros:.2f}")