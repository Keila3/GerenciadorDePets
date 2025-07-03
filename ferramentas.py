import os
import json

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def salvar_pet(pet):
    dados={
        "nome": pet.nome,
        "fome": pet.fome,
        "energia": pet.energia,
        "humor": pet.humor,
        "saude": pet.saude
    }
    with open("pet.json", "w") as f:
        json.dump(dados, f)

def carregar_pet():
    if not os.path.exists("pet.json"):
        print("Nenhum pet salvo foi encontrado.")
        return None
    with open("pet.json", "r") as f:
        dados = json.load(f)
        return Pet(
            dados["nome"],
            dados["fome"],
            dados["energia"],
            dados["humor"],
            dados["saude"]
        )