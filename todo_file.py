print("----------------------"
      "********** Welcome in my todos program **************\n"
      "************************************Designed by Japo Camero ******* "
      "-----------------------------------------")
while True:
      print()
      user_input = input("Type add, show, edit, complete or exit: ")
      user_input = user_input.strip()

      if user_input.startswith("add"):
            todo = user_input[4:]
            with open("todo.txt",'r') as file:
                  todos = file.readlines()
                  todos.append(todo)
            with open("todo.txt",'w') as file:
                  file.writelines(todos)
      elif user_input.startswith('edit'):
            number = int(user_input[5:])
            number = number - 1
            with open("todo.txt",'r') as file:
                  todos = file.readlines()
                  new_todos = input("Enter the new todo: ")
                  todos[number] = new_todos + "\n"
            with open("todo.txt",'w') as file:
                  file.writelines(todos)

      elif user_input.startswith('complete'):
            number = int(user_input[9:])

            with open("todo.txt",'r') as file:
                  todos = file.readlines()
            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("todo.txt", 'w') as file:
                  file.writelines(todos)
      elif user_input.startswith('show'):
            with open("todo.txt", 'r') as file:
                  todos = file.readlines()
            for index, items in enumerate(todos):
                  items = items.strip("\n")
                  row = (f"{index +1}.{items.title()}")
                  print(row)














