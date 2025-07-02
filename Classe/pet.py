class Pet:
    def __init__(self, nome, fome, energia, humor, saude):
        self.nome = nome
        self.fome = fome
        self.energia = energia
        self.humor = humor
        self.saude = saude



    def comer(self):
        print(f'{self.nome} está comendo..')
        self.fome -= 20
        self.humor += 10
        self.ajustar_limites()

    def brincar(self):
        print(f'{self.nome} está brincando..')
        self.humor += 20
        self.fome -= 10
        self.energia -= 30
        self.ajustar_limites()

    def dormir(self):
        print(f'{self.nome} está dormindo..')
        self.energia += 100
        self.fome -= 15
        self.humor += 10
        self.ajustar_limites()

    def veterinario(self):
        if self.saude <= 50:
            print(f'{self.nome} foi ao veterinário.')
            self.saude += 40
            self.humor -= 5
            self.energia -= 5
            self.ajustar_limites()
        else:
            print(f'{self.nome} está saudável e não precisa ir ao veterinário.')

    def ajustar_limites(self):
        self.fome = max(0, min(self.fome, 100))
        self.saude = max(0, min(self.saude, 100))
        self.energia = max(0, min(self.energia, 100))
        self.humor = max(0, min(self.humor, 100))

    def status(self):
        print('-=-' * 20)
        print(f'NOME: {self.nome}\n'
              f'HP: {self.saude}\n'
              f'FOME: {self.fome}\n'
              f'SONO: {self.energia}\n'
              f'HUMOR: {self.humor}')
        print('-=-' * 20)




