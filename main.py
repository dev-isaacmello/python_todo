tarefas_pendentes = []
tarefas_concluidas = []

def adiconar_tarefas():
    descricao = input("Digite a descrição da tarefa: ")
    relevancia = int(input("Digite a relevância da tarefa (1-5): "))
    tempo = int(input("Digite o tempo estimado da tarefas (em minutos):"))
    tarefa = [descricao, relevancia, tempo]
    tarefas_pendentes.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def editar_tarefa():
    if not tarefas_pendentes:
        print("Nenhuma tarefa pendente para editar.")
        return
    mostrar_tarefas(tarefas_pendentes)
    idx = int(input("Digite o índice da tarefa que deseja editar: "))
    if 0 <= idx < len(tarefas_pendentes):
        nova_desc = input("Digite a nova descrição da tarefa: ")
        nova_rel = int(input("Digite a nova relevância da tarefa (1-5): "))
        novo_tempo = int(input("Digite o novo tempo estimado da tarefa (em minutos): "))
        tarefas_pendentes[idx] = [nova_desc, nova_rel, novo_tempo]
        print("Tarefa adicionada com sucesso!")
    else:
        print("Índice inválido. Tente novamente. \n")

def deletar_tarefa():
    if not tarefas_pendentes:
        print("Nenhuma tarefa pendente para deletar.")
        return
    mostrar_tarefas(tarefas_pendentes)
    idx = int(input("Digite o indice da tarefa que deseja Deletar: "))
    if 0 <= idx < len(tarefas_pendentes):
        tarefas_pendentes.pop(idx)
        print("Tarefa deletada com sucesso!")
    else:
        print("Índice inválido. Tente novamente. \n")

def concluir_tarefa():
    if not tarefas_pendentes:
        print("Nenhuma tarefa pendente.")
        return
    mostrar_tarefas(tarefas_pendentes)
    idx = int(input("Digite o índice da tarefa que deseja concluir: "))
    if 0 <= idx < len(tarefas_pendentes):
        tarefa = tarefas_pendentes.pop(idx)
        tarefas_concluidas.append(tarefa)
        print("Tarefa concluida com sucesso!")
    else:
        print("Índice inválido. Tente novamente. \n")

def ver_tarefa():
    tipo = input("Visualizar Pendentes ou Concluídas? (P/C): ").lower()
    lista = tarefas_pendentes if tipo == 'p' else tarefas_concluidas

    if not lista:
        print("Nenhuma tarefa encontrada.")
        return

    print("Ordernar por: 1) Ordem de adição 2) Relevância 3) Tempo")
    criterio = input("Digite o criterio da ordem: ")

    if criterio == '2':
        ordenada = ordenar_por_rel(lista)
    elif criterio == '3':
        ordenada = ordenar_por_tempo(lista)
    else:
        ordenada = lista

    mostrar_tarefas(ordenada)

def mostrar_tarefas(lista):
    for i, tarefa in enumerate(lista):
        print(f"{i}: Descrição: {tarefa[0]} | Relevância: {tarefa[1]} | Tempo: {tarefa[2]} min")
    print()

def ordenar_por_tempo(lista):
    return sorted(lista, key=lambda t: t[2])

def ordenar_por_rel(lista):
    return sorted(lista, key=lambda t: t[1])

def menu():
    while True:
        print("1. Adicionar tarefa")
        print("2. Editar tarefa")
        print("3. Deletar tarefa")
        print("4. Concluir tarefa")
        print("5. Ver tarefas")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adiconar_tarefas()
        elif opcao == "2":
            editar_tarefa()
        elif opcao == "3":
            deletar_tarefa()
        elif opcao == "4":
            concluir_tarefa()
        elif opcao == "5":
            ver_tarefa()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

