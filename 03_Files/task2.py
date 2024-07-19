'''
In this make task, you should write a simple note taking program. It should wait for user input and do the following depending on it: 
1. All saved notes are loaded to a list notebook from the file notebook.txt
2. The user can enter a short message that is appended to the list notebook.
3. Show all notes
4: The notebook is stored in a file called notebook.txt and the program is terminated
'''

def print_menu():
    print('\n')
    print(20*'-')
    print('1. Load notes from storage')
    print('2. Add new note')
    print('3. Show all notes')
    print('4. Close program and save notes to file')
    print(20*'-')
    print('\n')
    choice = int(input())
    return choice

def load_notes(notebook):
    fileHandler = open('03_Files/notebook.txt')
    for note in fileHandler: 
        notebook.append(note)
    return notebook

def add_note(notebook):
    note = input('Enter new note: ') + '\n'
    notebook.append(note)
    return notebook

def show_notes(notebook):
    print(20*'-')
    for note in notebook:
        print(note)
    print(20*'-')

def save_notebook(notebook):
    fileHandler = open('03_Files/notebook.txt', 'w') 
    for note in notebook:
        fileHandler.write(note)
    print('Goodbye!')



notebook = []

while True:
    choice = print_menu()
    if choice == 1:
        notebook = load_notes(notebook)
    elif choice == 2:
        add_note(notebook)
    elif choice == 3:
        show_notes(notebook)
    elif choice == 4:
        save_notebook(notebook)
        break
    else:
        print('Invalid input')