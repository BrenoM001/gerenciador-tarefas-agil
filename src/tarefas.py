tarefas = []

def criar_tarefa(titulo, descricao, status="A Fazer"):
    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "status": status
    }
    tarefas.append(tarefa)
    return tarefa

def listar_tarefas():
    return tarefas

def filtrar_tarefas_por_status(status):
    return [tarefa for tarefa in tarefas if tarefa["status"] == status]
