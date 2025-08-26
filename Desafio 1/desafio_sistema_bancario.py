menu = """

#### Caixa Eletrônico ####

Selecione a opção desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_d = float(input("Digite o valor: "))
        if valor_d > 0:
            saldo += valor_d
            extrato += f"\n+ R$ {valor_d:.2f}"
            print("✅ Depósito realizado com sucesso")
        else:  
            print("⚠️ ERRO! Digite um valor válido para depósito!")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor_s = float(input("Digite o valor: "))

            if valor_s < 0:
                print("⚠️ ERRO! Digite um valor válido para depósito!")
            elif valor_s > saldo:
                 print("❌ Saldo insuficiente")
            elif valor_s > limite:
                print(f"O valor que deseja sacar é maior que o limite diário de R${limite}")
            else:
                numero_saques += 1
                saldo -= valor_s
                extrato += f"\n- R$ {valor_s:.2f}"
                print("✅ Saque realizado com sucesso")
        else:
            print("⚠️ ERRO! Limite de saques diários atingido!")
    
    elif opcao == "e":
        print("\n##### EXTRATO #####")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("###################")

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema bancário! 👋")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
