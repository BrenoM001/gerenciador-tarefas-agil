from src.tarefas import criar_tarefa

def test_criar_tarefa_com_nome_valido():
    resultado = criar_tarefa("Estudar algoritmos")
    assert resultado == "Tarefa 'Estudar algoritmos' criada com sucesso"

def test_criar_tarefa_com_nome_vazio():
    resultado = criar_tarefa("")
    assert resultado == "Nome da tarefa inválido"