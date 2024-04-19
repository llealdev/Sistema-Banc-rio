print(f"""
-------- Bem-vindo ao BitBank --------
                Menu              
[1] Depositar
[2] Sacar
[4] Extrato
[5] Sair
""")

saldo = 0
saque = 500
extrato = " "
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input("\nO que senhor(a) desejaria fazer ? "))

    if opcao == 1:
        valor = float(input("\nQuanto o senhor desejaria depositar: R$"))

        if valor > 0:
            saldo += valor
            extrato += f"Déposito: {valor:.2f}\n"
        else:
            print("Valor inválido")

    elif opcao == 2:
        valor = float(input("\nQuanto o senhor desejaria sacar: R$"))

        excedeu_valor_de_saque = valor > saque
        excedeu_saldo = valor > saldo
        excedeu_limite_saque = numero_saque > LIMITE_SAQUES

        if excedeu_valor_de_saque:
            print("Valor de saque excedido")

        elif excedeu_saldo:
            print("Saldo insuficiente")
        
        elif excedeu_limite_saque:
            print("Limite de saque diário alcançado")
        
        elif valor > 0:
            saldo -= valor
            numero_saque += 1
            extrato = f"Saque:{valor:.2f}"

        else: 
            print("Operção falhou! O Valor informado é inválido")

    elif opcao == 4:
        print("\n-------- Extrato --------\n")
        print("Não foram realizadas movimentações. \n"if not extrato else extrato)
        print(f"Saldo:{saldo:.2f}\n")
    
    elif opcao == 5:
        break
        
else:
    print("\nOeração inválida. por favor selecione outra opção ")
    


        

