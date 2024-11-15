# from Turma import Turma
# from Aluno import Aluno
# from Disciplina import Disciplina
# from Database.connection import database, create_db
#
# engine = database()
# create_db(engine)
#
# aluno1 = Aluno("Lucas", 322126458, "lucas@hotmail.com")
# aluno2 = Aluno("Grazi", 322126459, "grazi@gmail.com")
# aluno3 = Aluno("Bernardo", 322126460, "bernardo@gmail.com")
#
# disciplina1 = Disciplina("Sistemas Distribuídos", "SD101")
# disciplina2 = Disciplina("Desenvolvimento WEB", "DEV102")
#
# turma1 = Turma(disciplina1, "T01")
# turma2 = Turma(disciplina2, "T02")
#
#
# #Adicionando a Turma 1
# turma1.adicionar_aluno_turma(aluno1)
# turma1.adicionar_aluno_turma(aluno2)
# #Adicionando a Turma 2
# turma2.adicionar_aluno_turma(aluno3)
# #Listando alunos da turma 1
# turma1.listar_alunos()
# #Listando alunos da turma
# print("\n")
# turma2.listar_alunos()
# #Pesquisar aluno por matrícula
# print("\n")
# turma1.buscar_por_matricula(322126459)
# #Atualizando dados de 1 aluno
# print("\n")
# aluno3.atualizar_aluno()
# #Testar remover aluno de uma turma
# print("\n")
# turma1.remover_aluno_turma(322126459)
# turma1.listar_alunos()

from Controllers.Controller_Aluno import *
from Controllers.Controller_Disciplina import *
from Controllers.Controller_Turma import *
from Aluno import Aluno
from Disciplina import Disciplina
from Turma import Turma
from Database.connection import database, create_session, create_db, Base


# Função principal de teste
def main():
    # Conexão com o banco de dados
    engine = database()
    create_db(engine)  # Cria as tabelas no banco de dados se não existirem
    session = create_session(engine)

    # --- Testando Aluno ---
    # Criar um novo aluno
    # aluno1 = Aluno(nome="Lucas", matricula="2021001", email="lucas@email.com")
    # aluno2 = Aluno(nome="Grazi", matricula="2021002", email="grazi@email.com")
    aluno3 = Aluno(nome="Vitor", matricula="2021005", email="vitor@email.com")
    # adicionar_aluno(aluno1)
    # adicionar_aluno(aluno2)
    adicionar_aluno(aluno3)

    # Buscar o aluno pela matrícula
    aluno_busca = buscar_aluno_por_matricula("2021001")
    if aluno_busca:
        print(f"Aluno encontrado: {aluno_busca.nome}, {aluno_busca.email}")

    # Atualizar o aluno
    atualizar_aluno("2021001", novo_nome="Lucas Rocha", novo_email="lucas.rocha@email.com")

    # Deletar o aluno
    deletar_aluno("2021001")

    # --- Testando Disciplina ---
    # Criar uma nova disciplina
    disciplina1 = Disciplina(nome="Matemática", codigo="MAT101")
    disciplina2 = Disciplina(nome="Artes", codigo="ART103")
    adicionar_disciplina(disciplina1)
    adicionar_disciplina(disciplina2)

    # Buscar disciplina por código
    disciplina_busca = buscar_disciplina_por_codigo("MAT101")
    if disciplina_busca:
        print(f"Disciplina encontrada: {disciplina_busca.nome}, {disciplina_busca.codigo}")

    # Atualizar a disciplina
    atualizar_disciplina("MAT101", novo_nome="Matemática Avançada")

    # Deletar a disciplina
    deletar_disciplina("MAT101")

    # --- Testando Turma ---
    # Criar uma nova turma
    turma1 = Turma(disciplina=disciplina2, codigo="TURMA03")
    adicionar_turma(turma1)

    # Buscar turma por código
    turma_busca = buscar_turma_por_codigo("TURMA01")
    if turma_busca:
        print(f"Turma encontrada: {turma_busca.codigo}")

    # Adicionar aluno à turma
    adicionar_aluno_turma("TURMA01", "2021002")  # Usando a matrícula do aluno

    # Remover aluno da turma
    remover_aluno_turma("TURMA01", "2021002")

    # Fechar a sessão ao final
    session.close()


if __name__ == "__main__":
    main()
