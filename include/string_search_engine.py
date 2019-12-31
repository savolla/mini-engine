from include.horspool import horspool as f_search
from include.levenshtein import levenshtein as d_search
from include.extract_text import extract_text
from colorama import init, Fore, Style


class Engine:
    def __init__(self):
        self.__file_path = ""
    
    def set_file_path(self, path):
        self.__file_path = path

    def get_text_from_file(self):
        self.text = extract_text(self.__file_path)

    def search(self, pattern):
        if self.__file_path == "":
            print("Öncelikle dosyayı belirtmeniz gerekiyor.")
            return 0

        self.get_text_from_file()
        result, word_list = f_search(self.text, pattern)

        if result == None:
            out = []
            for pattern_word in pattern.split():
                for word in word_list:
                    if d_search(pattern_word, word) <= int(len(pattern_word)*1/2):
                        out.append(word)
                        break
                
            if len(out) == 0:
                return None, False

            return " ".join(out), False

        return result, True

    def show_search_result(self, found_at):    
        init()
        
        for index, position in enumerate(found_at):
            try:
                line_begin = position[0] - self.text[:position[0]][::-1].index('\n')
            except:
                line_begin = 0

            try:
                line_end = position[1] + self.text[position[1]:].index('\n')
            except:
                line_end = -1

            line = self.text[line_begin:line_end]
            
            print("{}.".format(index+1), line[:position[0]-line_begin], end='')
            print(Fore.GREEN + line[position[0]-line_begin:position[1]-line_begin], end='')
            print(Style.RESET_ALL, end='')
            print(line[position[1]-line_begin:])

