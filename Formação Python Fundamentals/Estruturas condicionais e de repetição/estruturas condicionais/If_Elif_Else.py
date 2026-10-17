#Exemplo 1(if)
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo <= saque:
    print("Saldo Insuficiente!")

#Exemplo 2(if/else)
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo Insuficiente!")

#Exemplo 3(if/elif/else)
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para saque: "))
elif opcao == 2:
    print("Exibindo o extrato: ")
else:
    sys.exit("Opção Invalida")