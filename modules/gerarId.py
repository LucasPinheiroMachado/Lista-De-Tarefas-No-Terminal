import json, os

def gerarId():
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

    def maiorId(dadosTarefa):
        maiorId = 0
        for tarefa in dadosTarefa:
            if tarefa['id'] > maiorId:
                maiorId = int(tarefa['id'])
        novoId = maiorId + 1
        return novoId

    novo_id = maiorId(dados)

    return novo_id