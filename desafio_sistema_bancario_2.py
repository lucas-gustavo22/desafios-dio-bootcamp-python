import textwrap

def menu():

    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuario
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"\n+ R$ {valor:.2f}"
        print("✅ Depósito realizado com sucesso")
    else:  
        print("⚠️ ERRO! Digite um valor válido para depósito!")
    
    return saldo, extrato

    

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("❌ Saldo insuficiente")
    
    elif excedeu_limite:
        print(f"❌ O valor que deseja sacar é maior que o limite diário de R${limite}")

    elif excedeu_saques:
        print("❌ Limite de saques diários atingido!")
    
    elif valor > 0:
        numero_saques += 1
        saldo -= valor
        extrato += f"\n- R$ {valor:.2f}"
        print("✅ Saque realizado com sucesso")
    
    else:
        print("❌ Operação falhou. O valor informado é inválido!")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n########## EXTRATO ##########")
    print("Nenhuma movimentação realizada." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("###############################")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n❌ Já existe um usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

    print("\n✅ Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuarios:
        print("\n✅ Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n❌ Usuário não encontrado. Não foi possível criar a conta!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            if numero_saques < LIMITE_SAQUES:
                valor = float(input("Digite o valor: "))
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema bancário! 👋")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()