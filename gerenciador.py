def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"A tarefa '{nome_tarefa}' foi adicionada ao campo.")

def ver_tarefas(tarefas):
    print("\nLista de tarefas:")

    for indice, tarefa in enumerate(tarefas, start=1):
        status = "OK" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
        
    
def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else: 
         print("indice de tarefa invalido")
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) -1 
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print(f"tarefa {indice_tarefa} marcada como completada")
    return    

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("tarefas completadas removidas")
    return         

tarefas = []
while True:
    print("\nMenu gerenciador de tarefas")
    print("1. adicionar tarefas")
    print("2. ver tarefas")
    print("3. atualizar tarefa")
    print("4. completar tarefa")
    print("5. deletar tarefas completas")
    print("6. sair")

    escolha = input("escreve oq tu mandas: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja inserir: ")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == "2":
        ver_tarefas(tarefas)

    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)    
    
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input("digite o numero da tarefa que deseja completar:")
        completar_tarefa(tarefas, indice_tarefa) 

    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)

    elif escolha == "6":
        break

print("Fim do programa")