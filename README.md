# 🧩 Gerenciador de Tarefas Ágil

Projeto acadêmico da disciplina de Engenharia de Software, desenvolvido para simular a criação de um sistema ágil no GitHub. O objetivo é aplicar práticas modernas de desenvolvimento, planejamento, controle de qualidade e simulação de mudanças usando metodologias ágeis.

---

## 🧠 Objetivo do Projeto

Desenvolver um sistema simples de gerenciamento de tarefas, com funcionalidades básicas de CRUD, utilizando boas práticas de versionamento, testes automatizados e metodologias ágeis.

---

## 📌 Escopo do Projeto

- CRUD de tarefas (Criar, Listar, Atualizar, Excluir)
- Planejamento com Kanban (Projects do GitHub)
- Testes automatizados com `pytest`
- Pipeline de CI com GitHub Actions
- Simulação de mudança no escopo
- Controle de versão com commits descritivos

---

## 🚀 Metodologia Utilizada

- **Metodologia Ágil:** Kanban
- **Controle de Qualidade:** Testes unitários com Pytest
- **CI/CD:** GitHub Actions
- **Gestão de Projeto:** Projects (Kanban) no GitHub

---

## 🛠️ Como Executar o Projeto

🚀 Como executar o projeto
Para executar este projeto, é necessário ter o Python 3.10 ou superior instalado em sua máquina.

Primeiro, faça o clone do repositório e acesse a pasta do projeto. Recomenda-se a criação de um ambiente virtual para instalar as dependências de forma isolada, utilizando o comando python -m venv venv. Em seguida, ative o ambiente virtual e instale as dependências listadas no arquivo requirements.txt com pip install -r requirements.txt.

Após a configuração, basta executar o arquivo main.py para iniciar o sistema e interagir com as funcionalidades de gerenciamento de tarefas. Caso deseje validar a integridade do código, é possível rodar os testes automatizados utilizando o comando pytest, que está configurado para ser executado diretamente no GitHub Actions a cada push.

🔄 Simulação de Mudança de Escopo
Durante o projeto, foi solicitada uma mudança de escopo: adicionar a funcionalidade de filtrar tarefas por status.

Ações realizadas:

A funcionalidade filtrar_tarefas_por_status() foi implementada.

Testes foram adicionados no arquivo test_tarefas.py.

O quadro Kanban foi atualizado com uma nova tarefa representando a mudança.

Esta alteração está documentada aqui no README.

Essa simulação representa um cenário real de adaptação a mudanças em um projeto ágil.