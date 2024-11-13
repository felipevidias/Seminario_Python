# Definição de uma classe
class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som

    def fazer_som(self):
        return f"O {self.nome} faz '{self.som}'"

# Subclasse herdando de Animal
class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome, "au au")

    def correr(self):
        return f"O {self.nome} está correndo."

# Subclasse herdando de Animal
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome, "miau")

    def pular(self):
        return f"O {self.nome} está pulando."

def main():
    cachorro = Cachorro("Rex")
    gato = Gato("Mimi")

    print(cachorro.fazer_som())  # O Rex faz 'au au'
    print(cachorro.correr())     # O Rex está correndo.

    print(gato.fazer_som())      # O Mimi faz 'miau'
    print(gato.pular())          # O Mimi está pulando.

if __name__ == "__main__":
    main()
