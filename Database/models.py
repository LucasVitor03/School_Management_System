from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Date, Table
from sqlalchemy.orm import relationship
from Database.connection import Base


# Tabela de associação entre Alunos e Turmas
aluno_turma_association = Table(
    'aluno_turma', Base.metadata,
    Column('aluno_id', ForeignKey('alunos.id'), primary_key=True),
    Column('turma_id', ForeignKey('turmas.id'), primary_key=True)
)


# Definindo o modelo SQLAlchemy no models
class AlunoModel(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    matricula = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    # Relacionamento bidirecional entre Alunos e Turmas
    turmas = relationship('TurmaModel', secondary=aluno_turma_association, back_populates='alunos')

    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email


class DisciplinaModel(Base):
    __tablename__ = 'disciplinas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    codigo = Column(String(50), unique=True, nullable=False)
    turmas = relationship("TurmaModel", back_populates="disciplina")

    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo


# Modelo SQLAlchemy no controller
class TurmaModel(Base):
    __tablename__ = 'turmas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(50), unique=True, nullable=False)
    disciplina_id = Column(Integer, ForeignKey('disciplinas.id'))
    disciplina = relationship('DisciplinaModel', back_populates='turmas')
    alunos = relationship('AlunoModel', secondary=aluno_turma_association, back_populates='turmas')

    def __init__(self, codigo, disciplina_id, alunos):
        self.codigo = codigo
        self.disciplina_id = disciplina_id
        self.alunos = alunos