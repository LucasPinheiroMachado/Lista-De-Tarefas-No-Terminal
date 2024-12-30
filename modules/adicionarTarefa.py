import json, os

def adicionarTarefa(tarefa):
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
    
    dados.append(tarefa)

    with open('arquivo.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)