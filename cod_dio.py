menu = """
    [d] Deposito
    [s] Saque
    [e] Extrato
    [q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saque = 3

while True:
    
    opicao = input(menu)

    if opicao == "d":
        dep = float(input("quanto voce deseja depositar:"))

        if dep > 0:
            saldo += dep
            extrato += (f"Deposito: R$ {dep:.2f}\n")
        else:
            print("porfazor informe um valor positivo")
    
    elif opicao == "s":
        saq = float(input("informe o valor do saque:"))

        exedeu_saldo = saq > saldo
        exedeu_limite = saq > limite
        exedeu_saque = numero_saques >= limite_saque

        if exedeu_saldo:
            print("Falha, o saldo é menor que o saque")
        elif exedeu_limite:
            print("Falh, voce exedeu o limite de saque")
        elif exedeu_saque:
            print("Falha,voce o numero de saques para o dia")
        elif saq > 0:
            saldo -= saq
            extrato += f"saque R$:{saq:.2f}\n"
            numero_saques += 1
        else:
            print("operação falhou o valor é invalido")

    elif opicao == "e":
        print("\n=====EXTRATO=====")
        print("O extrato esta vazio" if not extrato else extrato)
        print(f"\nO valor da conta é {saldo:.2f}")
        print("===================")
    
    elif opicao == "q":
        break

    else:
        print("operacao invalida, verifique se estar tudo certo.")