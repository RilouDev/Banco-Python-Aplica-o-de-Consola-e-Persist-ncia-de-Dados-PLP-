from database import conectar

class Cliente:
    @staticmethod
    def cadastrar_cliente(nome, cpf, senha):
        conexao = conectar()
        cursor = conexao.cursor()

        try:
            cursor.execute("""
                INSERT INTO clientes (nome, cpf, senha) VALUES (?, ?, ?)
                """, (nome, cpf, senha))

            conexao.commit()
            cliente_id = cursor.lastrowid
            print("Cliente cadastrado com sucesso!")

            return cliente_id

        except Exception:
            print("\n CPF já cadastrado. Tente novamente com outro CPF.")
            return None

        finally:
            conexao.close()

    @staticmethod
    def login(cpf, senha):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, nome FROM clientes WHERE cpf = ? AND senha = ?
            """, (cpf, senha))

        cliente = cursor.fetchone()
        conexao.close()

        return cliente  # Retorna None se não encontrar o cliente, ou uma tupla (id, nome) se encontrar

    @staticmethod
    def cadastrar(nome, cpf, senha):
        """Alias compatível com chamadas `Cliente.cadastrar(...)` em outros módulos."""
        return Cliente.cadastrar_cliente(nome, cpf, senha)