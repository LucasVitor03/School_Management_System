class Aluno:
    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def mostrar_aluno(self):
        print(f"O nome do aluno é: {self.nome}")
        print(f"O número da matrícula é: {self.matricula}")
        print(f"O e-mail do aluno é: {self.email}")

    def atualizar_aluno(self):
        self.nome = input("Digite o novo nome do aluno: ")
        self.matricula = input("Digite a nova matricula do aluno: ")
        self.email = input("Digite o novo email do aluno: ")
        print("\n----Os dados do aluno foram atualizados----")
        print(f"{self.mostrar_aluno()}")
