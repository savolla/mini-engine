from include.string_search_engine import Engine
from include.select import select
import os

def main():
    engine = Engine()
    choice = ""

    while choice != 'Q':
        choice = input("(A)dd File, (S)earch, (Q)uit\n\nEnter choice: ")
        
        os.system("clear")

        if choice == 'A':
            path = select() 
            #engine.set_file_path(select())
            engine.set_file_path(path)
        elif choice =='S':
            pattern = input("Search pattern: ")
            
            found_at, full_match = engine.search(pattern)
    
            if found_at == None:
                print("Aradığınız kelime ve hiçbir yerde bulunamadı.")
                continue

            if not(full_match):
                choice_2 = int(input("Did you mean: {}?\n\n1- Yes\n2- No\n\nEnter choice: ".format(found_at)))
                if choice_2 == 1:
                    found_at, full_match = engine.search(found_at)
                else:
                    continue

            engine.show_search_result(found_at)
            print(path)
            if path.split('.')[-1] == 'txt':
                os.system("vim "+'"'+path+'"')

            elif path.split('.')[-1] == 'pdf':
                os.system("zathura "+path)


main()
