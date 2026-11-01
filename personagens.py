"""
personagens.py - Funções da tabela PERSONAGENS.

Colunas: id, nome, nivel, jogador_id, classe_id

jogador_id e classe_id são CHAVES ESTRANGEIRAS: guardam o id de um
jogador e de uma classe. Para mostrar o APELIDO do jogador e o NOME da
classe, junte as tabelas com JOIN.

As consultas (buscar_por_id, buscar_por_nome e listar) devem devolver
as colunas nesta ordem, que é a ordem que o main.py mostra na tela:
    (id, nome, nivel, apelido do jogador, nome da classe)

TAREFA: complete as 4 funções.
"""

# Parte comum das consultas. Complete o segundo JOIN (classes).
CONSULTA = """
    SELECT personagens.id, personagens.nome, personagens.nivel,
           jogadores.apelido, classes.nome
    FROM personagens
    JOIN jogadores ON jogadores.id = personagens.jogador_id
    JOIN classes ON classes.id = personagens.classe_id
"""


def incluir(conn, nome, nivel, jogador_id, classe_id):
    cursor = conn.execute("INSERT INTO personagens (nome, nivel, jogador_id, classe_id) VALUES (?)", (nome, nivel, jogador_id, classe_id,))
    conn.commit()               
    return cursor.lastrowid


def buscar_por_id(conn, id):
    cursor = conn.execute(CONSULTA + "SELECT id, nome FROM personagens WHERE id = ?", (id,))
    return cursor.fetchone()


def buscar_por_nome(conn, nome):
    cursor = conn.execute(
        "SELECT id, nome FROM personagens WHERE nome LIKE ? ORDER BY nome",
        ("%" + nome + "%",))
    return cursor.fetchall()


def listar(conn):
    cursor = conn.execute("SELECT id, , nivel, jogador_id, classe_id FROM personagens ORDER BY id")
    return cursor.fetchall()
