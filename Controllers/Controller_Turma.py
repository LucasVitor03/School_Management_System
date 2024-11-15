from Database.models import TurmaModel, AlunoModel, DisciplinaModel
from Database.connection import database, create_session, Base

engine = database()
session = create_session(engine)


# Operações CRUD
def adicionar_turma(turma):
    # Verifica se a disciplina já está no banco
    disciplina = session.query(DisciplinaModel).filter_by(codigo=turma.disciplina.codigo).first()

    if not disciplina:
        print(f"Disciplina {turma.disciplina.codigo} não encontrada no banco de dados.")
        return

    # Relação turma disciplina
    turma_model = TurmaModel(codigo=turma.codigo, disciplina_id=turma.disciplina.id, alunos=turma.alunos)

    # Adiciona à sessão
    session.add(turma_model)
    session.commit()
    session.close()
    print(f"Turma {turma.codigo} adicionada com sucesso.")


def buscar_turma_por_codigo(codigo):
    turma = session.query(TurmaModel).filter_by(codigo=codigo).first()
    return turma

def atualizar_turma(codigo, nova_disciplina=None):
    turma = buscar_turma_por_codigo(codigo)
    if turma:
        if nova_disciplina:
            turma.disciplina = nova_disciplina
        session.commit()
        print(f"Turma {codigo} atualizada com sucesso.")
    else:
        print(f"Turma com código {codigo} não encontrada.")

def deletar_turma(codigo):
    turma = buscar_turma_por_codigo(codigo)
    if turma:
        session.delete(turma)
        session.commit()
        print(f"Turma {codigo} deletada com sucesso.")
    else:
        print(f"Turma com código {codigo} não encontrada.")


def adicionar_aluno_turma(codigo_turma, matricula_aluno):
    session = create_session(engine)

    # Buscar a turma pelo código
    turma = session.query(TurmaModel).filter_by(codigo=codigo_turma).first()
    # Buscar o aluno pela matrícula
    aluno = session.query(AlunoModel).filter_by(matricula=matricula_aluno).first()

    if turma and aluno:
        # Adicionar o aluno à turma
        turma.alunos.append(aluno)
        session.commit()
        print(f"Aluno {aluno.nome} adicionado à turma {turma.codigo}.")
    else:
        print("Turma ou aluno não encontrado.")

    session.close()


def remover_aluno_turma(codigo_turma, matricula_aluno):
    session = create_session(engine)

    # Buscar a turma pelo código
    turma = session.query(TurmaModel).filter_by(codigo=codigo_turma).first()
    # Buscar o aluno pela matrícula
    aluno = session.query(AlunoModel).filter_by(matricula=matricula_aluno).first()

    if turma and aluno:
        # Remover o aluno da turma
        turma.alunos.remove(aluno)
        session.commit()
        print(f"Aluno {aluno.nome} removido da turma {turma.codigo}.")
    else:
        print("Turma ou aluno não encontrado.")

    session.close()