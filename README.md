# 🏦 Sistema Bancário em Python (SQLite)

Projeto desenvolvido durante as aulas da disciplina de **Paradigmas de Linguagem de Programação (PLP)**.

## 📌 Sobre o Projeto
Trata-se de um sistema bancário em consola (terminal) construído em Python, com persistência de dados relacional utilizando **SQLite**. O sistema simula as principais rotinas de uma instituição financeira, desde o cadastro e autenticação de utilizadores até a execução de transações em tempo real.

## 🚀 Funcionalidades
- **Gestão de Clientes:** Registo de novos utilizadores com validação de unicidade por CPF e sistema de login.
- **Contas Bancárias:** Abertura de conta corrente vinculada ao cliente, com numeração automática sequencial (a iniciar em 1001).
- **Operações Financeiras:**
  - Consulta de saldo em tempo real.
  - Depósitos e saques com verificação de saldo disponível.
  - Transferências entre contas cadastradas com validação de saldo e verificação da conta destino.
- **Extrato Detalhado:** Histórico ordenado de todas as movimentações financeiras executadas.

## 🛠️ Tecnologias e Conceitos Utilizados
- **Linguagem:** Python 3
- **Base de Dados:** SQLite3 (`banco.db`)
- **Conceitos de PLP:** Modularização de código (`main`, `banco`, `cliente`, `conta`, `database`), manipulação de dados relacionais, funções estáticas, tratamento de exceções e estruturas condicionais/de repetição.

## 📁 Estrutura do Código
- `main.py`: Ponto de entrada do programa e menu inicial (Cadastro/Login).
- `cliente.py`: Regra de negócio para registo e autenticação de clientes.
- `conta.py`: Regras das operações financeiras (depósito, saque, transferência, extrato).
- `banco.py`: Menu interativo das operações bancárias do cliente logado.
- `database.py`: Criação e gestão do esquema das tabelas na base de dados SQLite.
