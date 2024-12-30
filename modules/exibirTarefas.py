import json, os

def exibirTarefas():
    if os.path.exists('arquivo.json'):
        with open('arquivo.json', 'r', encoding='utf-8') as arquivo:
            try:
                dados = json.load(arquivo)
                if not isinstance(dados, list):
                    dados = [dados]
            except json.JSONDecodeError:
                dados = []
    else:
        dados = []

    for tarefa in dados:
        for chave, valor in tarefa.items():
            print(f'{chave}: {valor}', end='  |  ')
        print() 