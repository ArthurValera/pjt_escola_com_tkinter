import sqlite3

#conectando ao banco

try:
    conn = sqlite3.connect('alunos.db')
    print("Conexão ao banco de dados com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados:", e)
    
#criando a tabela de alunos
try:
    with conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS alunos(
            matricula INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            sexo TEXT NOT NULL,
            n1 REAL NOT NULL,
            n2 REAL NOT NULL,
            n3 REAL NOT NULL,
            media REAL NOT NULL,
            situacao TEXT NOT NULL
        )""")
        print("Tabela de alunos criada com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar tabela alunos:", e)