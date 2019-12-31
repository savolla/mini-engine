import os

def print_content(contents):
    print("·"*50)
    for index, value in enumerate(contents):
        print("{} - {}".format(index, value))
    print("·"*50)

def get_choice():
    print("(P)revious")
    print("·"*50)
    return input("choice: ")

def handle_choice(choice, current_path):
    is_done = False
    if choice == -1:
        current_path += '../'
    else:
        current_path += choice

        if os.path.isdir(current_path):
            current_path += '/'
        else:
            is_done = True
    
    return is_done, current_path

def select():
    current_path = os.getcwd() + '/'
    is_done = False

    while is_done == False:
        contents = os.listdir(current_path)
        
        print(current_path)

        print_content(contents)
        
        choice = get_choice()
        
        if choice == 'P':
            choice = -1
        else:
            choice = contents[int(choice)]

        is_done, current_path = handle_choice(choice, current_path)
        os.system("clear")
    
    return current_path
