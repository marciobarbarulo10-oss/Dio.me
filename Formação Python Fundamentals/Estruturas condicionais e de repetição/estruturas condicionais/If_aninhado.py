#Exemplo 1
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque: 
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficente!")