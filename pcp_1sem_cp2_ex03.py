nome_do_funcionario = input("Digite seu nome:\n")
cargo = input("Digite seu cargo (Gerente, Analista, Assistente, Estagíário):\n")
salario_base = float(input("Digite seu salario base por mês em R$:\n"))
horas = int(input("Digite quantas horas extras você trabalhou:\n"))
faltas = int(input("Digite quantas vezes você faltou no mês:\n"))
recebeu_bonus = input("Você recebeu bonus por desemprenho, sim ou não:\n")

def calcular_horas_extras(salario_base, horas):
  if horas > 0:
    horas_extras = (salario_base * 0.015) * horas
    return horas_extras
  else:
    return 0

def calcular_descontos_faltas(salario_base, faltas):
  if faltas > 0:
    descontos_faltas = (salario_base * 0.02) * faltas
    return descontos_faltas
  else:
    return 0

def calcular_bonus(cargo, recebeu_bonus):
  bonus = 0

  if recebeu_bonus == "sim":
    if cargo == "Gerente":
      bonus = 1000
    elif cargo == "Analista":
      bonus = 500
    elif cargo == "Assistente":
      bonus = 300
    elif cargo == "Estagiário":
      bonus = 100
      
  return bonus

salario_bruto = (calcular_horas_extras(salario_base, horas)) + (calcular_bonus(cargo, recebeu_bonus)) + salario_base
total_acrescimos = (calcular_horas_extras(salario_base, horas)) + (calcular_bonus(cargo, recebeu_bonus))
total_descontos = (calcular_descontos_faltas(salario_base, faltas))
salario_final = salario_bruto - total_descontos

print("O seu salario bruto desse mês é de: ", salario_bruto)
print("O total de acréscimos desse mês foi de: ", total_acrescimos)
print("O tatal de descontos desse mês foi de: ", total_descontos)
print("O seu salário liquido desse mês é de: ", salario_final) 