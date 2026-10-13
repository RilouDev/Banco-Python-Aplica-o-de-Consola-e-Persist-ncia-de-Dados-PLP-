from database import conectar


class Conta:

    @staticmethod
    def criar (cliente_id):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT MAX (numero)
            FROM contas
        """)

        ultimo_numero = cursor.fetchone()[0]

        if ultimo_numero is None:
            numero_conta = 1001
        else:
            numero_conta = ultimo_numero + 1

        cursor.execute("""
            INSERT INTO contas (numero, cliente_id, saldo) VALUES (?, ?, 0)
        """, (numero_conta, cliente_id))

        conexao.commit()
        conexao.close()

        print(f"Conta criada com sucesso! Número da conta: {numero_conta}")

        return numero_conta

    @staticmethod
    def consultar(numero):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, cliente_id, saldo FROM contas WHERE numero = ?
        """, (numero,))

        conta = cursor.fetchone()
        conexao.close()
        return conta

    @staticmethod
    def depositar(numero, valor):
        if valor <= 0:
            print("O valor depositado deve ser maior que zero.")
            return

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE contas
            SET saldo = saldo + ?
            WHERE numero = ?
        """, (valor, numero))

        conta = Conta.consultar(numero)

        if conta:
            conta_id = conta[0]

            cursor.execute("""
                INSERT INTO transacoes
                (conta_id, tipo, valor)
                VALUES (?, ?, ?)
            """, (conta_id, 'Depósito', valor))

        conexao.commit()
        conexao.close()

        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    @staticmethod
    def sacar(numero, valor):
        if valor <= 0:
            print("O valor sacado deve ser maior que zero.")
            return

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, saldo
            FROM contas
            WHERE numero = ?
        """, (numero,))

        conta = cursor.fetchone()

        if not conta:
            print("Conta não encontrada.")
            conexao.close()
            return

        conta_id, saldo = conta

        if valor > saldo:
            print("Saldo insuficiente para realizar o saque.")
            conexao.close()
            return

        cursor.execute("""
            UPDATE contas
            SET saldo = saldo - ?
            WHERE numero = ?
        """, (valor, numero))

        cursor.execute("""
            INSERT INTO transacoes
            (conta_id, tipo, valor)
            VALUES (?, ?, ?)
        """, (conta_id, 'Saque', valor))

        conexao.commit()
        conexao.close()

        print(f"Saque de R${valor:.2f} realizado com sucesso.")

    @staticmethod
    def transferir(origem, destino, valor):
        if valor <= 0:
            print("O valor transferido deve ser maior que zero.")
            return
        
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, saldo
            FROM contas
            WHERE numero = ?
        """, (origem,))

        conta_origem = cursor.fetchone()

        cursor.execute("""
            SELECT id
            FROM contas
            WHERE numero = ?
        """, (destino,))

        conta_destino = cursor.fetchone()

        if not conta_origem or not conta_destino:
            print("Conta de origem ou destino não encontrada.")
            conexao.close()
            return

        origem_id, saldo= conta_origem
        destino_id = conta_destino[0]

        if valor > saldo:
            print("Saldo insuficiente para realizar a transferência.")
            conexao.close()
            return

        cursor.execute("""
            UPDATE contas
            SET saldo = saldo - ?
            WHERE numero = ?
        """, (valor, origem))

        cursor.execute("""
            UPDATE contas
            SET saldo = saldo + ?
            WHERE numero = ?
        """, (valor, destino))

        cursor.execute("""
            INSERT INTO transacoes
            (conta_id, tipo, valor)
            VALUES (?, ?, ?)
        """, (origem_id, 'Transferência enviada', valor))

        cursor.execute("""
            INSERT INTO transacoes
            (conta_id, tipo, valor)
            VALUES (?, ?, ?)
        """, (destino_id, 'Transferência recebida', valor))

        conexao.commit()
        conexao.close()

        print(f"Transferência de R${valor:.2f} realizada com sucesso.")

    @staticmethod
    def extrato(numero):

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT c.nome, ct.numero, ct.saldo
            FROM contas ct
            INNER JOIN clientes c
            ON ct.cliente_id = c.id
            WHERE ct.numero = ?
        """, (numero,))

        conta = cursor.fetchone()

        if not conta:
            print("Conta não encontrada")
            conexao.close()
            return

        nome, numero_conta, saldo = conta

        print("\n========== EXTRATO ==========")
        print(f"Titular: {nome}")
        print(f"Conta: {numero_conta}")
        print(f"Saldo: R$ {saldo:.2f}")

        cursor.execute("""
            SELECT tipo, valor, data
            FROM transacoes
            WHERE conta_id = (
                SELECT id
                FROM contas
                WHERE numero = ?
            )
            ORDER BY data DESC
        """, (numero,))

        transacoes = cursor.fetchall()

        print("\n--- Histórico ---")

        if not transacoes:
            print("Nenhuma movimentação")

        for tipo, valor, data in transacoes:
            print(f"{data} | {tipo} | R${valor:.2f}")

        print("==============================")