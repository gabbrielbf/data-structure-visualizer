[🇧🇷 Português](./README.pt-BR.md) | [🇬🇧 English](./README.md)

<p align="center">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
</p>

# 🚀 Data Structure Visualizer (Stacks and Queues)

This project was developed for study purposes during the 1st semester of the Systems Analysis and Development (SAD) course. The idea was to create an interactive simulator in **Python** via terminal to visualize, in practice, the operation of two of the most fundamental linear data structures in computing: **Stacks (LIFO)** and **Queues (FIFO)**.

The system features interactive menus, integrated theoretical concepts, and input validations to ensure smooth, error-free navigation in real time.

---
## 🛠️ How does the project work?

To apply best practice concepts and maintain clean, modular, and easy-to-maintain code, the logic was fully separated by responsibilities:

* **`main.py`**: Entry point of the application, responsible for starting the program while keeping the scope encapsulated.
* **`src/structures.py`**: Main engine managing program execution (`run_code`) and operations on the structures (add, remove, and display).
* **`src/classes.py`**: Contains the necessary abstractions and representations for data type management.
* **`src/menu.py`**: Centralizes terminal interface utilities, such as numbered menus, validated data reading, and screen clearing.
* **`src/lessons.py`**: Dedicated file for storing educational texts, theoretical concepts (LIFO and FIFO), and system banners.

---

## 💡 Demonstrated Concepts

* **Stack (LIFO - Last In, First Out):** The last element to enter is the first to be removed (example: stack of plates or browser history).
* **Queue (FIFO - First In, First Out):** The first element to enter is the first to be removed (example: bank line or print queue).

---

## 📃 License

Esse projeto está sob a licença MIT.

---

## 🚀 How to run it on your machine

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/gabbrielbf/data-structure-visualizer.git](https://github.com/gabbrielbf/data-structure-visualizer.git)
   cd data-structure-visualizer