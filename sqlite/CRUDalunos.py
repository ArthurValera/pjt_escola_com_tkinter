import sqlite3 as lite

# Estabelecendo conexão
try:
    conn = lite.connect('alunos.db')
    print("Conexão ao banco de dados com sucesso!")
except lite.Error as e:
    print("Erro ao conectar com o banco de dados:", e)

# Função para cálculo de média e atualizar a situação
def calcula_media_situacao(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    situacao = "Aprovado" if media >= 6.0 else "Reprovado"
    return media, situacao

# CREATE
def cria_aluno(i):
    n1, n2, n3 = float(i[4]), float(i[5]), float(i[6])
    media, situacao = calcula_media_situacao(n1, n2, n3)
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO alunos (matricula, nome, idade, sexo, n1, n2, n3, media, situacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i + [media, situacao])

# READ
def ve_aluno():
    lista = []
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM alunos')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
        return lista

# UPDATE
def atualiza_aluno(i):
    n1, n2, n3 = float(i[4]), float(i[5]), float(i[6])
    media, situacao = calcula_media_situacao(n1, n2, n3)
    with conn:
        cur = conn.cursor()
        query = "UPDATE alunos SET nome=?, idade=?, sexo=?, n1=?, n2=?, n3=?, media=?, situacao=? WHERE matricula=?"
        cur.execute(query, [i[1], i[2], i[3], i[4], i[5], i[6], media, situacao, i[0]])

# DELETE
def deleta_aluno(matricula):
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM alunos WHERE matricula=?"
        cur.execute(query, (matricula,))
