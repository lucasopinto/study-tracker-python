import json
import os
from datetime import datetime

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)


def adicionar_tarefa(tarefas):
    titulo = input("Digite a tarefa: ")

    tarefa = {
        "titulo": titulo,
        "concluida": False,
        "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

    print("Tarefa adicionada com sucesso!\n")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.\n")
        return

    print("\n===== TAREFAS =====")

    for i, tarefa in enumerate(tarefas):
        status = "✅" if tarefa["concluida"] else "❌"

        print(f"{i + 1}. {status} {tarefa['titulo']}")
        print(f"   Criada em: {tarefa['data_criacao']}")

    print()


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    if not tarefas:
        return

    try:
        numero = int(input("Digite o número da tarefa: "))

        if 1 <= numero <= len(tarefas):
            tarefas[numero - 1]["concluida"] = True
            salvar_tarefas(tarefas)

            print("Tarefa concluída!\n")
        else:
            print("Número inválido.\n")

    except ValueError:
        print("Digite apenas números.\n")


def mostrar_estatisticas(tarefas):
    total = len(tarefas)
    concluidas = sum(t["concluida"] for t in tarefas)

    if total == 0:
        progresso = 0
    else:
        progresso = (concluidas / total) * 100

    print("\n===== ESTATÍSTICAS =====")
    print(f"Total de tarefas: {total}")
    print(f"Concluídas: {concluidas}")
    print(f"Progresso: {progresso:.1f}%\n")


def menu():
    tarefas = carregar_tarefas()

    while True:
        print("===== STUDY TRACKER =====")
        print("1 - Adicionar tarefa")
        print("2 - Ver tarefas")
        print("3 - Concluir tarefa")
        print("4 - Estatísticas")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            concluir_tarefa(tarefas)

        elif opcao == "4":
            mostrar_estatisticas(tarefas)

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida.\n")


menu()