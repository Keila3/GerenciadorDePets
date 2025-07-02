from Classe.pet import Pet
from time import  sleep

print('CRIE SEU PET:')
nome = input(str('EScolha um nome: '))
pet = Pet(nome, 50, 50, 50, 50)

while True:
    print('MENU:\n'
          '[1] Status\n'
          '[2] Dar comida\n'
          '[3] Brincar\n'
          '[4] Colocar para dormir\n'
          '[5] Levar ao veterinario\n'
          '[6] Sair')
    try:
      escolha = int(input("Digite uma opção: "))
    except ValueError:
        print('Digte um número valido')
        continue
    if escolha == 1:
        pet.status()
    elif escolha == 2:
        pet.comer()
    elif escolha == 3:
        pet.brincar()
    elif escolha == 4:
        pet.dormir()
    elif escolha == 5:
        pet.veterinario()
    elif escolha == 6:
        print('Saindo..')
        sleep(1)
        break
    else:
        print('Escolha uma opção valida.')