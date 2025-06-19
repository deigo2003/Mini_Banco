import getpass

menu = """
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
"""

banco = {
    "DIEGO": "d123",
    "ANA": "a123",
    "CARLOS": "c123"
}

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

nome = input("Qual o seu nome? ")
senha = getpass.getpass("Digite sua senha: ")

if banco.get(nome.upper()) == senha:
    print(f"\nBem-vindo, {nome}!\n")

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            deposito = float(input("Quanto você deseja depositar: "))

            if deposito > 0:
                saldo += deposito
                extrato += f"Depósito: R$ {deposito:.2f}\n"
            else:
                print("Por favor, informe um valor positivo.")

        elif opcao == "s":
            saque = float(input("Informe o valor do saque: "))

            excedeu_saldo = saque > saldo
            excedeu_limite = saque > limite
            excedeu_saques = numero_saques >= limite_saques

            if excedeu_saldo:
                print("Falha: saldo insuficiente.")
            elif excedeu_limite:
                print(f"Falha: o valor máximo por saque é R$ {limite:.2f}.")
            elif excedeu_saques:
                print("Falha: número máximo de saques diários atingido.")
            elif saque > 0:
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                numero_saques += 1
            else:
                print("Operação falhou: valor inválido.")

        elif opcao == "e":
            print("\n===== EXTRATO =====")
            print(extrato if extrato else "Nenhuma movimentação.")
            print(f"Saldo atual: R$ {saldo:.2f}")
            print("====================\n")

        elif opcao == "q":
            print("Saindo... Obrigado por usar nosso banco!")
            break

        else:
            print("Operação inválida. Escolha uma opção válida do menu.")
else:
    print("Autenticação falhou: nome ou senha incorretos.")
