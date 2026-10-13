from conta import Conta


def menu_cliente(cliente_id, nome):
    numero_conta = None

    while True:
        print(f"\n=== Menu do Cliente: {nome} (ID {cliente_id}) ===")
        print("1 - Criar conta")
        print("2 - Consultar saldo")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Transferir")
        print("6 - Extrato")
        print("7 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero_conta = Conta.criar(cliente_id)
            print(f"Conta criada: {numero_conta}")

        elif opcao == "2":
            if numero_conta is None:
                print("Você ainda não possui uma conta")
                continue

            conta = Conta.consultar(numero_conta)

            if conta:
                print(f"\nSaldo: R$ {conta[2]:.2f}")

        elif opcao == "3":
            if numero_conta is None:
                print("Você ainda não possui uma conta")
                continue
            try:
                valor = float(input("Valor do deposito: R$ "))
                Conta.depositar(numero_conta, valor)
            except ValueError:
                print("Digite um valor válido")

        elif opcao == "4":
            if numero_conta is None:
                print("Você ainda não possui uma conta")
                continue
            try:
                valor = float(input("Valor do saque: R$ "))
                Conta.sacar(numero_conta, valor)
            except ValueError:
                print("Digite um valor válido.")

        elif opcao == "5":
            if numero_conta is None:
                print("Você ainda não possui uma conta")
                continue
            try:
                destino = int(input("Número da conta destino: "))
                valor = float(input("Valor da transferência: R$ "))
                Conta.transferir(numero_conta, destino, valor)
            except ValueError:
                print("Digite valores válidos.")

        elif opcao == "6":
            if numero_conta is None:
                print("Você ainda não possui uma conta")
                continue
            Conta.extrato(numero_conta)

        elif opcao == "7":
            break

        else:
            print("Opção inválida.")
