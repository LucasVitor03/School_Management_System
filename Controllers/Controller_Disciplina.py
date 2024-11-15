from Disciplina import Disciplina
from Database.models import DisciplinaModel
from Database.connection import database, create_session, Base


engine = database()
session = create_session(engine)


# Operações CRUD
def adicionar_disciplina(disciplina):
    # Verifica se a disciplina com o código já existe
    disciplina_existente = session.query(DisciplinaModel).filter_by(codigo=disciplina.codigo).first()

    if disciplina_existente:
        print(f"Disciplina com o código {disciplina.codigo} já existe no banco de dados.")
        return  # Não insere novamente

    # Adiciona a nova disciplina se não existir
    disciplina_model = DisciplinaModel(nome=disciplina.nome, codigo=disciplina.codigo)
    session.add(disciplina_model)
    session.commit()
    # session.close()

    print(f"Disciplina {disciplina.codigo} adicionada com sucesso.")

def buscar_disciplina_por_codigo(codigo):
    disciplina = session.query(DisciplinaModel).filter_by(codigo=codigo).first()
    return disciplina

def atualizar_disciplina(codigo, novo_nome=None):
    disciplina = buscar_disciplina_por_codigo(codigo)
    if disciplina:
        if novo_nome:
            disciplina.nome = novo_nome
        session.commit()
        print(f"Disciplina {codigo} atualizada com sucesso.")
    else:
        print(f"Disciplina com código {codigo} não encontrada.")

def deletar_disciplina(codigo):
    disciplina = buscar_disciplina_por_codigo(codigo)
    if disciplina:
        session.delete(disciplina)
        session.commit()
        print(f"Disciplina {codigo} deletada com sucesso.")
    else:
        print(f"Disciplina com código {codigo} não encontrada.")
