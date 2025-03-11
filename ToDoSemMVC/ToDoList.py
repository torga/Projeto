class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Tarefa "{task}" adicionada!')

    def list_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa disponível.")
        else:
            print("Lista de tarefas:")
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')
    
    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Tarefa "{removed_task}" removida!')
        else:
            print("Número de tarefa inválido.")


def main():
    todo = ToDoList()
    while True:
        print("\nOpções:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Excluir Tarefa")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            task = input("Digite a nova tarefa: ")
            todo.add_task(task)
        elif opcao == "2":
            todo.list_tasks()
        elif opcao == "3":
            todo.list_tasks()
            try:
                task_number = int(input("Digite o número da tarefa a ser removida: "))
                todo.delete_task(task_number)
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()