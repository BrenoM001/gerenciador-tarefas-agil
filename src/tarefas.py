tarefas = []  # Lista de tarefas
proximo_id = 1  # ID inicial

# Cria uma nova tarefa
def criar_tarefa(titulo, descricao, status="A Fazer"):
    global proximo_id
    tarefa = {
        "id": proximo_id,
        "titulo": titulo,
        "descricao": descricao,
        "status": status
    }
    tarefas.append(tarefa)
    proximo_id += 1
    return tarefa

# Lista todas as tarefas
def listar_tarefas():
    return tarefas

# Filtra tarefas por status
def filtrar_tarefas_por_status(status):
    return [tarefa for tarefa in tarefas if tarefa["status"] == status]

# Atualiza uma tarefa pelo ID
def atualizar_tarefa(id, novo_titulo=None, nova_descricao=None, novo_status=None):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            if novo_titulo is not None:
                tarefa["titulo"] = novo_titulo
            if nova_descricao is not None:
                tarefa["descricao"] = nova_descricao
            if novo_status is not None:
                tarefa["status"] = novo_status
            return tarefa
    return None  # Se não encontrar

# Remove uma tarefa pelo ID
def deletar_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return tarefa
    return None  # Se não encontrar