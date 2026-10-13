from database import criar_tabelas
from cliente import Cliente
from banco import menu_cliente


def main():

    criar_tabelas()

    while True:

        print("""
==============================
       BANCO PYTHON
==============================

1 - Criar cliente
2 - Login
3 - Sair

==============================
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            nome = input("Nome: ")
            cpf = input("CPF: ")
            senha = input("Senha: ")

            cliente_id = Cliente.cadastrar(
                nome,
                cpf,
                senha
            )

            if cliente_id:
                print(f"Seu ID de cliente é: {cliente_id}")

        elif opcao == "2":

            cpf = input("CPF: ")
            senha = input("Senha: ")

            cliente = Cliente.login(cpf, senha)

            if cliente:

                cliente_id, nome = cliente

                print(f"\n✅ Login realizado!")
                print(f"Bem-vindo, {nome}!")

                menu_cliente(
                    cliente_id,
                    nome
                )

            else:
                print("\n❌ CPF ou senha incorretos.")

        elif opcao == "3":

            print("\nObrigado por utilizar o Banco Python!")
            break

        else:
            print("\n❌ Opção inválida.")


if __name__ == "__main__":
    main()