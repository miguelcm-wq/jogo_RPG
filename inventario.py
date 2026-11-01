"""
inventario.py - Funções da tabela INVENTARIO.   (DESAFIO)

Colunas: id, personagem_id, item_id, quantidade

Cada linha do inventário diz que um PERSONAGEM carrega um ITEM, em uma
certa quantidade. A busca "por nome" deve procurar pelo nome do PERSONAGEM.

As consultas devem devolver as colunas nesta ordem:
    (id, nome do personagem, nome do item, tipo do item, quantidade)

TAREFA: escreva a CONSULTA (com dois JOINs) e complete as 4 funções.
Dica: o arquivo personagens.py faz algo muito parecido.
"""

CONSULTA = """
    -- TODO: SELECT ... FROM inventario JOIN personagens ... JOIN itens ...
"""


def incluir(conn, personagem_id, item_id, quantidade):
    cursor = conn.execute("INSERT INTO inventario (personagem_id, item_id, quantidade) VALUES (?, ?, ?)", (personagem_id, item_id, quantidade,))
    conn.commit()                 
    return cursor.lastrowid


def buscar_por_id(conn, id):
    cursor = conn.execute("SELECT id, nome_personagem FROM inventario WHERE id = ?", (id,))
    return cursor.fetchone()


def buscar_por_nome(conn, nome_personagem):
    cursor = conn.execute(
        "SELECT id, nome_personagem FROM inventario WHERE nome_personagem LIKE ? ORDER BY nome_personagem",
        ("%" + nome_personagem + "%",))
    return cursor.fetchall()  

    
def listar(conn):
    cursor = conn.execute("SELECT id, personagem_id, item_id, quantidade FROM inventario ORDER BY id")
    return cursor.fetchall()
