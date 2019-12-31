import time

def horspool(text1, pattern):
    out = []
    shift = {}
    text_index = len(pattern) - 1
    text = text1.lower()
    
    for index, char in enumerate(pattern[:-1]):
        shift[char] = len(pattern) - index - 1 
    
    word_list = " ".join(text.split('\n')).split()
    
    ms = time.time()
    while text_index < len(text) - 1:
        pattern_index = len(pattern) - 1
        tmp_text_index = text_index

        skip = len(pattern)
        control = True
    
        while tmp_text_index > text_index - len(pattern):
            if pattern[pattern_index] != text[tmp_text_index]:
                try:
                    skip = shift[text[text_index]]
                except:
                    pass
    
                control = False
                break
            
            tmp_text_index -= 1
            pattern_index -= 1
        
        if control == True:
            out.append((text_index-len(pattern)+1, text_index+1))
    
        text_index += skip
    
    ms = time.time() - ms

    if out == []:
        return None, word_list

    print("Arama sonuçları {}sn içerisinde bulundu.".format(ms))
    return out, None
