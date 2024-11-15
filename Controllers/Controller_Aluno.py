from Database.models import AlunoModel
from Database.connection import database, create_session, Base

engine = database()
session = create_session(engine)


# Operações CRUD
def adicionar_aluno(aluno):
    aluno_model = AlunoModel(nome=aluno.nome, matricula=aluno.matricula, email=aluno.email)
    session.add(aluno_model)
    session.commit()
    print(f"Aluno {aluno.nome} adicionado com sucesso.")


def buscar_aluno_por_matricula(matricula):
    aluno = session.query(AlunoModel).filter_by(matricula=matricula).first()
    return aluno


def atualizar_aluno(matricula, novo_nome=None, novo_email=None):
    aluno = buscar_aluno_por_matricula(matricula)
    if aluno:
        if novo_nome:
            aluno.nome = novo_nome
        if novo_email:
            aluno.email = novo_email
        session.commit()
        print(f"Aluno {matricula} atualizado com sucesso.")
    else:
        print(f"Aluno com matrícula {matricula} não encontrado.")


def deletar_aluno(matricula):
    aluno = buscar_aluno_por_matricula(matricula)
    if aluno:
        session.delete(aluno)
        session.commit()
        print(f"Aluno {matricula} deletado com sucesso.")
    else:
        print(f"Aluno com matrícula {matricula} não encontrado.")
