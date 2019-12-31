from os import system
from math import ceil

def get_file_format_of( file_path ):
    return file_path.split('.')[-1]

def extract_text_from_pdf( pdf_file ):
    system("pdftotext " + pdf_file + " tmp") # third party "pdftotext"

    with open('tmp','r') as file:
        extracted_text = file.read()

    system("rm tmp")
    return extracted_text

def extract_text_from_doc( doc_file ):
    system("catdoc " + doc_file + " > tmp.txt")
    with open("tmp.txt","r") as file:
        extracted_text = file.read()

    return extracted_text

def extract_text_from_docx( doc_file ):
    system("unzip -p " + doc_file + " word/document.xml | sed -e 's/<[^>]\{1,\}>//g; s/[^[:print:]]\{1,\}//g' > tmp.txt")
    
    with open('tmp.txt','r') as file:
        extracted_text = file.read()
    
    tmp = []
    for index in range(0, ceil(len(extracted_text.split())/10), 10):
        tmp.append(extracted_text.split()[index+1:index+10])
    
    tmp = map(lambda x: " ".join(x), tmp)
    tmp = "\n".join(list(tmp))

    system("rm tmp.txt")
    return tmp

def extract_text_from_txt( txt_file ):
    with open(txt_file, 'r') as file:
        extracted_text = file.read()

    return extracted_text

# base function. uses all those above ^
def extract_text( file_path ):
    extension = get_file_format_of( file_path )

    return eval("extract_text_from_{}(file_path)".format(extension))

