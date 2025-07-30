def criar_tarefa(nome):
    if nome:
        return f"Tarefa '{nome}' criada com sucesso"
    return "Nome da tarefa inválido"