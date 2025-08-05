import pytest
from src import tarefas

# Limpa os dados antes de cada teste
def setup_function():
    tarefas.tarefas.clear()
    tarefas.proximo_id = 1

# Testa a criação de uma tarefa
def test_criar_tarefa():
    resultado = tarefas.criar_tarefa("Estudar", "Estudar Python para o projeto")
    assert resultado["titulo"] == "Estudar"
    assert resultado["descricao"] == "Estudar Python para o projeto"
    assert resultado["status"] == "A Fazer"
    assert resultado["id"] == 1

# Testa a listagem de tarefas
def test_listar_tarefas():
    tarefas.criar_tarefa("Tarefa 1", "Desc 1")
    tarefas.criar_tarefa("Tarefa 2", "Desc 2")
    lista = tarefas.listar_tarefas()
    assert len(lista) == 2

# Testa o filtro por status
def test_filtrar_tarefas_por_status():
    tarefas.criar_tarefa("Tarefa 1", "Desc", "A Fazer")
    tarefas.criar_tarefa("Tarefa 2", "Desc", "Concluído")
    resultado = tarefas.filtrar_tarefas_por_status("Concluído")
    assert len(resultado) == 1
    assert resultado[0]["titulo"] == "Tarefa 2"

# Testa a atualização de uma tarefa
def test_atualizar_tarefa():
    tarefa = tarefas.criar_tarefa("Original", "Desc")
    atualizada = tarefas.atualizar_tarefa(tarefa["id"], novo_titulo="Atualizada", novo_status="Em Progresso")
    assert atualizada["titulo"] == "Atualizada"
    assert atualizada["status"] == "Em Progresso"

# Testa a exclusão de uma tarefa
def test_deletar_tarefa():
    tarefa = tarefas.criar_tarefa("Apagar", "Desc")
    deletada = tarefas.deletar_tarefa(tarefa["id"])
    assert deletada["titulo"] == "Apagar"
    assert len(tarefas.listar_tarefas()) == 0

# Testa a atualização de uma tarefa que não existe
def test_atualizar_tarefa_inexistente():
    resultado = tarefas.atualizar_tarefa(999, novo_titulo="Nada")
    assert resultado is None

# Testa a exclusão de uma tarefa que não existe
def test_deletar_tarefa_inexistente():
    resultado = tarefas.deletar_tarefa(999)
    assert resultado is None