import json

tarefas_pendentes = []
tarefas_concluidas = []

# salva as listas de tarefas pendentes e concluídas em um arquivo JSON
def salvar_tarefas_em_arquivo(nome_arquivo="tarefas.json"):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump({
            "pendentes": tarefas_pendentes,
            "concluidas": tarefas_concluidas
        }, f, indent=4)
    print(f"Tarefas salvas em '{nome_arquivo}' com sucesso!")

# carrega as listas de tarefas pendentes e concluídas de um arquivo JSON
def carregar_tarefas_de_arquivo(nome_arquivo="tarefas.json"):
    global tarefas_pendentes, tarefas_concluidas
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
            tarefas_pendentes = dados.get("pendentes", [])
            tarefas_concluidas = dados.get("concluidas", [])
        print(f"Tarefas carregadas de '{nome_arquivo}' com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhuma tarefa carregada.")
    except json.JSONDecodeError:
        print("Erro ao carregar o arquivo. Verifique se o conteúdo está no formato correto.")

# adiciona uma nova tarefa à lista de tarefas pendentes
def adiconar_tarefas():
    descricao = input("Digite a descrição da tarefa: ")
    relevancia = int(input("Digite a relevância da tarefa (1-5): "))
    tempo = int(input("Digite o tempo estimado da tarefas (em minutos): "))
    tarefa = [descricao, relevancia, tempo]
    tarefas_pendentes.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# edita uma tarefa existente na lista de tarefas pendentes
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
        print("Tarefa editada com sucesso!")
    else:
        print("Índice inválido. Tente novamente.\n")

# remove uma tarefa da lista de tarefas pendentes
def deletar_tarefa():
    if not tarefas_pendentes:
        print("Nenhuma tarefa pendente para deletar.")
        return
    mostrar_tarefas(tarefas_pendentes)
    idx = int(input("Digite o índice da tarefa que deseja deletar: "))
    if 0 <= idx < len(tarefas_pendentes):
        tarefas_pendentes.pop(idx)
        print("Tarefa deletada com sucesso!")
    else:
        print("Índice inválido. Tente novamente.\n")

# move uma tarefa da lista de tarefas pendentes para a lista de tarefas concluídas
def concluir_tarefa():
    if not tarefas_pendentes:
        print("Nenhuma tarefa pendente.")
        return
    mostrar_tarefas(tarefas_pendentes)
    idx = int(input("Digite o índice da tarefa que deseja concluir: "))
    if 0 <= idx < len(tarefas_pendentes):
        tarefa = tarefas_pendentes.pop(idx)
        tarefas_concluidas.append(tarefa)
        print("Tarefa concluída com sucesso!")
    else:
        print("Índice inválido. Tente novamente.\n")

# exibe as tarefas pendentes ou concluídas, com opções de ordenação
def ver_tarefa():
    tipo = input("Visualizar Pendentes ou Concluídas? (P/C): ").lower()
    lista = tarefas_pendentes if tipo == 'p' else tarefas_concluidas

    if not lista:
        print("Nenhuma tarefa encontrada.")
        return

    print("Ordenar por: 1) Ordem de adição 2) Relevância 3) Tempo")
    criterio = input("Digite o critério da ordem: ")

    if criterio == '2':
        ordenada = ordenar_por_rel(lista)
    elif criterio == '3':
        ordenada = ordenar_por_tempo(lista)
    else:
        ordenada = lista

    mostrar_tarefas(ordenada)

# mostra as tarefas de uma lista específica no formato de índice e detalhes
def mostrar_tarefas(lista):
    for i, tarefa in enumerate(lista):
        print(f"{i}: Descrição: {tarefa[0]} | Relevância: {tarefa[1]} | Tempo: {tarefa[2]} min")
    print()

# ordena uma lista de tarefas pelo tempo estimado
def ordenar_por_tempo(lista):
    return sorted(lista, key=lambda t: t[2])

# ordena uma lista de tarefas pela relevância
def ordenar_por_rel(lista):
    return sorted(lista, key=lambda t: t[1])

# exibe o menu principal e gerencia a interação com o usuário
def menu():
    # carrega as tarefas do arquivo ao iniciar
    carregar_tarefas_de_arquivo() 
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
            salvar_tarefas_em_arquivo()  # Salva as tarefas ao sair
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
