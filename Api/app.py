from flask import Flask, request, jsonify
from Database.models import *
from Database.connection import create_db, create_session, database

app = Flask(__name__)

# Configuração do banco de dados
engine = database()
session = create_session(engine)

# Rota para adicionar um aluno
@app.route('/alunos', methods=['POST'])
def add_aluno():
    data = request.json
    novo_aluno = AlunoModel(nome=data['nome'], matricula=data['matricula'], email=data['email'])
    session.add(novo_aluno)
    session.commit()
    return jsonify({"message": "Aluno adicionado com sucesso!"}), 201

# Rota para listar todos os alunos
@app.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = session.query(AlunoModel).all()
    return jsonify([{"nome": aluno.nome, "matricula": aluno.matricula, "email": aluno.email} for aluno in alunos]), 200

# Rota para atualizar um aluno
@app.route('/alunos/<matricula>', methods=['PUT'])
def update_aluno(matricula):
    data = request.json
    aluno = session.query(AlunoModel).filter_by(matricula=matricula).first()
    if aluno:
        aluno.nome = data.get('nome', aluno.nome)
        aluno.email = data.get('email', aluno.email)
        session.commit()
        return jsonify({"message": "Aluno atualizado com sucesso!"}), 200
    return jsonify({"message": "Aluno não encontrado!"}), 404

# Rota para deletar um aluno
@app.route('/alunos/<matricula>', methods=['DELETE'])
def delete_aluno(matricula):
    aluno = session.query(AlunoModel).filter_by(matricula=matricula).first()
    if aluno:
        session.delete(aluno)
        session.commit()
        return jsonify({"message": "Aluno deletado com sucesso!"}), 200
    return jsonify({"message": "Aluno não encontrado!"}), 404

# Rota para adicionar uma disciplina
@app.route('/disciplinas', methods=['POST'])
def add_disciplina():
    data = request.json
    nova_disciplina = DisciplinaModel(nome=data['nome'], codigo=data['codigo'])
    session.add(nova_disciplina)
    session.commit()
    return jsonify({"message": "Disciplina adicionada com sucesso!"}), 201

# Rota para listar todas as disciplinas
@app.route('/disciplinas', methods=['GET'])
def get_disciplinas():
    disciplinas = session.query(DisciplinaModel).all()
    return jsonify([{"nome": disciplina.nome, "codigo": disciplina.codigo} for disciplina in disciplinas]), 200

# Rota para adicionar uma turma
@app.route('/turmas', methods=['POST'])
def add_turma():
    data = request.json
    disciplina = session.query(DisciplinaModel).filter_by(codigo=data['disciplina_codigo']).first()
    if disciplina:
        nova_turma = TurmaModel(codigo=data['codigo'], disciplina_id=disciplina.id)
        session.add(nova_turma)
        session.commit()
        return jsonify({"message": "Turma adicionada com sucesso!"}), 201
    return jsonify({"message": "Disciplina não encontrada!"}), 404

# Rota para listar todas as turmas
@app.route('/turmas', methods=['GET'])
def get_turmas():
    turmas = session.query(TurmaModel).all()
    return jsonify([{"codigo": turma.codigo, "disciplina_id": turma.disciplina_id} for turma in turmas]), 200

# Iniciar o servidor
if __name__ == '__main__':
    create_db(engine) #cria se não existir
    app.run(debug=True)
