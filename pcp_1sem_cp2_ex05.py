nome_do_cliente = input("Digite o nome do cliente: ")
idade_do_cliente = int(input("Digite a idade do cliente: "))
renda_mensal = float(input("Digite a renda mensal: "))
val_emprestimo = float(input("Digite o valor do empréstimo: ") )
num_parcelas = int(input("Digite o número de parcelas: "))

if idade_do_cliente > 18 and (num_parcelas == 3 or num_parcelas == 24):
    print("Aprovado")
else:
    ("Negado")