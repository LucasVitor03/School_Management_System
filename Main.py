from Turma import Turma
from Aluno import Aluno
from Disciplina import Disciplina

aluno1 = Aluno("Lucas", 322126458, "lucas@hotmail.com")
aluno2 = Aluno("Grazi", 322126459, "grazi@gmail.com")
aluno3 = Aluno("Bernardo", 322126460, "bernardo@gmail.com")

disciplina1 = Disciplina("Sistemas Distribuídos", "SD101")
disciplina2 = Disciplina("Desenvolvimento WEB", "DEV102")

turma1 = Turma(disciplina1, "T01")
turma2 = Turma(disciplina2, "T02")


#Adicionando a Turma 1
turma1.adicionar_aluno_turma(aluno1)
turma1.adicionar_aluno_turma(aluno2)
#Adicionando a Turma 2
turma2.adicionar_aluno_turma(aluno3)
#Listando alunos da turma 1
turma1.listar_alunos()
#Listando alunos da turma
print("\n")
turma2.listar_alunos()
#Pesquisar aluno por matrícula
print("\n")
turma1.buscar_por_matricula(322126459)
#Atualizando dados de 1 aluno
print("\n")
aluno3.atualizar_aluno()
#Testar remover aluno de uma turma
print("\n")
turma1.remover_aluno_turma(322126459)
turma1.listar_alunos()