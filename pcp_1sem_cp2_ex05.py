def aprovar(idade, renda, valor, parcelas):
    return True

def definir_taxa(parcelas):
    return 0.02

def calcular_parcela(valor, taxa, parcelas):
    return (valor * (1 + taxa)) / parcelas

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor


nome_do_cliente = input("Digite o nome do cliente: ")
idade_do_cliente = int(input("Digite a idade do cliente: "))
renda_mensal = float(input("Digite a renda mensal: "))
val_emprestimo = float(input("Digite o valor do empréstimo: "))
num_parcelas = int(input("Digite o número de parcelas: "))


if aprovar(idade_do_cliente, renda_mensal, val_emprestimo, num_parcelas):
    print("Aprovado")

    taxa = definir_taxa(num_parcelas)
    parcela = calcular_parcela(val_emprestimo, taxa, num_parcelas)
    total = calcular_total(parcela, num_parcelas)
    juros = calcular_juros(total, val_emprestimo)

    print(f"Parcela: R$ {parcela:.2f}")
    print(f"Total: R$ {total:.2f}")
    print(f"Juros: R$ {juros:.2f}")

else:
    print("Negado")
