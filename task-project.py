#empty list to store the task
task = []

#function to add the task to the list
def add_task(title, description, time):
    task.append((title, description, time))
    
#function to remove a task from the list
def remove_task(title):
    for t in task:
        if t[0] == title:
            print(t)
            del t
    
#function to display all the task
def display_task():
    for t in task:
        print(t)

#main program
while True:
    print('\nTo-do list menu')
    print('\n1. Add a new task')
    print('2. Remove a task')
    print('3. Display a task')
    print('4. Quit')
    
    user_input = int(input('\nPlease enter the given choices: '))
    
    if user_input == 1:
        title = input('Enter the task title: ')
        description = input('Enter the task description: ')
        time = input('Enter the time taken to complete the task: ')
        add_task(title, description, time)
    elif user_input == 2:
        title = input('Please enter the task to be removed: ')
        remove_task(title)
    elif user_input == 3:
        display_task()
    elif user_input == 4:
        print('Exiting the program')
        break
    else:
        print('Please enter the valid choices: ')