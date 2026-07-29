### `README_pt-BR.md` (Versão em português)

<p align="right">
  <a href="README_pt-BR.md">🇧🇷 Português</a> | 
  <a href="README.md">🇬🇧 English</a>
</p>

# 🚀 Visualizador de Estruturas de Dados (Pilhas e Filas)

Este projeto foi desenvolvido para fins de estudo durante o 1º semestre do curso de Análise e Desenvolvimento de Sistemas (ADS). A ideia foi criar um simulador interativo em **Python** via terminal para visualizar, na prática, o funcionamento de duas das estruturas de dados lineares mais fundamentais da computação: **Pilhas (LIFO)** e **Filas (FIFO)**.

O sistema possui menus interativos, conceitos teóricos integrados e validações de entrada para garantir uma navegação fluida e sem erros em tempo real.

---

## 🛠️ Como o projeto funciona?

Para aplicar conceitos de boas práticas e manter um código limpo, modular e fácil de manter, a lógica foi totalmente separada por responsabilidades:

* **`main.py`**: Ponto de entrada da aplicação, responsável por iniciar o programa mantendo o escopo encapsulado.
* **`src/structures.py`**: Motor principal que gerencia a execução do programa (`run_code`) e as operações nas estruturas (adicionar, remover e exibir).
* **`src/classes.py`**: Contém as abstrações e representações necessárias para o gerenciamento dos tipos de dados.
* **`src/menu.py`**: Centraliza utilitários de interface de terminal, como menus numerados, leitura de dados validada e limpeza de tela.
* **`src/lessons.py`**: Arquivo dedicado ao armazenamento de textos educacionais, conceitos teóricos (LIFO e FIFO) e banners do sistema.

---

## 💡 Conceitos Demonstrados

* **Pilha (LIFO - Last In, First Out / Último a Entrar, Primeiro a Sair):** O último elemento a entrar é o primeiro a ser removido (exemplo: pilha de pratos ou histórico do navegador).
* **Fila (FIFO - First In, First Out / Primeiro a Entrar, Primeiro a Sair):** O primeiro elemento a entrar é o primeiro a ser removido (exemplo: fila de banco ou fila de impressão).

---

