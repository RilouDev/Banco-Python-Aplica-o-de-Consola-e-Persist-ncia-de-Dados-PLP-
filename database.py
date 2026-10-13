import sqlite3

DATABASE = 'banco.db'

def conectar():
    return sqlite3.connect(DATABASE)

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero INTEGER UNIQUE NOT NULL,
        cliente_id INTEGER NOT NULL,
        saldo REAL DEFAULT 0,
        FOREIGN KEY (cliente_id) REFERENCES clientes (id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        conta_id INTEGER NOT NULL,
        tipo TEXT NOT NULL,
        valor REAL NOT NULL,
        data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (conta_id) REFERENCES contas (id)
    )""")

    conexao.commit()
    conexao.close()


def criar_tabelas():
    """Alias compatível com scripts que importam criar_tabelas()."""
    return criar_tabela()