from Classe.pet import Pet
from time import  sleep
from ferramentas import limpar_tela

print('CRIE SEU PET:')
nome = input(str('EScolha um nome: '))
pet = Pet(nome, 50, 50, 50, 50)

while True:
    limpar_tela()
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
        limpar_tela()
        pet.status()
        sleep(2)
    elif escolha == 2:
        limpar_tela()
        pet.comer()
        sleep(2)
    elif escolha == 3:
        limpar_tela()
        pet.brincar()
        sleep(2)
    elif escolha == 4:
        limpar_tela()
        pet.dormir()
        sleep(2)
    elif escolha == 5:
        limpar_tela()
        pet.veterinario()
        sleep(2)
    elif escolha == 6:
        limpar_tela()
        print('Saindo..')
        sleep(1)
        break
    else:
        print('Escolha uma opção valida.')

