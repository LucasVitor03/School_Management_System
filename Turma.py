class Turma:
    def __init__(self,disciplina, codigo):
        self.disciplina = disciplina
        self.codigo = codigo
        self.alunos = []

    def adicionar_aluno_turma(self, aluno):
        self.alunos.append(aluno)

    def remover_aluno_turma(self, matricula):
        self.alunos = [aluno for aluno in self.alunos if aluno.matricula != matricula]

    def buscar_por_matricula(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno.mostrar_aluno()
        return print("Não foi possível encontrar o  aluno! Tente novamente.")

    def listar_alunos(self):
        print(f"-------Detalhes dos Alunos {self.codigo}:-------")
        for aluno in self.alunos:
            aluno.mostrar_aluno()
            print(45 * "#")
        return self.alunos


    def mostrar_turma(self):
        print(f"Código da Turma: {self.codigo}")
        self.disciplina.mostrar_disciplina()

