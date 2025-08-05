import pytest
from src import tarefas

def setup_function():
    # Limpa a lista de tarefas antes de cada teste
    tarefas.tarefas.clear()

def test_criar_tarefa():
    resultado = tarefas.criar_tarefa("Estudar", "Estudar Python para o projeto")
    assert resultado["titulo"] == "Estudar"
    assert resultado["descricao"] == "Estudar Python para o projeto"
    assert resultado["status"] == "A Fazer"
    assert resultado["id"] == 1

def test_listar_tarefas():
    tarefas.criar_tarefa("Tarefa 1", "Desc 1")
    tarefas.criar_tarefa("Tarefa 2", "Desc 2")
    lista = tarefas.listar_tarefas()
    assert len(lista) == 2

def test_filtrar_tarefas_por_status():
    tarefas.criar_tarefa("Tarefa 1", "Desc", "A Fazer")
    tarefas.criar_tarefa("Tarefa 2", "Desc", "Concluído")
    resultado = tarefas.filtrar_tarefas_por_status("Concluído")
    assert len(resultado) == 1
    assert resultado[0]["titulo"] == "Tarefa 2"
