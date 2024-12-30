import json, os

def excluirTarefa(id):
    tarefas = []
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
        if not tarefa['id'] == id:
            tarefas.append(tarefa)

    with open('arquivo.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)