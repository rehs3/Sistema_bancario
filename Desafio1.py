menu = """
=========== MENU ===========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
==============================
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE= 3

while True:
    opcao = input(menu)
    if opcao == '1':
        valor = float(input("Digite o valor que deseja depositar:"))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
             print("OPERACAO FALHOU!")
        
    elif opcao == '2':
        valor = float(input("Digite o valor que deseja sacar:"))
        excedeu_saldo = valor >saldo
        excedeu_limite = valor >limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Operacao falhou! voce nao possui saldo suficiente")
        elif excedeu_limite:
            print("operacao falou! excedeu o limite")
        elif excedeu_saques:
            print("Operacao falhou! voce excedeu o limite de saques")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operacao falhou! o valor informado e invalido")
        
    elif opcao == '3':
        print("\n ============= EXTRATO =============")
        print("Nao foram realizados movimentos." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================")
        
    elif opcao == '4':
        break
    
    else:
        print("Operacao invalida, por favor selecione novamente.")
