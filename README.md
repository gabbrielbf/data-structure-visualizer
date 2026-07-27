# 🚀 Visualizador de Estrutura de Dados (Pilhas e Filas)

Este é um projeto desenvolvido para fins de estudo no 1º semestre do curso de Análise e Desenvolvimento de Sistemas (ADS). A ideia foi criar um simulador interativo em **Python** via terminal para visualizar, na prática, o funcionamento de duas das estruturas de dados lineares mais fundamentais da computação: **Pilhas (Stack - LIFO)** e **Filas (Queue - FIFO)**.

O sistema conta com menus interativos, conceitos teóricos integrados e validações de entrada para garantir uma navegação fluida e sem erros em tempo real.

---
## 🛠️ Como o projeto funciona?

Para aplicar conceitos de boas práticas e manter o código limpo, modular e de fácil manutenção, a lógica foi totalmente separada por responsabilidades:

* **`main.py`**: Ponto de entrada da aplicação, encarregado de iniciar o programa mantendo o escopo encapsulado.
* **`logica_projeto/estruturas.py`**: Motor principal que gerencia a execução do programa (`run_code`) e as operações nas estruturas (adicionar, remover e exibir).
* **`logica_projeto/classes.py`**: Contém as abstrações e representações necessárias para o gerenciamento dos tipos de dados.
* **`logica_projeto/menu.py`**: Centraliza os utilitários de interface via terminal, como menus numerados, leitura validada de dados e limpeza de tela.
* **`logica_projeto/lessons.py`**: Arquivo dedicado a armazenar os textos educativos, conceitos teóricos (LIFO e FIFO) e banners do sistema.

---

## 💡 Conceitos Demonstrados

* **Pilha (LIFO - Last In, First Out):** O último elemento a entrar é o primeiro a ser removido (exemplo: pilha de pratos ou histórico de navegação).
* **Fila (FIFO - First In, First Out):** O primeiro elemento a entrar é o primeiro a ser removido (exemplo: fila de banco ou fila de impressão).

---

## 🚀 Como rodar na sua máquina

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
   cd SEU_REPOSITORIO