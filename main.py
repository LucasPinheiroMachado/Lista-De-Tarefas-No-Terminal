from modules import adicionarTarefa, excluirTarefa, exibirTarefas, gerarId

def switch_case(opcao):
    if opcao == 1:
        id = gerarId.gerarId()
        nomeTarefa = input('Digite a tarefa: ')
        tarefa = {'id': id, 'tarefa': nomeTarefa}
        adicionarTarefa.adicionarTarefa(tarefa)
    elif opcao == 2:
        id = int(input('Digite o id da tarefa a ser removida: '))
        excluirTarefa.excluirTarefa(id)
    elif opcao == 3:
        exibirTarefas.exibirTarefas()
    else:
        print("Opção inválida")


print(f'Menu de tarefas:\n')

print(f'\n\nO que você deseja fazer?\n\n1: Adicionar Tarefa\n2: Excluir Tarefa\n3: Ver Tarefas\n')
opcao = int(input('>'))

switch_case(opcao)