class Disciplina:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def mostrar_disciplina(self):
        print(f"Nome da disciplina: {self.nome}")
        print(f"Codigo da disciplina: {self.codigo}")
